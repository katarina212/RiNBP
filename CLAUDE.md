# CLAUDE.md - Codebase Guidelines

## Repository Purpose
This repository contains educational materials for database courses, focusing on relational and NoSQL databases.

## Python Guidelines
- Use `snake_case` for variables/functions, `PascalCase` for classes
- Import order: stdlib, third-party, local modules (with blank line separators)
- Error handling: use try/except blocks with specific exception types
- Type hints preferred for function parameters and return values
- Generate visualization images: `python lectures/03/generate_nosql_images.py`

## Markdown Presentation Guidelines
- Use Marp for slideshows (frontmatter: `marp: true`)
- Separate slides with `---` on a separate line
- Include proper frontmatter: theme, title, pagination
- Use consistent header levels throughout presentations
- Structure: title slide → agenda/overview → content → summary/questions

## Code Style & Documentation
- Document functions with docstrings explaining purpose and parameters
- Keep functions focused (< 30 lines) and descriptive naming
- Add context explaining the "why" behind code decisions
- Matplotlib visualizations: use consistent styling, proper labels, and readable fonts

## Commit Guidelines
- Format: `<type>(<scope>): <short summary>`
- Types: feat, fix, docs, style, refactor, test, chore
- Describe what changed and why in commit messages