import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: could not read tasks file. Starting with an empty list.")
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task description: ").strip()
    if not title:
        print("Task cannot be empty.\n")
        return

    priority = input("Priority (High/Medium/Low) ").strip().capitalize()
    if priority not in ("High", "Medium", "Low"):
        priority = "Medium"

    new_id = (max([t["id"] for t in tasks]) + 1) if tasks else 1
    tasks.append({
        "id": new_id,
        "title": title,
        "priority": priority,
        "done": False
    })
    save_tasks(tasks)
    print(f"Task added (ID: {new_id}).\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.\n")
        return

    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    sorted_tasks = sorted(tasks, key=lambda t: priority_order.get(t["priority"], 1))

    print("\n--- Your Tasks ---")
    for t in sorted_tasks:
        status = "✔ Done" if t["done"] else "✗ Pending"
        print(f"[{t['id']}] ({t['priority']}) {t['title']} - {status}")
    print()

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to mark complete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as complete.\n")
            return
    print("Task ID not found.\n")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID.\n")
        return

    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            save_tasks(tasks)
            print(f"Task {task_id} deleted.\n")
            return
    print("Task ID not found.\n")

def show_menu():
    print("===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.\n")

if __name__ == "__main__":
    main()
