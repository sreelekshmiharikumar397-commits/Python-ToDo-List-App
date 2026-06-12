tasks = []

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(" Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print(" No tasks available.")
        else:
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print(" No tasks to delete.")
        else:
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f" '{removed_task}' deleted successfully!")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print(" Please enter a valid number.")

    elif choice == "4":
        print(" Thank you for using the To-Do List App!")
        break

    else:
        print(" Invalid choice. Please enter 1, 2, 3, or 4.")