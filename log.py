from tkinter import simpledialog, messagebox
from tkinter import Tk
from datetime import *


from two import logg, reg

class wel:
        
    def welcome1():
        while True:
            q = simpledialog.askinteger("WELCOME", "Would you like to: \n 1. Login \n 2. Register \n 3. Quit")
            if q == 1:
                logg.login()
            elif q == 2:
                reg.register()
            elif q == 3:
                pass
                break
        else:
            simpledialog.messagebox.showinfo("wrong input", "Please select using 1, 2, or 3")
            welcome1()

wel.welcome1()