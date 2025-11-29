# Future Plan of Action (PoA)

This document outlines the future enhancements and features for the First Contributions repository. This project is currently in Phase 1 (Documentation and Basic Tutorial), and Phase 2 will focus on automation, interactivity, and broader reach.

## Phase 2: Enhancements and Automation

### 1. Automated Validation
- **Goal**: Ensure all contributions follow the project guidelines automatically.
- **Action**: Implement GitHub Actions or pre-commit hooks to:
  - Validate the format of `Contributors.md` (e.g., ensure new lines are added correctly).
  - Check filename conventions for new translations (using `scripts/validate_filenames.py`).
  - Lint Markdown files for syntax errors and broken links.

### 2. Interactive CLI Tool
- **Goal**: Provide a guided experience for users who prefer the terminal but need more hand-holding.
- **Action**: Develop a CLI tool (e.g., `first-contributions-cli`) that walks the user through the steps:
  - Cloning the repo.
  - Creating a branch.
  - Editing the file.
  - Pushing changes.

### 3. Website Integration
- **Goal**: Make the tutorial more accessible and interactive on the web.
- **Action**:
  - Enhance the current GitHub Pages site.
  - Add an interactive "playground" where users can simulate git commands without needing to install git locally initially.

### 4. Expanded GUI Tutorials
- **Goal**: Cover more Git clients.
- **Action**: Add tutorials for:
  - GitKraken (Updated versions)
  - Sublime Merge
  - Tower
  - TortoiseGit

### 5. Community Engagement
- **Goal**: Foster a more active community.
- **Action**:
  - Create a Discord or Slack channel for real-time help.
  - Host "First Contribution" workshops or webinars.

## Phase 3: Long-term Vision

- **Gamification**: badges and achievements for helping other first-time contributors.
- **Localization**: Automate the translation process using tools like Crowdin to keep all language versions in sync.
