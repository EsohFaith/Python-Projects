tasks = []
def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as Done")
    print ("4. Delete task")
    print("5. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "Done": False})
    print (f"Task '{task}' added successfully.")
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print ("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["Done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")
def mark_task_done():
    view_tasks()
    if not tasks:
        return
    try:
     task_number = int(input("Enter the task number to mark as Done: "))
     if 1 <= task_number <= len(tasks):
          tasks[task_number - 1]["Done"] = True
          print(f"Task '{tasks[task_number - 1]['task']}' marked as Done.")
     else:
         print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting the To-do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
