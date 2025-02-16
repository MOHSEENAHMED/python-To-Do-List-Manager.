The To-Do List Manager is a simple command-line application that allows users to manage their daily tasks. 

The program enables users to view, add, and mark tasks as complete, while ensuring that tasks are saved persistently using a JSON file.


Features
1. View all tasks – Displays a list of tasks with their status ([Complete] or [Pending]).
2. Add new tasks – Allows users to add tasks with a description.
3. Mark tasks as complete – Updates a task’s status to [Complete].
4. Persistent storage – Tasks are stored in a JSON file, so they remain even after restarting the program.
5. User-friendly CLI – Simple command-line interface for easy task management.

How the code works
1. The script loads tasks from todo_list.json when it starts.
2. The user selects an option from the menu.
3. If the user adds or completes a task, it is saved back to todo_list.json.
4. The program runs in a loop until the user chooses to exit.
