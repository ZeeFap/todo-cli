import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
    except (json.JSONDecodeError, OSError):
        pass
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet ✅\n")
        return
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['title']}")
    print()


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Empty title. Task not added.\n")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added ✅\n")


def toggle_task(tasks):
    if not tasks:
        print("No tasks to update.\n")
        return
    try:
        idx = int(input("Task number to toggle: "))
        if idx < 1 or idx > len(tasks):
            print("Wrong number.\n")
            return
        tasks[idx - 1]["done"] = not tasks[idx - 1]["done"]
        save_tasks(tasks)
        print("Task updated 🔁\n")
    except ValueError:
        print("Please enter a number.\n")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.\n")
        return
    try:
        idx = int(input("Task number to delete: "))
        if idx < 1 or idx > len(tasks):
            print("Wrong number.\n")
            return
        removed = tasks.pop(idx - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']} 🗑️\n")
    except ValueError:
        print("Please enter a number.\n")


def menu():
    tasks = load_tasks()
    while True:
        print("=== To-Do CLI ===")
        print("1) Show tasks")
        print("2) Add task")
        print("3) Toggle done/undone")
        print("4) Delete task")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            toggle_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "0":
            print("Bye! 👋")
            break
        else:
            print("Unknown option.\n")


if __name__ == "__main__":
    menu()
