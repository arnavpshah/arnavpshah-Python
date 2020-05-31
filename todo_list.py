
todo_tasks = []

def Todo_list():
    exit_loop = True
    while (exit_loop):
        choice = str(input("Type a, r, p, q, or c. a to add, r to remove, p to print, q to quit or c to complete\n"))
        if (choice == "a"):
            task = str(input("Type task to add\n"))
            todo_tasks.append(task)
        elif (choice == "r"):
            print("Remove task")
        elif (choice == "p"):
            print(todo_tasks)
        elif (choice == "q"):
            print("Exiting from app")
            exit_loop = False
        elif (choice == "c"):
            completed_tasks = str(input("Which one is a completed task\n"))
            print(completed_tasks , "- Completed")
        else:
                print("That is not a valid input")
    
Todo_list()
