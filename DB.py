import tkinter as tk
import mysql.connector
import random
import hashlib
import os
import bcrypt
from tkinter import *



def connect_to_DB():
    conc = mysql.connector.connect(host = 'localhost', user = 'gautamchintalapati', password = 'new_password', db = 'RailwayDB')
    cursor = conc.cursor()
    create_DB(cursor)
    create_Table(cursor)
    return conc,cursor

def create_DB(cursor):
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]
    if "RailwayDB" not in databases:
        print("db does not exist")
    cursor.execute("USE RailwayDB")


def create_Table(cursor):
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]
    if "customers" not in tables:
        print(" c does not exist")

def register(cursor,conn,data):
    CustomerID = random.randint(1,10000)
    hashed_password = bcrypt.hashpw((data['CUSTOMER_Password']).encode('utf-8'),bcrypt.gensalt(10))
    cursor.execute("""
        INSERT INTO customers (CUSTOMER_ID, CUSTOMER_Name, CUSTOMER_PASSWORD, CUSTOMER_EMAIL, CUSTOMER_Phone_Number)
        VALUES (%s, %s, %s, %s, %s)
    """, (CustomerID,data['CUSTOMER_Name'], hashed_password.decode('utf-8'), data['CUSTOMER_Email'], data['CUSTOMER_Phone_Number']))
    conn.commit()

def login(cursor,data):
    password = bytes(data['CUSTOMER_Password'],encoding=('utf-8'))
    cursor.execute("""
    SELECT CUSTOMER_PASSWORD FROM customers WHERE CUSTOMER_Email = %s""", (data['CUSTOMER_Email'],))
    result = cursor.fetchone()
    print(result)
    if result != None:
        matched = bcrypt.checkpw(password, bytes(result[0]))
        return matched
    else:
        return False
    

def scheduleSelection(cursor,dataForTrain):
    cursor.execute(f"""SELECT * FROM Schedule WHERE Train_Date = '{dataForTrain['Train_Date']}'""")
    rows = cursor.fetchall()
    return rows
   


def purchaseTicketEntry(cursor,conn,dataForTicketPurchase):
    print("function worked")
    departure_station_number = int(dataForTicketPurchase['Departure_Station_Number'])
    arrival_station_number = int(dataForTicketPurchase['Arrival_Station_Number'])

    cursor.execute(f"""SELECT Departure_Station_Number FROM Station where Departure_Station_Number = {departure_station_number}""")
    result1 = cursor.fetchone()
    cursor.execute(f"""SELECT Arrival_Station_Number FROM Station WHERE Arrival_Station_Number = {arrival_station_number}""")
    result2 = cursor.fetchone()
    NoOfStops = 0
    if result1 is not None and result2 is not None:
        print("it worked")
        departure_station_number = result1[0]
        arrival_station_number = result2[0]
        NoOfStops = abs(int(departure_station_number) - int(arrival_station_number))
        FinalTicketPrice = float((NoOfStops * 1.5) +5)
        TicketID = random.randint(1000,9999)

        cursor.execute(f"""SELECT Station_Location From Station WHERE Departure_Station_Number = {departure_station_number}""")
        departureResult= cursor.fetchone()[0]

        cursor.execute(f"""SELECT Station_Location From Station WHERE Arrival_Station_Number = {arrival_station_number}""")
        arrivalResult= cursor.fetchone()[0]
        cursor.execute(f"""INSERT INTO Tickets (Ticket_ID, Train_ID, Ticket_Date, Ticket_Price, Departure_Destination, Arrival_Destination)
                           VALUES({TicketID}, {dataForTicketPurchase['Train_ID']}, '{dataForTicketPurchase['Ticket_Date']}',{FinalTicketPrice},'{departureResult}','{arrivalResult}') 
                            """)
        conn.commit()
        return FinalTicketPrice
    else:
        print("the nums didnt work")
        return None
   


                                               
def admin(cursor,user,passw): 
    if passw:
        db = mysql.connector.connect(host = 'localhost', user = user, password = passw, db = 'RailwayDB')
        cursor = db.cursor()
        return True


    else:
        db = mysql.connector.connect(host = 'localhost', user = user, db = 'RailwayDB')
        cursor = db.cursor()
        return False

    # saveqry = "select * from customers"

    # try:
    #     cursor.execute(saveqry)
    #     result = cursor.fetchall()

    #     for x in result:
    #         print(result)
    #     print("qry successful")
    # except mysql.connector.Error as err:
    #     print(f"Error: {err}")
    #     db.rollback()
        
    # finally:
    #     cursor.close()
    #     db.close()



def cancelTicketFunction(cursor,conn,dataForCancel):
    print(dataForCancel['Ticket_ID'])
    try: 
        cursor.execute(f"""SELECT * FROM Tickets WHERE Ticket_ID = '{dataForCancel['Ticket_ID']}'""")
        ticket = cursor.fetchone()[0]
        print(ticket)
        cursor.execute(f"""DELETE FROM Tickets WHERE Ticket_ID = {dataForCancel['Ticket_ID']}""")
        conn.commit()
        return ticket
    except:
        return None