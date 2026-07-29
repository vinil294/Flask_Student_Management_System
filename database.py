import sqlite3
import os
os.makedirs("Database", exist_ok=True)
DB_PATH = "Database/database.db"
def get_connection():
    return sqlite3.connect(DB_PATH, timeout=20)
def create_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            ROLL_NUMBER TEXT NOT NULL UNIQUE,
            BRANCH TEXT NOT NULL,
            CGPA REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()
def insert_student(name, roll_no, branch, cgpa):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO student(NAME,ROLL_NUMBER,BRANCH,CGPA)
        VALUES(?,?,?,?)
    """, (name, roll_no, branch, cgpa))
    connection.commit()
    connection.close()
def view_student():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM student
        ORDER BY ID ASC
    """)
    students = cursor.fetchall()
    connection.close()
    return students
def search_student(roll_no):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM student
        WHERE ROLL_NUMBER=?
    """, (roll_no,))
    student = cursor.fetchone()
    connection.close()
    return student
def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM student
        WHERE ID=?
    """, (student_id,))
    student = cursor.fetchone()
    connection.close()
    return student
def update_student(student_id, name, roll_no, branch, cgpa):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        UPDATE student
        SET
            NAME=?,
            ROLL_NUMBER=?,
            BRANCH=?,
            CGPA=?
        WHERE ID=?
    """, (name, roll_no, branch, cgpa, student_id))
    connection.commit()
    connection.close()
def delete_student(roll_no):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        DELETE FROM student
        WHERE ROLL_NUMBER=?
    """, (roll_no,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted
def total_students():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM student")
    total=cursor.fetchone()[0]
    conn.close()
    return total
def order_student(branch):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM student WHERE BRANCH=? ORDER BY CGPA DESC""", (branch,))
    result = cursor.fetchall()
    connection.close()
    return result
if __name__ == "__main__":
    create_database()