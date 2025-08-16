import json
from datetime import datetime

DATA_FILE = "my_tasks.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(task_list):
    with open(DATA_FILE, "w") as file:
        json.dump(task_list, file, indent=2)

def show_tasks(task_list):
    if not task_list:
        print("\n📭 No tasks yet!\n")
        return
    print("\n🗂️ Your Tasks:")
    for idx, task in enumerate(task_list, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{idx}. {task['task']} (Due: {task['due']}) [{status}]")
    print()

def add_task(task_list):
    title = input("📝 Task name: ").strip()
    due = input("📅 Due date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(due, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("⚠️ Invalid date format. Try again.")
        return
    task_list.append({"task": title, "due": due, "done": False})
    save_data(task_list)
    print("✅ Task added!\n")

def mark_done(task_list):
    show_tasks(task_list)
    try:
        index = int(input("🔢 Task number to mark done: ")) - 1
        task_list[index]["done"] = True
        save_data(task_list)
        print("🎉 Task marked as complete!\n")
    except (IndexError, ValueError):
        print("⚠️ Invalid selection.\n")

def remove_task(task_list):
    show_tasks(task_list)
    try:
        index = int(input("🗑️ Task number to delete: ")) - 1
        removed = task_list.pop(index)
        save_data(task_list)
        print(f"🧹 Removed: {removed['task']}\n")
    except (IndexError, ValueError):
        print("⚠️ Invalid selection.\n")

def main():
    tasks = load_data()
    while True:
        print("📌 Menu:\n1. View Tasks\n2. Add Task\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❓ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()