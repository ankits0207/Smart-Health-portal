# Submitted by Ankit Sharma MT16121, Ankit Rehani MT16085 and Suprateek Shula MT16115
from Dao import UserDao, UtilityDao
from tkinter import *
from FrontEnd_GUI import EndUserGUI, SignupGUI, AdminGUI, ModGUI

UtilityDao.UtilityDao().my_util()


def login():
    username = user_name.get()
    password_text = password.get()
    user_type = UserDao.UserDao().login(username, password_text)
    if user_type == 1:
        EndUserGUI.call(username)
    elif user_type == 2:
        ModGUI.call(username)
    elif user_type == 3:
        AdminGUI.call(username)
    else:
        Label(master, text="Invalid user name or password!!").grid(row=6, column=2)


def signup():
    SignupGUI.call()

master = Tk()
Label(master, text="").grid(row=0, column=2)
Label(master, text="Welcome to Smart Health portal!!").grid(row=1, column=2)
Label(master, text="User Name: ").grid(row=2, column=1)
user_name = Entry(master)
user_name.grid(row=2, column=2)
Label(master, text="Password: ").grid(row=3, column=1)
password = Entry(master, show="*")
password.grid(row=3, column=2)
Button(master, text="Login", command=login).grid(row=4, column=2)
Button(master, text="Signup", command=signup).grid(row=5, column=2)

master.mainloop()
