# GitHub PR Analyzer

## Overview
This repository contains scripts for analyzing pull requests (PRs) on GitHub repositories. It includes tools for aggregating and formatting data about PRs.

## Prerequisites
- GitHub CLI (`gh`): [GitHub CLI](https://github.com/cli/cli)
- `jq`: [jq](https://stedolan.github.io/jq/)

## Commands

### gpa (github-pr-analyzer)
- **Description:** Analyzes PRs in a GitHub repository within a specified date range.
- **Usage:** `gpa --since=YYYY-MM-DD --until=YYYY-MM-DD --repo=orgName/repoName [--output=json|tsv] [--authors=author1,author2] [-v]`
- **Options:**
  - `--since`, `--until`: Date range for PR analysis.
  - `--repo`: Target GitHub repository.
  - `--output`: Output format (json or tsv).
  - `--authors`: Filter PRs by authors.
  - `-v`: Verbose mode.
- **Example:** `bin/gpa --since=2023-12-05 --until=2023-12-11 --repo=myOrg/myRepo --output=json`

### json-aggregator
- **Description:** Aggregates PR data over multiple iterations into a single JSON object.
- **Usage:** `json-aggregator --iter-start=YYYY-MM-DD --iter-end=YYYY-MM-DD --iter-duration=days --count=number --repo=orgName/repoName [--authors=author1,author2] [-v]`
- **Options:**
  - Iteration control parameters (`--iter-start`, `--iter-end`, `--iter-duration`).
  - `--count`: Number of iterations.
  - `--repo`: Target GitHub repository.
  - `--authors`: Filter PRs by authors.
  - `-v`: Verbose mode.
- **Example:** `bin/json-aggregator --iter-start=2023-12-05 --iter-end=2023-12-11 --iter-duration=7 --count=4 --repo=myOrg/myRepo`

### ★tsv-aggregator
- **Description:** Converts JSON output from `json-aggregator` to TSV format.
- **Usage:** `tsv-aggregator --iter-start=YYYY-MM-DD --iter-end=YYYY-MM-DD --iter-duration=days --count=number --repo=orgName/repoName [--authors=author1,author2] [-v]`
- **Options:** Similar to `json-aggregator`.
- **Example:** `bin/tsv-aggregator --iter-start=2023-12-05 --iter-end=2023-12-11 --iter-duration=7 --count=4 --repo=myOrg/myRepo > out.tsv`
  - You can paste the result to spreadsheets.

## Misc Scripts

### json-to-tsv.py
- **Description:** Python script for converting JSON data to TSV format.
- **Usage:** `python json-to-tsv.py <json_file>`
- **Details:** Processes JSON data to generate a TSV file suitable for spreadsheets.
- **Example:** `python json-to-tsv.py out.json`
