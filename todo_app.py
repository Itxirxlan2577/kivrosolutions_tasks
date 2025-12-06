tasks = []  # This list will store our to‑do tasks

while True:
    print("\n==== TO‑DO LIST ====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nSelect the number of the task to delete:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            try:
                idx = int(input("Task number to delete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select 1, 2, 3, or 4.")
