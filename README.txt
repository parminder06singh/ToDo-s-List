A simple command-line To-Do List Manager built in pure Python (standard library only, no external packages, no database).

This project lets a user manage a personal task list from the terminal: add tasks with a priority level, view them sorted by priority, mark tasks complete, delete tasks, and view a summary report. Data is saved to a plain text file (`tasks.txt`) so tasks persist between runs.

- Add tasks with a title and priority (High / Medium / Low)
- View all tasks, automatically sorted by priority
- Mark a task as complete by ID
- Delete a task by ID
- View a summary report (totals, completed vs. pending, breakdown by priority)
- Input validation (empty titles rejected, invalid priorities default to Medium, invalid IDs handled gracefully)
- Data persists between runs using plain text file storage (no JSON, no database)

- Python 3 (standard library only: `os`)
- `unittest` and `unittest.mock` for testing

```
todo_project/
├── main.py
├── task_manager.py
├── file_handler.py
├── validator.py
├── report.py
├── requirements.txt
├── README.md
├── statement.md
└── tests/
    └── test_task_manager.py
```

1. Make sure Python 3 is installed (`python --version`).
2. Clone or download this repository.
3. No dependencies to install — this project uses only the standard library.
4. From the project root, run:
   ```
   python main.py
   ```
5. Follow the on-screen menu (1–6) to add, view, complete, delete tasks, or view the summary.

Unit tests cover the validation logic and core task operations (adding, completing, deleting), using mocks so tests don't write to the real `tasks.txt` file.

From the project root, run:
```
python -m unittest discover tests
```

- Task data is stored in `tasks.txt`, created automatically on first save.
- See `statement.md` for the problem statement, scope, and target users.