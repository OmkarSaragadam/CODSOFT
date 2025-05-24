import json
import os

FILE_NAME = "todo_list.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

def add_task(tasks):
    task_text = input("Enter task: ")
    tasks.append({"task": task_text, "completed": False})

def mark_task_done(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
