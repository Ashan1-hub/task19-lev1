
#=====importing libraries===========
'''This is the section where you will import your selected libraries''' 
from datetime import datetime


# This is the login section of the program.
# This is reading the file and adding the username and password to a list.

username_list = []
password_list = []
with open("user.txt", "r") as read_user:
    for line in read_user:
        line = line.replace("\n", "").split(", ")
        file_username = line[0]
        file_password = line[-1]
        username_list.append(file_username)
        password_list.append(file_password)
user_name = None
while True:
    user_name = input("Username: ")

    if not user_name in username_list:
        print("incorrect user")
        continue

    password_index = username_list.index(user_name)
    correct_password = password_list[password_index]

    user_password = input("Password: ")

    if user_password != correct_password:
        print("incorrect password")
        continue

    break
    
while True:

# This is the code that is asking the user to enter a new username and password.
    if user_name == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
ds - display stats
:''').lower()
    else:
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
:''').lower()


 # The below code is asking the user to enter a new username and password.
    if menu == 'r':
        print("Here")
        if user_name == 'admin':
            user_name =input("please enter new user name:").lower()
            new_user_password = input("please enter user password :").lower()         
            confirm_user_password = input("please confirm new password.password must be the same as first password:").lower()          
            if new_user_password == confirm_user_password :
                with open("user.txt", "a+") as user_file:
                    user_file.write(f"\n{user_name}, {new_user_password}")
                    print("welcome")
                    print("Username has been added to registry!")
            else:
                print("incorrect password")
        else:
            print('Sorry only admin can Register')            
                
    # This is the code that is adding the task to the file.
    elif menu == 'a':

        assigned_user = input("please enter name of person task assigned:\n")
        task_title = input("please enter the title of the task:\n")
        task_description = input("A description of the task:\n")
        due_date = input("enter date due :\n")
        current_date = datetime.today()
        current_date = current_date.strftime("%d %b %Y")
        task_complete = "NO"
        with open("tasks.txt","a+") as file:
            file.write(f"\n{assigned_user}, {task_title}, {task_description}, {due_date}, {current_date}, {task_complete}")
            
# This is reading the file and printing the data in the file.

    elif menu == 'va':
        
        in_files  = open("tasks.txt","r")
        for line in in_files:
            datalist = line.split(", ")
            print("Task:\t"+ datalist[1])
            print("Assigned to:\t" + datalist[0])
            print("date assinged:\t" + datalist[3])
            print("due date:\t" + datalist[4])
            print("task complete:\t" + datalist[5])
            print("task description:\t")
            print(datalist[2])

   # The above code is reading the file and printing the data in the file.
    elif menu == 'vm':
        with open ('tasks.txt','r+') as file :
            for line in file :
                datalist = line.split(", ")
                if user_name == datalist[0]:
                    print(line)
                    print("Task:\t"+ datalist[1])
                    print("Assigned to:\t" + datalist[0])
                    print("date assinged:\t" + datalist[3])
                    print("due date:\t" + datalist[4])
                    print("task complete:\t" + datalist[5])
                    print("task description:\t")
                    print(datalist[2])
                    
                    # This is the code that is counting the number of tasks and
                    # users in the file.
                
    elif menu =='ds' and user_name == 'admin':
        task_num =0
        user_num = 0
        with open ('tasks.txt', 'r') as task_file :
            for line in task_file:
                task_num +=1
            print(f'\ntotal number of tasks :{task_num}') 

        with open ('user.txt', 'r') as user_file :
            for line in user_file :
                user_num +=1
            print(f'\ntotal number of users : {user_num}')

    # This is the code that is asking the user to enter a new username and password.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")