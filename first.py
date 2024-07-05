from tkinter import simpledialog, messagebox
from tkinter import Tk
from datetime import *
import mysql.connector

dat = date.today()

root = Tk()
root.withdraw()
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="atm"
)

# obj = log().login
# obj2 = log().register

cursor = con.cursor()

print(dat)

session_data = {}

def set_session_data(email, data):
    session_data[email] = data

def get_session_data(email):
    return session_data.get(email)

class bal:
        def balance(b):
            cursor.execute(f"SELECT Balance FROM users WHERE email = '{b}'")
            e = cursor.fetchone()[0]
            s = simpledialog.askstring("Balance", f"Your current balance is: \n R{str(e)} \n \n 1. Back \n 2. Quit")
            if s == '1':
                welcome()
            elif s == '2':
                pass
                
class wit:
    pass
class dep:
    pass
class buy:
    pass


def welcome():
    email = get_session_data("current_email")
    cursor.execute(f"SELECT full_name FROM users WHERE email = '{email}'")
    e = cursor.fetchone()[0]
    cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
    x = cursor.fetchone()[0]
    select = simpledialog.askstring("Home Panel", f"====WELCOME TO OUR RICH ONLY ATM APP===== \n {str(e)} \n Balance: R{str(x)} \n \n select an option below: \n 1. Balance \n 2. Withdrawal \n 3. Deposit \n 4. Buy \n 5. Statement \n 6. Log Out",
                                    initialvalue='input your choice here')

    while int(select) > 0 and int(select) < 7:
        if select == '1':
            bal.balance(email)

            
        elif select == '2':
            cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
            e = cursor.fetchone()[0]
            amount = simpledialog.askstring("Withdraw", "Enter amount you would like to withdraw:")
            e2 = str(e)
            withdraw = float(e2) - float(amount)
            cursor.execute(f"UPDATE users SET Balance = '{str(withdraw)}' WHERE email = '{email}'")
            cursor.execute(f"INSERT INTO statement(email, dates, typez, amount) VALUES ('{email}', '{dat}','withdrawal','- R{amount}')")
            con.commit()
            s = simpledialog.askstring("withdrawal", f"Your new current balance is: \n R{withdraw} \n \n 1. Back \n 2. Quit")
            if s == '1':
                welcome()
                break
            elif s == '2':
                pass
                break
        elif select == '3':
            cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
            e = cursor.fetchone()[0]
            amount = simpledialog.askstring("Deposit", "Enter amount you would like to deposit:")
            e2 = str(e)
            deposit = float(e2) + float(amount)
            cursor.execute(f"UPDATE users SET Balance = '{str(deposit)}' WHERE email = '{email}'")
            cursor.execute(f"INSERT INTO statement(email, dates, typez, amount) VALUES ('{email}', '{dat}','deposit','+ R{amount}')")
            con.commit()
            s = simpledialog.askstring("Deposit",
                                       f"Your new current balance is: \n R{deposit} \n \n 1. Back \n 2. Quit")
            if s == '1':
                welcome()
                break
            elif s == '2':
                pass
                break
        elif select == '4':
            z = simpledialog.askstring("Buy","Select one of the options below: \n 1. Airtime \n 2. Electricity \n 3. Voucher")
            if z == '1':
                cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
                e = cursor.fetchone()[0]
                amount = simpledialog.askstring("Airtime", "Enter amount of airtime you would like to buy:")
                e2 = str(e)
                airtime = float(e2) - float(amount)
                cursor.execute(f"UPDATE users SET Balance = '{str(airtime)}' WHERE email = '{email}'")
                cursor.execute(f"INSERT INTO statement(email, dates, typez, amount) VALUES ('{email}', '{dat}','airtime','- R{amount}')")
                con.commit()
                s = simpledialog.askstring("Airtime",
                                           f"Succesfully bought R{amount} airtime \n Your new current balance is: \n R{airtime} \n \n 1. Back \n 2. Quit")
                if s == '1':
                    welcome()
                    break
                elif s == '2':
                    pass
                    break
            elif z == '2':
                cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
                e = cursor.fetchone()[0]
                amount = simpledialog.askstring("Electricity", "Enter amount of electricity you would like to buy:")
                e2 = str(e)
                electricity = float(e2) - float(amount)
                cursor.execute(f"UPDATE users SET Balance = '{str(electricity)}' WHERE email = '{email}'")
                cursor.execute(f"INSERT INTO statement(email, dates, typez, amount) VALUES ('{email}', '{dat}','electricity','- R{amount}')")
                con.commit()
                s = simpledialog.askstring("Electricity",
                                           f"Succesfully bought R{amount} electricity \n Your new current balance is: \n R{electricity} \n \n 1. Back \n 2. Quit")
                if s == '1':
                    welcome()
                    break
                elif s == '2':
                    pass
                    break
            elif z == '3':
                cursor.execute(f"SELECT Balance FROM users WHERE email = '{email}'")
                e = cursor.fetchone()[0]
                amount = simpledialog.askstring("Voucher", "Enter amount of voucher you would like to buy:")
                e2 = str(e)
                voucher = float(e2) - float(amount)
                cursor.execute(f"UPDATE users SET Balance = '{str(voucher)}' WHERE email = '{email}'")
                cursor.execute(f"INSERT INTO statement(email, dates, typez, amount) VALUES ('{email}', '{dat}','voucher','- R{amount}')")
                con.commit()
                s = simpledialog.askstring("Voucher",
                                           f"Succesfully bought R{amount} voucher \n Your new current balance is: \n R{voucher} \n \n 1. Back \n 2. Quit")
                if s == '1':
                    welcome()
                    break
                elif s == '2':
                    pass
                    break
            else:
                simpledialog.messagebox.showinfo("wrong input", "Please select using 1, 2, or 3")
                welcome()
        elif select == '5':
            cursor.execute(f"SELECT * FROM statement WHERE email = '{email}'")
            rows = cursor.fetchall()
            statement = "\n".join(str(row) for row in rows)
            s = simpledialog.askstring("Statement",
                                       f"Your previous transactions are as follows:\n {statement} \n Press OK to continue \n \n 1. Back \n 2. Quit")
            if s == '1':
                welcome()
            elif s == '2':
                pass
                break
            break
        elif select == '6':
            set_session_data("current_email", None)
            break
    else:
        simpledialog.messagebox.showinfo("selected option",
                                         f"you selected: {select} which is an invalid input, \n please enter a valid input")
        welcome()



root.destroy()