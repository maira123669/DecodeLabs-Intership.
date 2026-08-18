# DecodeLabs Python Mini-Projects 🐍

A collection of three beginner-friendly Python command-line applications:

1. [To-Do List Application](#-to-do-list-application)
2. [Expense Tracker](#-expense-tracker)
3. [Random Password Generator](#-random-password-generator)

---

## 📋 To-Do List Application

A simple console-based to-do list manager that lets you add and view tasks during a session.

### Features
- ➕ Add new tasks
- 📄 View all tasks in a numbered list
- ⚠️ Prevents adding empty tasks
- 🔁 Runs in a loop until you choose to exit

### How to Run
```bash
python todo_list.py
```

### Usage
```
1. Add Task
2. View Tasks
3. Exit
Choose an option (1-3):
```

---

## 💰 Expense Tracker

A command-line tool to track your expenses and keep a running total.

### Features
- 💵 Add expense amounts one at a time
- 📊 Displays a running total after each entry
- 🚫 Rejects negative or invalid input
- 🛑 Type `quit`, `exit`, `done`, or `stop` to finish and see your final total

### How to Run
```bash
python expense_tracker.py
```

### Usage
```
==========================================
      DECODELABS EXPENSE TRACKER          
==========================================
Enter expense amounts. Type 'quit' to exit.

Enter expense ($) or 'quit': 25.50
[+] Added: $25.50 | Current Total: $25.50
```

---

## 🔐 Random Password Generator

A secure password generator using Python's `secrets` module for cryptographically strong randomness.

### Features
- 🔒 Uses `secrets.choice()` instead of `random` for security
- 🔤 Combines uppercase, lowercase, digits, and special characters
- ✅ Validates that the requested length is a positive number

### How to Run
```bash
python password_generator.py
```

### Usage
```
--- DecodeLabs Random Password Generator ---
Enter desired password length: 12

Generated Secure Password: xK9$mP2#nQ7!
```

---

## 🛠️ Requirements

- Python 3.6+
- No external dependencies — uses only the Python standard library (`string`, `secrets`)

## 📁 Project Structure
```
.
├── todo_list.py
├── expense_tracker.py
├── password_generator.py
└── README.md
```

## 🤝 Contributing

Feel free to fork this repo, suggest improvements, or add new mini-projects to the collection.

## 📄 License

This project is open source and available for personal and educational use.
