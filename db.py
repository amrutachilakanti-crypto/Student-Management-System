import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amruta@2004",
        database="student_db"
    
    )
    return connection