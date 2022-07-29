import mysql.connector

password = ""
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "lms"
)

def addmember():
    m_id = input("Enter member id:")
    m_name = input("Enter member name: ")
    phone = input("Enter member phone:")
    email = input("Enter member email: ")
    address = input("Enter member address:")
    data = (m_id, m_name, phone, email, address)
    sql = "insert into members(m_id, m_name, phone, email, address) values(%s,%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")

def dmember():
    ac = input("Enter member id:")
    sql = "delete from members where m_id = %s"
    data = (ac,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Member deleted successfully")
