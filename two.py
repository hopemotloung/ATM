from first import *

class logg:
   def login():
    try:
        email = simpledialog.askstring("Registration", "Enter email:")
        password = simpledialog.askstring("Registration", "Enter password:")
        
        cursor.execute("SELECT email, pass FROM users")
        rows = cursor.fetchall()
        
        for row in rows:
            db_email, db_password = row
            if email == db_email and password == db_password:
                set_session_data("current_email", email)
                print("Email is available")
                welcome()
                break  # Exit the loop after successful login
        else:
            print("Email is not available")
            simpledialog.messagebox.showinfo("Wrong input", "Your login details are invalid")
            while True:
                q = simpledialog.askinteger("WELCOME", "Would you like to: \n 1. Login \n 2. Register \n 3. Quit")
                if q == 1:
                    logg.login()
                elif q == 2:
                    logg.register()
                elif q == 3:
                    pass
                    break
            else:
                simpledialog.messagebox.showinfo("wrong input", "Please select using 1, 2, or 3")

        cursor.close()
        
    except mysql.connector.Error as err:
        print("Error reading database: ", err)

class reg:
    def register():
        ob = logg.login()
        full_name = simpledialog.askstring("Registration", "Enter full name:")
        email = simpledialog.askstring("Registration", "Enter email:")
        password = simpledialog.askstring("Registration", "Enter password:")
        cursor.execute(f"INSERT INTO users(email, pass, full_name, Balance) VALUES ('{email}',{password},'{full_name}', '1000')")
        cursor.execute(f"INSERT INTO statement(email) VALUES ('{email}')")
        con.commit()
        messagebox.showinfo("information","Succesfully registered \n Please procced to login")
        ob.login()