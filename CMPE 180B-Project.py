### We should replace "your_host", "your_user", "your_password", and "your_database" with our actual MySQL server details

import mysql.connector
from getpass import getpass  # For secure password input
import logging

# Setup logging
logging.basicConfig(filename='database_app.log', level=logging.INFO)

# Connect to the MySQL server
try:
    conn = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    cursor = conn.cursor(buffered=True)
    logging.info("Connected to the database.")
except Exception as e:
    logging.error(f"Error connecting to the database: {e}")
    exit()

def login():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Hash or encrypt the password before comparing with the database

    cursor.execute("SELECT * FROM USERS WHERE User_Name = %s AND User_Password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        logging.info(f"User {username} logged in.")
        return user[0]  # Return the User_ID
    else:
        logging.warning(f"Failed login attempt for user {username}.")
        return None

def admin_menu():
    print("1. Add record")
    print("2. Update record")
    print("3. Delete record")
    choice = input("Enter your choice: ")

    # Implement administrative operations based on the choice

  

def purchase_ticket(customer_id):
    # Assume customer is logged in, and you have the customer_id
    schedule_id = input("Enter the Schedule ID for the train you want to book: ")
    seat_type = input("Enter the type of seat (e.g., First Class, Economy): ")

    # Check seat availability and perform the booking
    cursor.execute("SELECT * FROM SCHEDULE WHERE Schedule_ID = %s", (schedule_id,))
    schedule = cursor.fetchone()

    if schedule:
        if schedule[6] > 0:  # Assuming available_seats is a column in the SCHEDULE table
            cursor.execute("INSERT INTO TICKETS (Customer_ID, Schedule_ID, Ticket_Type) VALUES (%s, %s, %s)",
                           (customer_id, schedule_id, seat_type))
            cursor.execute("UPDATE SCHEDULE SET Available_Seats = Available_Seats - 1 WHERE Schedule_ID = %s",
                           (schedule_id,))
            conn.commit()
            print("Ticket purchased successfully!")
        else:
            print("Sorry, the selected train is fully booked.")
    else:
        print("Invalid Schedule ID. Please try again.")

def cancel_ticket():
    Ticket_ID = input("Please enter your ticket number:")
    cursor.execute("SELECT * FROM Tickets WHERE Ticket_ID = %s", (Ticket_ID,))
    ticket = cursor.fetchone()
    if Ticket_ID:
        userAnswer= input("Are you sure you want to cancel this ticket? If so, enter yes. If not, enter no: ")
        if userAnswer == "yes":
            ticket = cursor.fetchone()
            cursor.execute("DELETE FROM Tickets WHERE Ticket_ID = %s", (Ticket_ID,))
            connection.commit()
            print("Ticket has been cancelled")
        else:
            print(" Ticket is not cancelled ")
    else:
        print("The ticket you provided does not exist")

def display_schedules():
    cursor.execute("SELECT * FROM SCHEDULE")
    schedules = cursor.fetchall()

    if schedules:
        print("\nAvailable Train Schedules:")
        for schedule in schedules:
            print(f"Schedule ID: {schedule[0]}, Train ID: {schedule[5]}, Date: {schedule[2]}, Departure: {schedule[4]}, Arrival: {schedule[3]}")
    else:
        print("No schedules available.")

def display_ticket_class():
    cursor.execute("SELECT DISTINCT Ticket_Type, Ticket_Price FROM TICKETS")
    tickets = cursor.fetchall()

    if tickets:
        print("\nTypes of Tickets:")
        for ticket in tickets:
            print(f"Ticket Class: {ticket[0]}, Price: ${ticket[1]:.2f}")

def end_user_menu():
    print("1. View records")
    print("2. Add booking")
    print("3. Cancel booking")
    print("4. Display schedules")
    print("5. Display prices of different classes")
    choice = input("Enter your choice: ")

    if choice == "1":
        # Implement view records functionality
        pass
    elif choice == "2":
        # Implement add booking functionality
        customer_id = session.get('user_id')
        if customer_id:
            purchase_ticket(customer_id)
    elif choice == "3":
        cancel_ticket()
        pass
    elif choice == "4":
        display_schedules()
    elif choice == "5":
        display_ticket_class()





def main():
    user_id = login()

    if user_id:
        # Determine user role (admin or end-user) based on user_id and enable corresponding functionalities
        cursor.execute("SELECT * FROM EMPLOYEES WHERE Employee_ID = %s", (user_id,))
        is_admin = cursor.fetchone()

        if is_admin:
            admin_menu()
        else:
            end_user_menu()

    # Close the connection when done
    conn.close()

if __name__ == "__main__":
    main()
