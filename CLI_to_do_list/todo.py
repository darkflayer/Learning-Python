import os

todo_file="todo_list.txt"

#function to load task
def load_task():
    if not os.path.exists(todo_file):  #here checking the file exist or not
        return []   # return an empty list
    
    with open(todo_file,"r") as file:
        return [line.strip() for line in file.readlines()]   #read all lines and strip() removes extra space


#function to save task
def save_tasks(tasks):
    with open(todo_file,"w") as file:
        file.writelines(task +"\n" for task in tasks) #writing each task on new line


#function to show task
def show_task():
    tasks=load_task()  #get the list of tasks
    if not tasks:   #if the list is empty
        print("No Tasks yet! Add some.")
    else:
        print("\n📋 To-Do List:")
        for i,task in enumerate(tasks,start=1): #loop through tasks with i starting from 1
            print(f"{i}.{task}") #print index(task number) with task
         
# function to add a new task   
def add_task():
    task=input("Enter a new task: ") #asking user for a new task
    tasks=load_task() #here we are laoding existing tasks
    tasks.append(task) #add new task to the list
    save_tasks(tasks)
    print("Task added!")


#function to remove a task
def remove_task():
    show_task() #show all current tasks
    tasks=load_task() #load tasks
    
    try:
        task_num=int(input("Enter task number to remove:"))
        if 1<=task_num<=len(tasks): #ensure the task number is valid
            tasks.pop(task_num-1)  #removing the task(index start from 0)
            save_tasks(tasks)  #now saving the updated task
            print("Task removed!")
        else:
            print("⚠️Invalid task number.") #if enterd task number is out of range
    except ValueError:
        print("⚠️Please enter a valid number")
        
#the main menu to run the program

def main():
    while True:
        print("\n=== 📝 To-Do List CLI-App ===")
        print("1. Show Tasks")
        print("2. Add Tasks")
        print("3. Remove Tasks")
        print("4. Exit")
        
        choice=int(input("Choose an option:"))
        
        if(choice==1):
            show_task()
        elif(choice==2):
            add_task()
        elif(choice==3):
            remove_task()
        elif(choice==4):
            print("👋 Exiting... Have a productive day!")
            break
        else:
             print("⚠️ Invalid choice! Try again.") #if there is invalid choice entered by us

#ensures that script run only when script runs directly or from main
if __name__=="__main__":
    main()