from services.student_service import *

while True :
    print("\n===== Student CRUD Menu =====")
    print("1.Add Student")
    print("2.View Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit")

    choice =int(input("Enter choice:"))

    if choice == 1:

        name = input("Enter Name:")
        email = input("Enter Email:")
        age = int(input("Enter Age:"))

        create_student(name,email,age)

    elif choice == 2:
     
     get_student()

    elif choice == 3:

       id = int(input("Enter Student ID:"))
       email = input("Enter New Email:")
      

       update_student(id,email) 

    elif choice == 4:

       id = int(input("Enter Student ID to delete:"))
       delete_student(id)


    elif choice == 5:
       print("Exinting program")   

       break

    else:
       print("Invalid choice")    
