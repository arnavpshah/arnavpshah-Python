todo_tasks = []
completed_tasks = []

def Todo_list():
    exit_loop = True
    while (exit_loop):
        choice = str(input("Type a, r, p, q, or c. a to add, r to remove, p to print, q to quit or c to complete\n"))
        if (choice == "a"):
            add_task = str(input("Type a task to add\n"))
            todo_tasks.append(add_task)
        elif (choice == "r"):
            remove_task = str(input("Type the task and we will remove it\n"))
            for task in todo_tasks:
                if (task == remove_task):
                    todo_tasks.remove(remove_task)
        elif (choice == "p"):
            print("Todo list:", todo_tasks)
            print("Completed list:", completed_tasks)
        elif (choice == "q"):
            print("Exiting from app")
            exit_loop = False
        elif (choice == "c"):
            finished_task = str(input("Which one is a completed task\n"))
            for task in todo_tasks:
                if (task == finished_task):
                    todo_tasks.remove(finished_task)
                    completed_tasks.append(finished_task)
        else:
                print("That is not a valid input")
    
Todo_list()
