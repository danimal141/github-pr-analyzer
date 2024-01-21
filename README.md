# GitHub PR Analyzer

## Overview

The GitHub PR Analyzer is a command-line tool designed for aggregating and analyzing pull request (PR) data from specified GitHub repositories over a defined time period. It is particularly useful for project maintainers and teams wishing to track PR activity, such as the contribution volume and individual contributor activities.

## Features

- **Period Specification**: Users can define a specific date range for analysis using `--since` and `--until` parameters.
- **PR Count by Author**: Counts the number of PRs submitted by each author within the specified period.
- **Filter by Author**: Allows filtering PRs by specific authors using the `--authors` parameter.
- **Exclude Specific PRs**: Excludes PRs with titles containing keywords like "release" or "リリース".
- **Output Format Selection**: Users can choose between JSON or TSV output formats using the `--output` parameter.
- **Verbose Output**: Provides a more detailed output, including the URL of each PR, for in-depth analysis when using the `-v` flag.

## Prerequisites

- GitHub CLI (`gh`) must be installed and configured on your system. For installation and setup, see the [GitHub CLI documentation](https://cli.github.com/manual/).

## Usage

```sh
./gpa --since=YYYY-MM-DD --until=YYYY-MM-DD --repo=orgName/repoName [--output=json|tsv] [--authors=author1,author2] [-v]
```

### Parameters:

- `--since`: Start date of the period for analysis (inclusive). Format: `YYYY-MM-DD`.
- `--until`: End date of the period for analysis (inclusive). Format: `YYYY-MM-DD`.
- `--repo`: The repository to analyze, in `owner/repo` format.
- `--output` (optional): Specify the output format, either 'json' or 'tsv'. Default is 'json'.
- `--authors` (optional): Comma-separated list of authors to filter the analysis by.
- `-v` (optional): Enables verbose output, listing each PR's URL alongside the count.

### Examples:

- To analyze PRs in the `octocat/Spoon-Knife` repository from March 1, 2023, to March 31, 2023:

  ```sh
  ./gpa --since=2023-03-01 --until=2023-03-31 --repo=octocat/Spoon-Knife
  ```

- To analyze PRs in the `octocat/Spoon-Knife` repository for the same period with verbose output:

  ```sh
  ./gpa --since=2023-03-01 --until=2023-03-31 --repo=octocat/Spoon-Knife -v
  ```

- To analyze PRs in the `octocat/Spoon-Knife` repository from March 1, 2023, to March 31, 2023, filtered by authors 'alice' and 'bob', in TSV format:

  ```sh
  ./gpa --since=2023-03-01 --until=2023-03-31 --repo=octocat/Spoon-Knife --output=tsv --authors=alice,bob
  ```
