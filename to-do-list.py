tasks =[]
def show_tasks():
   print("\n")
   if tasks == []:
       print("You haven't added any task yet.")
       return False
   else:
     for task in tasks:
        print(f"{task['task_id']}) {task['Title']} ({task['Status']})")
   return True
  
def add_task(task_id):
    Title = input("\nEnter your task or 'q' to quit: ")
    if Title.lower() == 'q':
      return False
    while True:
      done_input=input("Is it done(Y/N): ")
      if done_input.upper() == 'Y':
          status= "Completed"
          break
      elif done_input.upper()=='N':
          status = "Not Completed"
          break
      else:
           print("Wrong input. Type only Y or N")
    tasks.append({"task_id": task_id , "Title": Title, "Status": status})

    return True
    
     
def remove_tasks():
    while True:
      try:
          delete_id=int(input("\nEnter the delete ID: "))
          if delete_id<=0:
             print("Please Enter a Positive Number")
             continue
          break
      except ValueError:
            print("Please Enter a Valid Number: ")

    for i, task in enumerate(tasks):
      if (task["task_id"]==delete_id):
         tasks.pop(i)
         print(f"\nTask number {task['task_id']} removed successfully")  
         return True 
    return False
      
       
def edit_tasks(edit_id):
     keys = input("\nWhat to change Title or Status or Both??(Select T / S/ B): ")     
     for task in tasks:
       if task["task_id"] == edit_id:
          if keys.upper()=='T':
               new_title= input("Enter a new task: ")
               task["Title"] = new_title
          elif keys.upper()=='S':
              status= input("Update(Is it done(Y/N)? ) ")
              if status.upper() =='Y':
                   task["Status"] = "Completed"
              elif status.upper() =='N':
                   task["Status"] = "Not Completed"
          elif keys.upper()=='B':
                new_title= input("Enter a new task: ")
                task["Title"] = new_title
                status= input("Update(Is it done(Y/N)? ) ")
                if status.upper() =='Y':
                  task["Status"] = "Completed"
                elif status.upper() =='N':
                   task["Status"] = "Not Completed"
          else:
             return False
          return True
     return False

      


def main():
    task_id =1
    while True:
      print("\nSelect one of the following: ")
      a = int(input("1) Add Task\n2) Remove task\n3) Edit Task\n4) Show TODO LIST\n \n"))
      match a:
        case 1:
         while True:
           add = add_task(task_id)
           if add:
              show_tasks()
              task_id+=1
              more_task= input("\nDo you want to add more tasks or not?(Y/N): ")
              if more_task.upper()!='Y':
                 break
           else:
            break
        case 2:
         while True:
           print("\t")
           if show_tasks()==False:
              break
           remove = remove_tasks()
           if remove:
             more_remove=input("\nDo you want to remove more task? Press(Y/N): ")
             if more_remove.upper()!='Y':
                break
           else:
             print("\nNo Task ID Founded")
             break

        case 3:
          while True:
             show_tasks()
             print("\n")
             edit_id = int(input("Select which task to edit: Enter the task number: "))
             edited = edit_tasks(edit_id)
             if edited:
                show_tasks()
                more_edit=input("\nDo you want to edit more task? Press(Y/N): ")
                if more_edit.upper() !='Y':
                   break
             else:
                print("\nTask Number not Found")
                break
        case 4: 
          print("\t")
          show_tasks()
        case _:
            break


main()






    

