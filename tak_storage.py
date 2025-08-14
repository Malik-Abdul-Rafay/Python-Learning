task = []

while True:
    print("""
    Menu:
    a) Add Task
    b) View Task
    c) Delete Task
    d) Exit
    """)

    choice = input("Enter Your Choice: ")

    if(choice.lower() == "a"):
        task_name = input("Enter Your Task: ")
        task.append(task_name)
        print("Task Added")

        
    elif(choice == "b"):
        if not task:
            print("Task Not Found")
        else:
            print(task)
    elif(choice == "c"):
        if not task:
            print("Task Not Found")
        else:
            delete_task_name = input("Enter Delete Task Name: ")
            found = False
            for task_ in task:
                if(delete_task_name.lower() == task_.lower()):
                    task.remove(task_)
                    print("Task Deleted Successfully")
                    found =  True
            if not found:
                print("This Task Not Found")

                    
    elif(choice == "d"):
        break

    else:
        print("Your chice is not correct")

