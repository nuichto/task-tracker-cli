# 🗂️ Task Tracker CLI

A simple but solid command-line task tracker built in Python. Lets you add, update, delete tasks and track their status — no databases, no frameworks, just Python's built-in modules.

## ✨ Features

- ➕ Add new tasks
- ✏️ Edit task descriptions
- 🗑️ Delete tasks
- 🔄 Change task status (`todo` → `in-progress` → `done`)
- 📋 View all tasks or filter by status
- 💾 Data stored in a JSON file (persists between runs)

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

Only Python 3 is required — no external libraries needed.

## 📖 Usage

```bash
# Add a task
python task_cli.py add "Buy groceries"
# Task added successfully (ID: 1)

# Update a task's description
python task_cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task_cli.py delete 1

# Mark a task as in progress / done
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1

# List all tasks
python task_cli.py list

# List tasks by status
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

## 🖼️ Example

```
$ python task_cli.py add "Learn Python"
Task added successfully (ID: 1)

$ python task_cli.py list
Tasks:
[1] Learn Python | Status: todo | Created: 2026-09-21 14:32:01
```

*(add your own terminal screenshot or GIF here — see the publishing guide for how)*

## 🗃️ Data structure

Each task is stored in `tasks.json` in the following format:

```json
{
  "id": 1,
  "description": "Learn Python",
  "status": "todo",
  "createdAt": "2026-09-21 14:32:01",
  "updatedAt": "2026-09-21 14:32:01"
}
```

## 🛠️ Built with

- Python 3
- Built-in modules: `json`, `sys`, `os`, `datetime`
- No external libraries or frameworks (per project requirements)

## 📌 About

A learning pet-project built from the [roadmap.sh](https://roadmap.sh/projects/task-tracker) task tracker project spec — practicing file system operations, JSON, user input handling, and CLI arguments in Python.

## 📄 License

MIT
