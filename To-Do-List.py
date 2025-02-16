import json

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {"tasks": []}
        save_tasks(tasks)
        return tasks

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Failed to save the Task: {e}")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if not task_list:
        print("No Tasks to View.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(task_list):
            status = "[Complete]" if task["complete"] else "[Pending]"
            print(f"{idx+1}. {task['description']} | {status}")

def add_tasks(tasks):
    description = input("Enter the Task Description: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Description should not be empty.")

def complete_tasks(tasks):
    view_tasks(tasks)
    if not tasks["tasks"]:
        return
    
    try:
        task_number = int(input("Enter the Task number to mark as Complete: ").strip())
        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as Complete.")
        else:
            print("Invalid Task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTO-DO List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Completed Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            complete_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
