
Task Manager App
Overview
The Task Manager App is a simple command-line application that allows users to manage
tasks, including adding, updating, deleting, and listing tasks. Tasks are stored in a JSON file,
where they can be categorized by their status as "todo," "in-progress," or "done."
Features
-Add New Task: Create a new task with a title and an initial "todo" status.
- Update Task: Modify an existing task's title or status.
- Delete Task: Remove a specific task from the list.
- List Tasks: Display tasks by category (all, completed, not done, in progress).
- Data Persistence: Tasks are saved to a `data.json` file, which persists between sessions.
Getting Started
Prerequisites
- Python 3.x installed on your machine
Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/task-manager-app.git
   cd task-manager-app
   ```
2. No additional dependencies are needed; just run the Python script directly.
Usage
Run the application with:
```bash
python task_manager.py
```
Once started, the app presents a menu where you can choose from the following options:
1. Add a New Task: Add a new task by entering its title.
2. Update a Task: Choose a task to update by entering its ID and specify whether to change
the title, status, or both.
3. Delete a Task: Select a task to delete from the list.
4. List Tasks: View tasks by status categories (all, done, Here’s a README for your task
manager project:
---
Task Manager App
BOverview
The Task Manager App is a simple command-line application that allows users to manage
tasks, including adding, updating, deleting, and listing tasks. Tasks are stored in a JSON file,
where they can be categorized by their status as "todo," "in-progress," or "done."
Features
- Add New Task: Create a new task with a title and an initial "todo" status.
- Update Task: Modify an existing task's title or status.
- Delete Task: Remove a specific task from the list.
- List Tasks: Display tasks by category (all, completed, not done, in progress).
- Data Persistence: Tasks are saved to a `data.json` file, which persists between sessions.
Getting Started
Prerequisites
- Python 3.x installed on your machine
Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/task-manager-app.git
   cd task-manager-app
   ```
2. No additional dependencies are needed; just run the Python script directly.
Usage
Run the application with:
```bash
python task_manager.py
```
Once started, the app presents a menu where you can choose from the following options:
1. Add a New Task: Add a new task by entering its title.
2. Update a Task: Choose a task to update by entering its ID and specify whether to change
the title, status, or both.
3. Delete a Task: Select a task to delete from the list.
4. List Tasks: View tasks by status categories (all, done, todo, in progress).
5. Exit: Close the application.
Example
```plaintext
Task Manager App
Whats on your mind today?
1. Add a new task
2. Update a task
3. Delete a task
4. List my tasks
5. Exit
```
JSON File Structure
Tasks are stored in `data.json` with a structure like this:
```json
{
"1": {
"title": "Complete project report",
"createdAt": "2024-11-13 at 14:00",
"updatedAt": "2024-11-13 at 14:30",
"status": "todo"
},
"2": {
"title": "Review code",
"createdAt": "2024-11-13 at 15:00",
"updatedAt": "2024-11-13 at 15:10",
"status": "done"
}
}
```
License
This project is open source and available under the MIT License.
Contact
For questions or suggestions, feel free to reach out to me at [kobbygilbert233@gmail.com].
Project Page: [GitHub Repository ] (https://github.com/Kobby24/task_manager-)
