import mysql.connector

password = "Blade369"
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "lms"
)

def search_book(field):
    print('\n BOOK SEARCH SCREEN ')
    print('-'*120)
    msg ='Enter '+ field +' Value :'
    title = input(msg)
    sql ='select * from books where '+ field + ' like "%'+ title+'%"'
    c = mydb.cursor()
    c.execute(sql)
    records = c.fetchall()
    print('Search Result for :',field,' :' ,title)
    print('-'*120)
    for record in records:
      print(record)
    mydb.close()

def search_menu():
    while True:
      print(' S E A R C H   M E N U ')
      print("\n1.  Book Name")
      print('\n2.  Book Author')
      print('\n3.  Book Category')
      print('\n4.  Exit task')
      print('\n\n')
      choice = int(input('Enter task no: '))
      field =''
      if choice == 1:
        field='b_name'
      if choice == 2:
        field = 'author'
      if choice == 3:
        field = 'sub'
      if choice == 4:
        break
      search_book(field)