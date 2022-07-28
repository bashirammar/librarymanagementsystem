import mysql.connector

password = "Blade369"
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "lms"
)

def loanbook():
    regno  = input("Enter regno:")
    b_id = input("Enter book id:")
    b_name = input("Enter book name:")
    m_id = input("Enter member id:")
    m_name = input("Enter member name:")
    l_date = input("Enter date:")
    r_date = input("Enter date:")
    sql  = "insert into loans(regno, b_id, b_name, m_id, m_name, l_date, r_date) values(%s,%s,%s,%s,%s,%s,%s)"
    data =(regno, b_id, b_name, m_id, m_name, l_date, r_date)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book borrowed to :",m_name)
    bookup(b_id,-1)

def returnbook():
    regno  = input("Enter regno:")
    b_id = input("Enter book id:")
    m_name = input("Enter member name:")
    sql = "delete from loans where regno = %s"
    data = (regno,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("Book returned from :",m_name)
    bookup(b_id,1)

def dbook():
    ac = input("Enter book id:")
    sql = "delete from books where b_id = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()


def bookup(co,u):
    sql = "select TOTAL from books where b_id = %s"
    data = (co,)
    c = mydb.cursor()
    c.execute(sql,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set TOTAL = %s where b_id = %s"
    d = (t,co)
    c.execute(sql,d)
    mydb.commit()
