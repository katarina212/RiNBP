# RiNBP - Raspodijeljene i Nerelacijske Baze Podataka

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Course materials for "Distributed and Non-Relational Databases" / "Raspodijeljene i Nerelacijske Baze Podataka" (2024/2025).

## 📚 Course Overview

This repository contains lecture materials, examples, and project ideas for the database systems course covering:

- Relational database advanced topics
- NoSQL database systems (Document, Key-Value, Column-Family, Graph)
- Modern analytical databases (DuckDB)
- Vector databases and AI integration
- Distributed database architectures
- Data modeling techniques
- Transaction processing
- Retrieval Augmented Generation (RAG)

## 🗂️ Repository Structure

- **`/lectures`**: Markdown-based lecture slides organized by week
  - Uses [Marp](https://github.com/marp-team/marp) for presentation format
  - Complete lecture series from 00-12 covering all database types
    - 00-04: Core concepts and SQL programming
    - 05-06: MongoDB and distributed databases
    - 07-12: NoSQL types (fundamentals, key-value, column-family, graph, document, vector)
- **`/assets`**: Images and diagrams used in lecture materials
- **`/materials`**: Sample databases and exercise files
- **`/projects`**: Git submodules linking to individual student project repositories

## 🎓 Project Ideas

Students are encouraged to explore the [project ideas](project-ideas.md) document to select or propose a course project. Projects can be completed individually or in small teams.

## 📋 Student Projects

View all current student projects in the [STUDENT-PROJECTS.md](STUDENT-PROJECTS.md) file. For information on how to update your project details, see the [CONTRIBUTING.md](CONTRIBUTING.md) guide.

## 🔄 Student Project Repositories

Student projects are included as Git submodules. This allows each student/team to maintain their own repository while keeping all projects accessible through this main repository.

### Cloning this repository

To clone this repository with all student projects:
```
git clone --recursive https://github.com/nkkko/rinbp
```

If you've already cloned without `--recursive`:
```
git submodule update --init --recursive
```

To update all student projects to their latest versions:
```
git submodule update --remote
```

### Adding new student projects

For instructors, to add a new student project repository:
```
git submodule add [REPO_URL] projects/[PROJECT_NAME]
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍🏫 Author

Nikola Balić
Email: nikola.balic@gmail.com
GitHub: [@nkkko](https://github.com/nkkko)