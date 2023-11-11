# SCHOOL PROJECT
# E- Ticketing system for reservation and cancellation of a single ticket at a time.
# RESERVATION
# train no.
# passenger name
# train name
# ticket no. unique


# CANCELLATION
# ticket no.


import mysql.connector
import random

mydb = mysql.connector.connect(host="localhost", user="neha", passwd="password",
                               database="railway")  # connecting the database and python
mycursor = mydb.cursor()
# tablename = 'reservedseats'


# RESERVATION
def reserve():
    print("1.TRAIN A -12563")
    print("2.TRAIN B -12345")
    print("3.TRAIN C -12785")

    train_name = input("Enter train  name:")
    train_no = int(input("Enter train number:"))

    if train_no == 12563:
        booking_func("train_a", 12563)
    elif train_no == 12345:
        booking_func("train b", 12345)

    elif train_no == 12785:
        booking_func("train c", 12785)
    else:
        print("NO TRAIN WITH THIS NAME FOUND")


# CANCELLATION
def cancel():
    ticket_no = str(input("Enter your ticket number:"))
    mycursor.execute("DELETE FROM reservedseats where ticket_no = %s ", (ticket_no,))

    mydb.commit()
    print(mycursor.rowcount, "records deleted")
    if mycursor.rowcount == 0:
        print("Your ticket has not been cancelled yet!!")
    else:
        print("Your ticket is been cancelled!!")



def booking_func(train_name, train_no):
    passenger_name = input("Enter passenger name:")
    ticket_no = random.randint(111, 999)  # append passenger name in table
    values = (passenger_name, train_name, train_no, ticket_no)
    statement = "insert into reservedseats values( %s, %s, %s, %s)"
    mycursor.execute(statement, values)
    mydb.commit()
    print("Your ticket number is:", ticket_no)
    print(mycursor.rowcount, "ticket booked successfully")


def reservationMenu():
    while 1:
        print("This website can be used for:")
        print("1.RESERVATION (one ticket at a time)")
        print("2.CANCELLATION (one ticket at a time)")
        print("3.EXIT APPLICATION")

        choice = input("What do you want to use the website for ? ")
        if choice == "1":
            reserve()
            mydb.close()
        elif choice == "2":
            cancel()
            mydb.close()
        elif choice == '3':
            print("Exiting")
            break
        else:
            print("Incorrect Input. Program will exit now !")
            break
        print("==================================================")


reservationMenu()
