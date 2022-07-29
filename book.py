import mysql.connector

password = ""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "lms"
)

def addbook():
    b_id = input("Enter book id:")
    b_name = input("Enter book name: ")
    author = input("Enter book author: ")
    sub = input("Enter subject:")
    total = input("Total books:")
    data = (b_id, b_name, author, sub, total)
    sql = "insert into books(b_id, b_name, author, sub, total) values(%s,%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")

def dbook():
    ac = input("Enter book id:")
    sql = "delete from books where b_id = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Book deleted successfully")
