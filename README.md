# DevSecOps Secret Scanner (Pre-Commit Hook)

An automated security tool built in Python that integrates directly into the Git lifecycle to prevent developers from accidentally committing hardcoded secrets, API keys, and credentials to version control.

## Architecture & Features
* **Automated Interception:** Runs as a local Git `pre-commit` hook, scanning all staged files before a commit is allowed to proceed.
* **Regex Threat Detection:** Utilizes the Python `re` module to identify high-risk strings, including AWS Access Keys and RSA Private Keys.
* **Fail-Secure Design:** If a secret is detected, the script exits with a non-zero status code, actively blocking the git commit and outputting the file and line number for remediation.
* **Continuous Integration:** Fully integrated with GitHub Actions to automatically run `pytest` unit tests on every push and pull request.

## How It Works
When a developer attempts to run `git commit`, the bash hook triggers the Python CLI module, passing in the currently staged files. The scanner reads the files line-by-line against a dictionary of threat patterns.

```bash
# Example Output of a Blocked Commit
[!] CRITICAL: Secrets detected in source code!
  -> app/config.py:12 - [AWS Access Key]
Git Hook: Commit blocked due to exposed secrets!