tasks = []

while True:
    print("\n------TO DO LIST MENU---------")
    print("1. Add Task")
    print("2. Mark Task As Completed")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task":task, "completed":False})
        print("\nTask Added successfully.")

    elif choice == "2":
        print("-------Tasks-------")
        for i, task in enumerate(tasks):
            print(f"{i+1}.[{task['completed']}] {task['task']}")


        task_index = int(input("Enter the index of task to mark as compelted: "))
        if task_index > 0 and task_index < len(tasks):
            tasks[task_index - 1]["completed"] = True
            print("\nTask Mark as compelted")
        else:
            print("Invalid task index.")

    elif choice == "3":
        print("\n---------Tasks---------")

        for i,task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i+1}. {task['task']} [{status}]")

    elif choice == "4":
        print("-------Exiting Program------")
        break

    else:
        print("Invalid choice. Please try again !!")