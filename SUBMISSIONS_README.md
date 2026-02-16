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
- Access to GitHub Issues API (via MCP server or cached data)

### Using the Script

The script can work with cached GitHub Issues data or fetch fresh data:

```bash
# If you have cached issues data from GitHub MCP server
python3 generate_submissions_report.py

# The script will generate/update SUBMISSIONS.md
```

### Notes

- The script identifies submission issues by:
  - Issues with titles starting with `[Submission]:`
  - Issues with track labels (🎨 Creative Apps, 🧠 Reasoning Agents, 💼 Enterprise Agents)
- If any required field is missing, it will be marked as "TBD"
- Issues are sorted by issue number in descending order (newest first)

## Submission Statistics

The report is automatically updated whenever new submissions are added to the repository.
