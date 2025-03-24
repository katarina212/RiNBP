# CLAUDE.md - Codebase Guidelines

## Repository Purpose
This repository contains educational materials for database courses, including:
- Relational database lectures (`relacijske-intro.md`)
- NoSQL database lectures (`nosql-1.md`, `nosql-2.md`)
- Database examples and assets

## Markdown Presentation Guidelines
- Use Marp for slideshows (frontmatter: `marp: true`)
- Separate slides with `---` on a separate line
- Include proper frontmatter with theme, title, and pagination
- Use consistent header levels throughout presentations
- Keep content focused with concise bullet points

## Python/Jupyter Guidelines (When Applicable)
- Keep notebook cells focused on single tasks (20-25 lines max)
- Use snake_case for variables/functions, PascalCase for classes
- Include markdown documentation explaining the purpose of code
- Document the "why" behind code decisions, not just the "what"
- Begin notebooks with title, overview, and author information

## Commit Guidelines
- Follow conventional commit format: `<type>(<scope>): <short summary>`
- Types: feat, fix, docs, style, refactor, test, chore, etc.
- Include detailed descriptions of what was changed
- Explain why changes were made in commit messages