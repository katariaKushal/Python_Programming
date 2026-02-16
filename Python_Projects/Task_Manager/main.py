from manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n📝 TASK MANAGER")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Toggle Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            title = input("Title: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            manager.add_task(title, deadline, priority)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.view_tasks()
            index = int(input("Task index: "))
            manager.toggle_complete(index)
        elif choice == '4':
            manager.view_tasks()
            index = int(input("Task index: "))
            manager.delete_task(index)
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
