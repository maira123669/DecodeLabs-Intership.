# To-Do List Application

def add_task(task_list):
    task = input("Enter a task: ").strip()
    if task:
        task_list.append(task)
        print("Task added!")
    else:
        print("Task cannot be empty!")

def view_tasks(task_list):
    print("\nYour Tasks:")
    if not task_list:
        print("No tasks added yet.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    my_tasks = []

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_task(my_tasks)
        elif choice == "2":
            view_tasks(my_tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# Run the program
if __name__ == "__main__":
    main()