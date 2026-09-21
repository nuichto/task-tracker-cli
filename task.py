import sys
import json
import os
from datetime import datetime

FILE_PATH = 'tasks.json'


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def add_task(description):
    tasks = load_tasks()

    new_id = max([task['id'] for task in tasks], default=0) + 1
    now = get_current_time()

    new_task = {
        'id': new_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f'Task added successfully (ID: {new_id})')


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = get_current_time()
            save_tasks(tasks)
            print(f'Task {task_id} updated successfully!')
            return
    print(f'Error: Task with ID {task_id} not found.')


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t['id'] != task_id]

    if len(tasks) == len(updated_tasks):
        print(f'Error: Task with ID {task_id} not found.')
        return

    deleted_task = next(t for t in tasks if t['id'] == task_id)
    save_tasks(updated_tasks)
    print(f'Task "{deleted_task["description"]}" deleted!')


def mark_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = get_current_time()
            save_tasks(tasks)
            print(f'Task {task_id} marked as {status}.')
            return
    print(f'Error: Task with ID {task_id} not found.')


def list_tasks(status_filter=None):
    tasks = load_tasks()
    
    if status_filter:
        tasks = [t for t in tasks if t['status'] == status_filter]

    if not tasks:
        print('No tasks found.')
        return

    print('\nTasks:')
    for task in tasks:
        print(f"[{task['id']}] {task['description']} | Status: {task['status']} | Created: {task['createdAt']}")


def main():
    args = sys.argv[1:]

    if not args:
        print("Usage: python task.py <command> [arguments]")
        return

    command = args[0].lower()

    if command == 'add' and len(args) > 1:
        add_task(args[1])

    elif command == 'update' and len(args) > 2:
        try:
            update_task(int(args[1]), args[2])
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'delete' and len(args) > 1:
        try:
            delete_task(int(args[1]))
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'mark-in-progress' and len(args) > 1:
        try:
            mark_status(int(args[1]), 'in-progress')
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'mark-done' and len(args) > 1:
        try:
            mark_status(int(args[1]), 'done')
        except ValueError:
            print("Error: Task ID must be an integer.")

    elif command == 'list':
        status = args[1] if len(args) > 1 else None
        list_tasks(status)

    else:
        print("Invalid command or missing arguments.")


if __name__ == '__main__':
    main()