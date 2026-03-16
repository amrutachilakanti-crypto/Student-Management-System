def insert_student_query():
    return "INSERT INTO students (name,email,age) VALUE (%s,%s,%s)"

def get_student_query():
    return "SELECT * FROM students"

def update_student_query():
    return "UPDATE students SET email=%s WHERE id=%s"

def delect_student_query():
    return "DELETE FROM students WHERE id=%s"