from config.db import get_connection
from models.student_model import *

def create_student(name,email,age):
    
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(insert_student_query(),(name,email,age))

    conn.commit()
    conn.close()

    print("Student Added Succesfully")

def get_student():

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(get_student_query())

    students = cursor.fetchall()

    for s in students:
        print("ID:",s[0],"name:",s[1],"Email:",s[2],"Age:",s[3])

        conn.close()

def update_student(id,email):

    conn = get_connection()
    cursor =conn.cursor()

    cursor.execute(update_student_query(),(email,id))

    conn.commit()
    conn.close()

    print("Student Update Successfully")


def delete_student(id):

   conn = get_connection()
   cursor = conn.cursor()

   cursor.execute(delect_student_query(),(id,))

   conn.commit()
   conn.close()

   print("student delected successfully")
