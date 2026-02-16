#!/usr/bin/env python3
"""
Generate a consolidated submissions report from GitHub Issues.

This script processes GitHub issue data and creates a markdown table with submission details.

Usage:
    python3 generate_submissions_report.py [issues_json_file]
    
If no file is provided, the script will attempt to fetch issues using the GitHub CLI (gh).
"""

import json
import os
import re
import subprocess
import sys
from typing import Dict, List, Optional


def fetch_issues_from_github(owner: str, repo: str) -> List[Dict]:
    """Fetch issues from GitHub using gh CLI."""
    print("Fetching issues from GitHub using gh CLI...", file=sys.stderr)
    
    # Use gh CLI to fetch all issues
    cmd = [
        "gh", "issue", "list",
        "--repo", f"{owner}/{repo}",
        "--state", "all",
        "--limit", "1000",
        "--json", "number,title,body,labels,url"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        issues = json.loads(result.stdout)
        print(f"Fetched {len(issues)} issues from GitHub", file=sys.stderr)
        return issues
    except subprocess.CalledProcessError as e:
        print(f"Error fetching issues from GitHub CLI: {e}", file=sys.stderr)
        print(f"stderr: {e.stderr}", file=sys.stderr)
        print("\nTip: You can provide a JSON file with issues data as an argument", file=sys.stderr)
        print("     python3 generate_submissions_report.py issues.json", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON from GitHub CLI: {e}", file=sys.stderr)
        sys.exit(1)


def load_issues_from_file(filepath: str) -> List[Dict]:
    """Load issues from a JSON file."""
    print(f"Loading issues from file: {filepath}", file=sys.stderr)
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Handle different JSON structures
        if isinstance(data, list):
            issues = data
        elif isinstance(data, dict) and 'issues' in data:
            issues = data['issues']
        else:
            print(f"Error: Unexpected JSON structure in {filepath}", file=sys.stderr)
            sys.exit(1)
        
        print(f"Loaded {len(issues)} issues from file", file=sys.stderr)
        return issues
    except FileNotFoundError:
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}", file=sys.stderr)
        sys.exit(1)


def parse_issue_body(body: str) -> Dict[str, str]:
    """Parse the issue body to extract project name and repository URL."""
    project_name = "TBD"
    repo_url = "TBD"
    
    if not body:
        return {"project_name": project_name, "repo_url": repo_url}
    
    # Look for Project Name field (supports both ### and ## headers)
    project_name_match = re.search(r'##\s+Project Name\s*\n\s*([^\n]+)', body, re.IGNORECASE)
    if project_name_match:
        project_name = project_name_match.group(1).strip()
    
    # Look for Repository URL field (supports both ### and ## headers)
    repo_url_match = re.search(r'##\s+Repository URL\s*\n\s*([^\n]+)', body, re.IGNORECASE)
    if repo_url_match:
        repo_url = repo_url_match.group(1).strip()
    
    # If we didn't find the project name but found a repo URL, try to extract from repo
    if project_name == "TBD" and repo_url != "TBD":
        # Extract repo name from URL (e.g., https://github.com/owner/repo -> repo)
        repo_match = re.search(r'github\.com/[^/]+/([^/\s]+)', repo_url)
        if repo_match:
            project_name = repo_match.group(1)
    
    return {"project_name": project_name, "repo_url": repo_url}


def generate_markdown_table(issues_data: List[Dict]) -> str:
    """Generate a markdown table from issues data."""
    # Table header
    table = "| Issue Number | Project Name | Label | Repository URL | Issue URL |\n"
    table += "|--------------|--------------|-------|----------------|----------|\n"
    
    # Sort by issue number (descending)
    sorted_issues = sorted(issues_data, key=lambda x: x['number'], reverse=True)
    
    for issue in sorted_issues:
        table += f"| {issue['number']} | {issue['project_name']} | {issue['label']} | {issue['repo_url']} | {issue['issue_url']} |\n"
    
    return table


def main():
    """Main function to generate the submissions report."""
    owner = "microsoft"
    repo = "agentsleague-techconnect"
    
    # Check if a JSON file was provided as an argument
    if len(sys.argv) > 1:
        issues = load_issues_from_file(sys.argv[1])
    else:
        # Try to fetch from GitHub CLI
        issues = fetch_issues_from_github(owner, repo)
    
    # Filter for submission issues (those with [Submission]: in title or submission-related labels)
    submission_issues = []
    
    for issue in issues:
        title = issue.get('title', '')
        number = issue.get('number', 0)
        body = issue.get('body', '')
        labels = issue.get('labels', [])
        url = issue.get('url', '')
        
        # Check if this is a submission issue
        is_submission = (
            title.startswith('[Submission]:') or
            any(label.get('name', '') in ['submission', '🎨 Creative Apps', '🧠 Reasoning Agents', '💼 Enterprise Agents'] 
                for label in labels)
        )
        
        if not is_submission:
            continue
        
        # Extract labels
        label_names = [label.get('name', '') for label in labels]
        label_str = ', '.join(label_names) if label_names else 'TBD'
        
        # Parse issue body for project name and repo URL
        parsed_data = parse_issue_body(body)
        
        # Create issue URL from number
        issue_url = f"https://github.com/{owner}/{repo}/issues/{number}"
        
        submission_issues.append({
            'number': number,
            'project_name': parsed_data['project_name'],
            'label': label_str,
            'repo_url': parsed_data['repo_url'],
            'issue_url': issue_url
        })
    
    # Generate the markdown table
    if not submission_issues:
        print("No submission issues found.", file=sys.stderr)
        sys.exit(1)
    
    markdown_table = generate_markdown_table(submission_issues)
    
    # Write to output file
    output_file = "/home/runner/work/agentsleague-techconnect/agentsleague-techconnect/SUBMISSIONS.md"
    with open(output_file, 'w') as f:
        f.write(markdown_table)
    
    print(f"Submissions report generated successfully!", file=sys.stderr)
    print(f"Total submissions: {len(submission_issues)}", file=sys.stderr)
    print(f"Output written to: {output_file}", file=sys.stderr)
    print("\n" + markdown_table)


if __name__ == "__main__":
    main()
