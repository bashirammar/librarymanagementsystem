#!/usr/bin/python3

import mysql.connector
import os
import book
import member
import borrow
import search

password = "Blade369"
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = password,
    database = "lms"
)

def main_menu():
    print("""............LIBRARY MANAGEMENT.............
    1. Add book
    2. Add member
    3. Loan book 
    4. Submit book 
    5. Delete book 
    6. Delete member 
    7. Display 
    8. Search
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        book.addbook()
    elif(choice == '2'):
        member.addmember()
    elif(choice == '3'):
        borrow.loanbook()
    elif(choice == '4'):
        borrow.returnbook()
    elif(choice == '5'):
        book.dbook()
    elif(choice == '6'):
        member.dmember()
    elif(choice == '7'):
        display_menu()
    elif(choice == '8'):
        search.search_menu()   
    else:
        print("wrong choice")
        main_menu()

def display_menu():
    print("""............DISPLAY MENU.............
    1. Display book
    2. Display member
    3. Display loans
    4. Return to main menu
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        dispbook()
    elif(choice == '2'):
        dispmember()
    elif(choice == '3'):
        disploan()
    elif(choice == '4'):
        main_menu()
    else:
        print("wrong choice")
        display_menu()

def dispbook():
    sql = "select * from books"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Book id:",i[0])
        print("Book name:",i[1])
        print("Book author:",i[2])
        print("Book subject:",i[3])
        print("Total:",i[4])
        print("................")


def dispmember():
    sql = "select * from members"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Member id:",i[0])
        print("Member name:",i[1])
        print("Member phone:",i[2])
        print("Member email:",i[3])
        print("Member address:",i[4])
        print("................")
    
def disploan():
    sql = "select * from loans"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("Member id:",i[0])
        print("Member name:",i[1])
        print("book id:",i[2])
        print("book name:",i[3])
        print("borrowing date:",i[4])
        print("returning date:",i[5])
        print("................")

main_menu()

