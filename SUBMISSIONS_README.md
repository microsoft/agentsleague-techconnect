# Submissions Report

This directory contains a consolidated report of all project submissions for Agents League @ TechConnect.

## Files

- **SUBMISSIONS.md** - The consolidated submissions table with all project details
- **generate_submissions_report.py** - Python script to regenerate the report from GitHub Issues

## Report Contents

The `SUBMISSIONS.md` file contains a markdown table with the following columns:

- **Issue Number**: The GitHub issue number/ID
- **Project Name**: The name of the submitted project
- **Label**: The track label(s) assigned to the submission
- **Repository URL**: Link to the project's GitHub repository
- **Issue URL**: Link to the submission issue

## How to Regenerate the Report

### Prerequisites

- Python 3.6+
- GitHub CLI (`gh`) authenticated (optional, for live fetching)
- OR a JSON file with GitHub Issues data

### Using the Script

The script can work with a JSON file containing GitHub Issues data or fetch fresh data from GitHub:

```bash
# Option 1: Using a JSON file with issues data
python3 generate_submissions_report.py issues.json

# Option 2: Fetch directly from GitHub (requires authenticated gh CLI)
python3 generate_submissions_report.py

# The script will generate/update SUBMISSIONS.md
```

### JSON File Format

If providing a JSON file, it should contain an array of GitHub issues with the following fields:
- `number`: Issue number
- `title`: Issue title
- `body`: Issue body (containing project details)
- `labels`: Array of label objects with `name` field
- `url`: Issue URL

You can export issues from GitHub using:
```bash
gh issue list --repo microsoft/agentsleague-techconnect --state all --limit 1000 --json number,title,body,labels,url > issues.json
```

### Notes

- The script identifies submission issues by:
  - Issues with titles starting with `[Submission]:`
  - Issues with track labels (🎨 Creative Apps, 🧠 Reasoning Agents, 💼 Enterprise Agents)
- If any required field is missing, it will be marked as "TBD"
- Issues are sorted by issue number in descending order (newest first)

## Submission Statistics

The report is automatically updated whenever new submissions are added to the repository.
