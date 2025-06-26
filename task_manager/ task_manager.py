def show_menu():
    print("Task Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit") 


tasks = []

def task_manager():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
            print("Task added.")

        elif choice == '2':
            if not tasks:
                print("No tasks found.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif choice == '3':
            num = int(input("Enter task number to delete: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

task_manager()
