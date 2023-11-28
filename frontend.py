import tkinter as tk
from tkinter import ttk
from DB import *
 
conn, cursor = connect_to_DB()
 
def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
 
 
class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Welcome")
        center_window(800, 400)
         
        login_button = tk.Button(self, text="User Login", width=10,
                          command=self.open_user_login_window)
        login_button.pack(padx=20, pady=(20, 10))

        login_button = tk.Button(self, text="Admin Login", width=10,
                          command=self.open_admin_login_window)
        login_button.pack(padx=20, pady=(20, 10))
         
        register_button = tk.Button(self, text="Register", width=10, 
                          command=self.open_register_window)
        register_button.pack(pady=10)
        self.pack()
         
    def open_user_login_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        UserLoginWindow(self.master)
    
    def open_admin_login_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
         
    def open_register_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)
 
 
class UserLoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("User Login")
        self.master.resizable(False, False)
        center_window(800, 400)
         
        tk.Label(self, text="Username:").grid(row=0, column=0)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)
         
        tk.Label(self, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
         
        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=(10, 0))
 
        submit_button = tk.Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
        self.pack()
             
    def submit(self):
        data={}
        data ['CUSTOMER_Email'] = self.email_entry.get()
        data ['CUSTOMER_Password'] = self.password_entry.get()
        if login(cursor,data) == True:
            print("Logged In!")
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            MainUserWindow(self.master)
        else:
            print("didnt work!")

 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

# class AdminLoginWindow(tk.Frame):
#     def __init__(self, master):
#         super().__init__()
#         self.master = master
#         self.master.title("Admin Login")
#         self.master.resizable(False, False)
#         center_window(800, 400)
         
#         tk.Label(self, text="Username:").grid(row=0, column=0)
#         self.Username = tk.Entry(self)
#         self.Username.grid(row=0, column=1, padx=10, pady=10)
         
#         tk.Label(self, text="Password:").grid(row=1, column=0)
#         self.password = tk.Entry(self, show="*")
#         self.password.grid(row=1, column=1, padx=10, pady=10)
         
#         submit_button = tk.Button(self, text="Submit", width=8, command=self.submitact)
#         submit_button.grid(row=2, column=1, sticky="e", padx=10, pady=(10, 0))
 
#         submit_button = tk.Button(self, text="Back", width=8, command=self.back)
#         submit_button.grid(row=2, column=0, sticky="w", padx=10, pady=(10, 0))
#         self.pack()

#     def submitact(self):
#         user = self.Username.get()
#         passw = self.password.get()
#         print(f"The name you entered is {user} {passw}")
#         if admin(cursor,user, passw) == True:
#             print("logged in")
#         AdminMenuWindow(self.master)
 
#     def back(self):
#         for widget in self.winfo_children(): 
#             widget.destroy()
#         self.destroy()
#         WelcomeWindow(self.master)

 


# class AdminMenuWindow(tk.Frame):
#     def __init__(self, master):
#         super().__init__()
#         self.master = master
#         self.master.title("Admin Menu")
#         self.master.resizable(False, False)
#         center_window(800, 400)

#         addRecord_button = tk.Button(self, text="View train schedule", width=10,command=self.open_addRecord_window)
#         addRecord_button.pack(padx=20, pady=(20, 10))

#         updateRecord_button = tk.Button(self, text="Purchase Ticket", width=10,command=self.open_updateRecord_window)
#         updateRecord_button.pack(padx=20, pady=(20, 10))

#         deleteRecord_button = tk.Button(self, text="Cancel Ticket", width=10,command=self.open_deleteRecord_window)
#         deleteRecord_button.pack(padx=20, pady=(20, 10))
#         self.pack()

class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Register")
        self.master.resizable(False, False)
        center_window(800, 400)
         
        tk.Label(self, text="Name(first and last):").grid(row=1, column=0, sticky="w")
        self.first_name_entry = tk.Entry(self, width=26)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Email:").grid(row=2, column=0, sticky="w")
        self.email_entry = tk.Entry(self, width=26)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        tk.Label(self, text="Password:").grid(row=3, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*", width=26)
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")
         
        tk.Label(self, text="Phone Number:").grid(row=4, column=0, sticky="w")
        self.phoneNO_entry = tk.Entry(self, width=26)
        self.phoneNO_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        
        submit_button = tk.Button(self, text="Submit", width=8, command=self.submit)
        submit_button.grid(row=7, column=1, padx=10, pady=10, sticky="e")
 
        submit_button = tk.Button(self, text="Back", width=8, command=self.back)
        submit_button.grid(row=7, column=0, sticky="w", padx=10, pady=(10, 10))
        self.pack()
         
    def submit(self):
        data = {}
        data ['CUSTOMER_Name'] = self.first_name_entry.get()
        data ['CUSTOMER_Email'] = self.email_entry.get()
        data ['CUSTOMER_Password'] = self.password_entry.get()
        data ['CUSTOMER_Phone_Number'] = self.phoneNO_entry.get()
        register(cursor,conn,data)
 
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)
 
 
class MainUserWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Main Page")
        center_window(800, 400)
        viewSchedule_button = tk.Button(self, text="View train schedule", width=10,
                          command=self.open_viewSchedule_window)
        viewSchedule_button.pack(padx=20, pady=(20, 10))

        purchaseTicket_button = tk.Button(self, text="Purchase Ticket", width=10,
                          command=self.open_purchaseTicket_window)
        purchaseTicket_button.pack(padx=20, pady=(20, 10))

        cancelTicket_button = tk.Button(self, text="Cancel Ticket", width=10,
                          command=self.open_cancelTicket_window)
        cancelTicket_button.pack(padx=20, pady=(20, 10))

        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.pack(padx=20, pady=(20, 10))
        self.pack()
    def open_viewSchedule_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        viewScheduleWindow(self.master)
    def open_purchaseTicket_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForPurchaseWindow(self.master)
    

    def open_cancelTicket_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForCancelWindow(self.master)

    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)

class viewScheduleWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("View Schedule")
        center_window(800, 400)

        tk.Label(self, text="Enter the date of your trip:").grid(row=0, column=0)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=1, column=0, padx=10, pady=10)

        submit_button = tk.Button(self, text="Submit", width=8, command=self.submitSelection)
        submit_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        self.pack()

    def submitSelection(self):
        dataForTrain = {}
        dataForTrain ['Train_Date'] = self.date_entry.get()
        if scheduleSelection(cursor,dataForTrain) != None:
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            displaySchedule(self.master,dataForTrain)
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)
    
class displaySchedule(tk.Frame):
    def __init__(self, master,dataForTrain):
        super().__init__()
        self.master = master
        self.master.title("Schedules Displayed")
        self.dataForTrain = dataForTrain
        center_window(800,400)
        root.resizable(True,True)
        self.pack()
        cursor.execute("SELECT * FROM SCHEDULE")
        results = cursor.fetchall()
        i=1
        # text_widget = Text()
        # text_widget.insert(tk.END, "Hello, Tkinter!\nThis is a multiline text widget.")

        Label(self,width = 10, fg = 'white', text = "Train ID").grid(row = 0, column = 0)
        Label(self,width = 10, fg = 'white', text = "Arrival_Time").grid(row = 0, column = 1)
        Label(self,width = 10, fg = 'white', text = "Departure_Time").grid(row = 0, column = 2)
        Label(self,width = 10, fg = 'white', text = "Train_Date").grid(row = 0, column = 3)
        Label(self,width = 100, fg = 'white', anchor="w", justify="left", text = "Destination").grid(row = 0, column = 4)
        self.pack()
        for x in results:
            # print('stuck here')
            # Label(self,width = 10, fg = 'white', text = f"{x[0]}\t {x[1]}\t {x[2]}\t {x[3]}\t {x[4]}\t").grid(row = i)
            Label(self,width = 10, fg = 'white', text = f"{x[0]}").grid(row = i, column = 0)
            Label(self,width = 10, fg = 'white', text = f"{x[1]}").grid(row = i, column = 1)
            Label(self,width = 10, fg = 'white', text = f"{x[2]}").grid(row = i, column = 2)
            Label(self,width = 10, fg = 'white', text = f"{x[3]}").grid(row = i, column = 3)
            Label(self,width = 100, fg = 'white', anchor="w", justify="left", text = f"{x[4]}").grid(row = i, column = 4)
            self.pack()
            i=i+1
        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row= i, column=2, padx=10, pady=10, sticky="e")
        self.pack()
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)
        # 
        # h = Scrollbar(root,orient = 'horizontal')
        # h.pack(side = BOTTOM, fill = 800)
        # v = Scrollbar(root)
        # v.pack(side = RIGHT, fill = 400)
        # 



class EnterTicketForPurchaseWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Enter values page")
        center_window(800, 400)
        tk.Label(self, text="Enter the Train_ID for the train you want to book: ").grid(row=1, column=0)
        self.TrainID_entry = tk.Entry(self)
        self.TrainID_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Enter the date of your trip: ").grid(row=2, column=0)
        self.date_entry = tk.Entry(self)
        self.date_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Enter the station number of your departure destination: ").grid(row=3, column=0)
        self.departureDestination_entry = tk.Entry(self)
        self.departureDestination_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self, text="Enter the station number of your arrival destination: ").grid(row=4, column=0)
        self.finalDestination_entry = tk.Entry(self)
        self.finalDestination_entry.grid(row=4, column=1, padx=10, pady=10)

        enterTicket_button = tk.Button(self, text="Enter", width=8, command=self.enterTicket)
        enterTicket_button.grid(row=4, column=5, padx=10, pady=10, sticky="e")

        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row=4, column=6, padx=10, pady=10, sticky="e")
        self.pack()
    def getTrainID(self):
        return  self.TrainID_entry()
    def enterTicket(self):
        dataForTicketPurchase ={}
        dataForTicketPurchase ['Train_ID'] = self.TrainID_entry.get()
        dataForTicketPurchase['Ticket_Date'] = self.date_entry.get()
        dataForTicketPurchase['Departure_Station_Number'] = self.departureDestination_entry.get()
        dataForTicketPurchase['Arrival_Station_Number'] = self.finalDestination_entry.get()
        NoOfStops = abs(int( dataForTicketPurchase['Departure_Station_Number']) - int(dataForTicketPurchase['Arrival_Station_Number']))
        Ticket_Price = float((NoOfStops * 1.5) +5)
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        purchaseTicketWindow(self.master, dataForTicketPurchase,Ticket_Price)
        
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)


class purchaseTicketWindow(tk.Frame):
    def __init__(self, master,dataForTicketPurchase, Ticket_Price):
        super().__init__()
        self.master = master
        self.dataForTicketPurchase = dataForTicketPurchase
        self.Ticket_Price = Ticket_Price
        self.master.title("Purchase Ticket")
        center_window(800, 400)
        tk.Label(self, text = f"Your total is ${'{:.2f}'.format(self.Ticket_Price)} . Are you sure you want to purchase this ticket?  ").grid(row=1, column=0)
        yes_button = tk.Button(self, text ="YES", width =9, command=lambda: self.yesFunction(master, dataForTicketPurchase))
        yes_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        
        no_button = tk.Button(self, text ="NO", width =9, command = self.noFunction)
        no_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        self.pack()

    def yesFunction(self, master,dataForTicketPurchase):
        Ticket_Price = purchaseTicketEntry(cursor, conn, dataForTicketPurchase)
        if Ticket_Price != None:
            print('ticket price found')
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            confirmedPurchaseWindow(self.master,Ticket_Price)

    def noFunction(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForPurchaseWindow(self.master)

class confirmedPurchaseWindow(tk.Frame):
    def __init__(self, master,Ticket_Price):
        super().__init__()
        self.master = master
        self.Ticket_Price = Ticket_Price
        self.master.title("Ticket Purchased!")
        center_window(800, 400)

        tk.Label(self, text ="The ticket has been purchased!").grid(row=0, column=0)
        back_button = tk.Button(self, text ="Back", width =9, command = self.back)
        back_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.pack()
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)


class EnterTicketForCancelWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Enter values page")
        center_window(800, 400)

        tk.Label(self, text="Enter the Ticket_ID of the train you want to cancel: ").grid(row=0, column=0)
        self.TicketID_entry = tk.Entry(self)
        self.TicketID_entry.grid(row=0, column=1, padx=10, pady=10)

        enterTicket_button = tk.Button(self, text="Enter", width=8, command= self.nextPage)
        enterTicket_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        back_button = tk.Button(self, text="Back", width=8, command=self.back)
        back_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        self.pack()

    def nextPage(self):
        dataForCancel ={}
        dataForCancel ['Ticket_ID'] = self.TicketID_entry.get()
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        ConfirmTicketForCancelWindow(self.master,dataForCancel)
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)

class ConfirmTicketForCancelWindow(tk.Frame):
    def __init__(self, master,dataForCancel):
        super().__init__()
        self.master = master
        self.master.title("Confirm")
        self.dataForCancel = dataForCancel
        center_window(800, 400)

        tk.Label(self, text = "Are you sure you want to cancel this ticket? ").grid(row=0,column=0)
        confirmCancel_Button=tk.Button(self,text="Confirm", width=8, command= lambda: self.confirmCancel(self.dataForCancel))
        confirmCancel_Button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        noCancel_Button =tk.Button(self,text="NO", width=8, command=self.noCancel )
        noCancel_Button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.pack()

    def confirmCancel(self,dataForCancel):
        ticket = cancelTicketFunction(cursor,conn,dataForCancel)
        if ticket == None:
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            notCancelLabel(self.master)

        elif ticket != None:
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            cancelLabel(self.master)
        else:
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            elseCancelLabel(self.master)

    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)
    def noCancel(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForCancelWindow(self.master)
class cancelLabel(tk.Frame):
    def __init__(self,master):
        print("it is here")
        super().__init__()
        self.master = master
        self.master.title("Confirm")
        center_window(800, 400)
        tk.Label(self,text = "The ticket has been canceled").grid(row=2,column=0)

        back_Button =tk.Button(self,text="Back", width=8, command=self.back_Button )
        back_Button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.pack()

    def back_Button(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        MainUserWindow(self.master)

class notCancelLabel(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.master.title("Confirm")
        center_window(800, 400)
        tk.Label(self,text = "The ticket you provided does not exist").grid(row=2,column=0)

        back_Button =tk.Button(self,text="Back", width=8, command=self.back_Button )
        back_Button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.pack()
    def back_Button(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForCancelWindow(self.master)


class elseCancelLabel(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master = master
        self.master.title("Confirm")
        center_window(800, 400)
        tk.Label(self,text = "The ticket has not been cancelled").grid(row=2,column=0)
        back_Button =tk.Button(self,text="Back", width=8, command=self.back_Button )
        back_Button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.pack()
    def back_Button(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        EnterTicketForCancelWindow(self.master)

root = tk.Tk()
root.eval('tk::PlaceWindow . center')
root.resizable(True,True)
WelcomeWindow(root)
root.mainloop()