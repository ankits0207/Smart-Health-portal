from tkinter import *
from Entities import Entities
from BusinessLogic import EndUserBL
from BusinessLogic import Moderator_BL
from BusinessLogic import AdministratorBL
from Dao import HealthDataDao
from Dao import QualificationDao
from Dao import UserDao
from email_validator import validate_email
# from validate_email_address import validate_email
import datetime
import random


def call():
    global count1, count2, l_invalid, l9, l_unique, l_pmail, l_smail, l_all_properties, choice_type, l_error
    l_error = None
    l_invalid = None
    l_unique = None
    l_pmail = None
    l_smail = None
    l_all_properties = None
    l9 = None
    count1 = len(HealthDataDao.HealthDataDao().read_properties())
    count2 = len(QualificationDao.QualificationDao().readall())
    choice_type = None

    def check_if_unique_username():
        global l_unique
        username = e2.get()
        if l_unique is not None:
            l_unique.grid_forget()
        if e2.get():
            if not UserDao.UserDao().check_if_user_exists(username):
                l_unique = Label(master, text="Username is available", fg="green")
                l_unique.grid(row=3, column=2)
            else:
                l_unique = Label(master, text="Username already exists!!", fg="red")
                l_unique.grid(row=3, column=2)
        else:
            l_unique = Label(master, text="Username field is mandatory!!", fg="red")
            l_unique.grid(row=3, column=1)

    def check_if_correct_pemail_id():
        global l_pmail
        email_id = e5.get()
        if l_pmail is not None:
            l_pmail.grid_forget()
        try:
            if e5.get():
                if validate_email(email_id):
                    l_pmail = Label(master, text="Correct email ID", fg="green")
                    l_pmail.grid(row=6, column=2)
                else:
                    l_pmail = Label(master, text="primary mail is not correct", fg="red")
                    l_pmail.grid(row=6, column=2)
            else:
                l_pmail = Label(master, text="EmailID field is mandatory!!", fg="red")
                l_pmail.grid(row=6, column=1)
        except Exception as e:
            l_pmail = Label(master, text=str(e), fg="red")
            l_pmail.grid(row=6, column=2)

    def check_if_correct_semail_id():
        global l_smail
        email_id = e7.get()
        if l_smail is not None:
            l_smail.grid_forget()
        try:
            if e7.get():
                if validate_email(email_id):
                    l_smail = Label(master, text="Correct email ID", fg="green")
                    l_smail.grid(row=8, column=2)
                else:
                    l_smail = Label(master, text="secondaray mail is not correct", fg="red")
                    l_smail.grid(row=8, column=2)
            else:
                l_smail = Label(master, text="EmailID field is mandatory!!", fg="red")
                l_smail.grid(row=8, column=1)
        except Exception as e:
            l_smail = Label(master, text=str(e), fg="red")
            l_smail.grid(row=8, column=2)

    def display_properties():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=50)
        listbox.pack()
        retList = HealthDataDao.HealthDataDao().read_properties()
        for prop in retList:
            listbox.insert(END, 'Property ID-' + str(prop.propertyid) + 'Property Name-' + prop.name +
                           ' Property description - ' + prop.description)

    def add_property():
        flag = 0
        global count1, l_invalid
        if l_invalid is not None:
            l_invalid.grid_forget()
        if e29.get() and e31.get() and count1 > 0:
            try:
                id = int(e29.get())
                val = int(e31.get())
                retList = HealthDataDao.HealthDataDao().read_properties()
                if retList is not None:
                    for ret in retList:
                        if ret.propertyid == id:
                            propidlist.append(id)
                            propvallist.append(val)
                            count1 -= 1
                            flag = 1
                            Label(master, text="count=" + str(count1) + " left").grid(row=27, column=3)
                            break
                    if flag == 0:
                        l_invalid = Label(master, text="Invalid property ID", fg="red")
                        l_invalid.grid(row=30, column=1)
                else:
                    l_invalid = Label(master, text="Properties not present", fg="red")
                    l_invalid.grid(row=30, column=1)
            except Exception as e:
                l_invalid = Label(master, text="property id and value must be integers!!", fg="red")
                l_invalid.grid(row=30, column=1)
        if count1 == 0:
            e29.grid_forget()
            e31.grid_forget()
            b1.grid_forget()
            b2.grid_forget()
            l1.grid_forget()
            l2.grid_forget()
            l3.grid_forget()
            l4.grid_forget()
            if l_invalid is not None:
                l_invalid.grid_forget()

    def display_qualifications():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=50)
        listbox.pack()
        retList = QualificationDao.QualificationDao().readall()
        for qual in retList:
            listbox.insert(END, 'Qualification id - ' + str(
                qual.qualificationid) + ' Description - ' + qual.description)

    def add_qualification():
        global count2, l9

        if l9 is not None:
            l9.grid_forget()
        if e36.get() and count2 > 0:
            try:
                qid = int(e36.get())
                retList = QualificationDao.QualificationDao().readall()
                if QualificationDao.QualificationDao().is_present(qid) is False:
                    l9 = Label(master, text='Qualification id - ' + str(qid) + ' not present in Database ', fg="red")
                    l9.grid(row=37, column=1)
                else:
                    for qual in retList:
                        if qual.qualificationid == qid:
                            qual_list.append(qid)
                            count2 -= 1
                            Label(master, text="count=" + str(count2) + " left").grid(row=34, column=3)
                            break
            except Exception as e:
                l9 = Label(master, text='Qualification id - ' + str(qid) + ' not present in Database ', fg="red")
                l9.grid(row=37, column=1)
        if count2 == 0:
            e36.grid_forget()
            b3.grid_forget()
            b4.grid_forget()
            l5.grid_forget()
            l6.grid_forget()
            l7.grid_forget()
            l8.grid_forget()

    def register():
        global l_all_properties, l_error
        username_flag = 0
        if e2.get() and e4.get() and e5.get() and e7.get() and e9.get() and e10.get() and e11.get() and e12.get() and \
                e13.get() and e14.get() and e15.get() and e16.get() and e17.get() and e18.get() and e19.get() and e21.get():
            try:
                if l_all_properties is not None:
                    l_all_properties.grid_forget()
                if l_error is not None:
                    l_error.grid_forget()
                if e2.get():
                    if not UserDao.UserDao().check_if_user_exists(e2.get()):
                        Label(master, text="Username is available", fg="green").grid(row=3, column=2)
                    else:
                        Label(master, text="Username already exists!!", fg="red").grid(row=3, column=2)
                        username_flag = 1
                else:
                    Label(master, text="Username field is mandatory!!", fg="red").grid(row=3, column=1)

                if e5.get():
                    if validate_email(e5.get()):
                        Label(master, text="Correct email ID", fg="green").grid(row=6, column=2)
                    else:
                        Label(master, text="primary mail is not correct", fg="red").grid(row=6, column=2)
                else:
                    Label(master, text="EmailID field is mandatory!!", fg="red").grid(row=6, column=1)

                if e7.get():
                    if validate_email(e7.get()):
                        Label(master, text="Correct email ID", fg="green").grid(row=8, column=2)
                    else:
                        Label(master, text="secondaray mail is not correct", fg="red").grid(row=8, column=2)
                else:
                    Label(master, text="EmailID field is mandatory!!", fg="red").grid(row=8, column=1)

                uid = int(e21.get())

                if uid == 1:
                    karma = 0
                    enduserobj = Entities.EndUser(karma, datetime.date.today(), e2.get(), e4.get(), e5.get(), e7.get(),
                                                  e9.get(), e10.get(), e11.get(), e12.get(), e13.get(), e14.get(),
                                                  e15.get()
                                                  , e16.get(), e17.get(), e18.get(), e19.get(), uid, 1)
                    proplist = HealthDataDao.HealthDataDao().read_properties()
                    ocount = len(proplist)
                    mcount = ocount
                    datumkey = random.randint(1, 100000)
                    if count1 != 0:
                        l_all_properties = Label(master, text="You have to add all properties!!", fg="red")
                        l_all_properties.grid(row=41, column=1)
                    else:
                        if EndUserBL.EndUserBL().create_end_user(enduserobj) is True:
                            while mcount > 0:
                                datumobj = Entities.Datum(datumkey, e2.get(), propidlist[ocount - mcount],
                                                          propvallist[ocount - mcount], datetime.date.today())
                                EndUserBL.EndUserBL().create_user_datum_mapping(datumobj)
                                datumkey += 1
                                mcount -= 1
                            Label(master, text="Registered!", fg="green").grid(row=40, column=1)
                            propvallist.clear()
                            propidlist.clear()
                            master.after(1000, lambda: Tk.destroy(master))
                elif uid == 2:
                    phone = e22.get()
                    modobj = Entities.Moderator(phone, e2.get(), e4.get(), e5.get(), e7.get(),
                                                e9.get(), e10.get(), e11.get(), e12.get(), e13.get(), e14.get(),
                                                e15.get()
                                                , e16.get(), e17.get(), e18.get(), e19.get(), uid, 1)
                    if Moderator_BL.ModeratorBL().create_moderator(modobj, qual_list) is True:
                        Label(master, text="Registered!!", fg="green").grid(row=40, column=1)
                        qual_list.clear()
                        master.after(1000, lambda: Tk.destroy(master))
                elif uid == 3:
                    phone = e22.get()
                    adminobj = Entities.Administrator(phone, e2.get(), e4.get(), e5.get(), e7.get(),
                                                      e9.get(), e10.get(), e11.get(), e12.get(), e13.get(), e14.get(),
                                                      e15.get()
                                                      , e16.get(), e17.get(), e18.get(), e19.get(), uid, 1)
                    if AdministratorBL.AdministratorBL().create_administrator(adminobj) is True:
                        Label(master, text="Registered!!", fg="green").grid(row=40, column=1)
                        master.after(1000, lambda: Tk.destroy(master))
                else:
                    Label(master, text="Wrong Choice..should be integer number among (1-3)!!", fg="red").grid(row=41,
                                                                                                              column=1)
            except Exception as e:
                if username_flag:
                    l_error = Label(master, text="Username is not unique!!", fg="red")
                    l_error.grid(row=41, column=1)
                elif "invalid literal for int() with base 10:" in str(e):
                    l_error = Label(master, text=str(e) + " Enter Integer value!!", fg="red")
                    l_error.grid(row=41, column=1)
                else:
                    l_error = Label(master, text=str(e), fg="red")
                    l_error.grid(row=41, column=1)
        else:
            Label(master, text="All user fields are mandatory!!", fg="red").grid(row=42, column=1)

    def choice_user_type():
        global choice_type
        if e21.get():
            choice_type = int(e21.get())

    master = Tk()
    Label(master, text="***** SignUp portal *****").grid(row=0, column=1)

    Label(master, text="Enter a unique username ").grid(row=2, column=0)
    e2 = Entry(master)
    e2.grid(row=2, column=1)
    Button(master, text="Check if Unique", command=check_if_unique_username).grid(row=2, column=2)

    l_1 = Label(master, text="Enter your password ")
    l_1.grid(row=4, column=0)
    e4 = Entry(master)
    e4.grid(row=4, column=1)
    l_2 = Label(master, text="Enter the first email id ")
    l_2.grid(row=5, column=0)
    e5 = Entry(master)
    e5.grid(row=5, column=1)
    Button(master, text="Check if correct", command=check_if_correct_pemail_id).grid(row=5, column=2)

    l_3 = Label(master, text="Enter the second email id ")
    l_3.grid(row=7, column=0)
    e7 = Entry(master)
    e7.grid(row=7, column=1)
    Button(master, text="Check if correct", command=check_if_correct_semail_id).grid(row=7, column=2)

    l_4 = Label(master, text="Enter the first name ")
    l_4.grid(row=9, column=0)
    e9 = Entry(master)
    e9.grid(row=9, column=1)
    l_5 = Label(master, text="Enter the last name ")
    l_5.grid(row=10, column=0)
    e10 = Entry(master)
    e10.grid(row=10, column=1)
    l_6 = Label(master, text="Tell us something about yourself ")
    l_6.grid(row=11, column=0)
    e11 = Entry(master)
    e11.grid(row=11, column=1)
    l_7 = Label(master, text="Enter the URL for your first profile photo ")
    l_7.grid(row=12, column=0)
    e12 = Entry(master)
    e12.grid(row=12, column=1)
    l_8 = Label(master, text="Enter the URL for your second profile photo ")
    l_8.grid(row=13, column=0)
    e13 = Entry(master)
    e13.grid(row=13, column=1)
    l_9 = Label(master, text="Enter the URL for your third profile photo ")
    l_9.grid(row=14, column=0)
    e14 = Entry(master)
    e14.grid(row=14, column=1)
    l_10 = Label(master, text="Enter the street number ")
    l_10.grid(row=15, column=0)
    e15 = Entry(master)
    e15.grid(row=15, column=1)
    l_11 = Label(master, text="Enter the street name ")
    l_11.grid(row=16, column=0)
    e16 = Entry(master)
    e16.grid(row=16, column=1)
    l_12 = Label(master, text="Enter the major municipality ")
    l_12.grid(row=17, column=0)
    e17 = Entry(master)
    e17.grid(row=17, column=1)
    l_13 = Label(master, text="Enter the governing district ")
    l_13.grid(row=18, column=0)
    e18 = Entry(master)
    e18.grid(row=18, column=1)
    l_14 = Label(master, text="Enter the postal area ")
    l_14.grid(row=19, column=0)
    e19 = Entry(master)
    e19.grid(row=19, column=1)
    l_15 = Label(master, text="Which type of user do you wish to add?")
    l_15.grid(row=20, column=0)
    l_16 = Label(master, text="1.End User 2.Moderator 3.Administrator")
    l_16.grid(row=21, column=0)
    e21 = Entry(master)
    e21.grid(row=21, column=1)

    l_17 = Label(master, text="*****Property fields are only for End Users and "
                              "qualification fields are only for moderators*****")
    l_17.grid(row=23, column=1)
    b1 = Button(master, text="Click here to see Available properties", command=display_properties)
    b1.grid(row=26, column=1)

    propidlist = []
    propvallist = []
    l1 = Label(master, text="count=" + str(count1) + " left")
    l1.grid(row=27, column=3)
    l2 = Label(master, text="**You have to add values for each property. "
                            "If you want to add more to this list, contact the admin..")
    l2.grid(row=27, column=0)
    l3 = Label(master, text="Enter propertyID to be added")
    l3.grid(row=29, column=0)
    e29 = Entry(master)
    e29.grid(row=29, column=1)
    l4 = Label(master, text="Enter value")
    l4.grid(row=31, column=0)
    e31 = Entry(master)
    e31.grid(row=31, column=1)
    b2 = Button(master, text="Add Property", command=add_property)
    b2.grid(row=31, column=2)
    l_18 = Label(master, text="Emergency Contact Number only for Moderator and Administrator")
    l_18.grid(row=22, column=0)
    e22 = Entry(master)
    e22.grid(row=22, column=1)
    b3 = Button(master, text="Click here to see Available qualifications. ", command=display_qualifications)
    b3.grid(row=33, column=1)
    qual_list = []
    l5 = Label(master, text="count=" + str(count2) + " left")
    l5.grid(row=34, column=3)
    l6 = Label(master, text="**You have to select only from the given qualifications. "
                            "If you want to add more to this list, contact the admin..")
    l6.grid(row=34, column=0)
    l8 = Label(master, text="Invalid ID will lead to no entry in the database!!")
    l8.grid(row=35, column=1)
    l7 = Label(master, text="Enter qualificationID to be added")
    l7.grid(row=36, column=0)
    e36 = Entry(master)
    e36.grid(row=36, column=1)
    b4 = Button(master, text="Add Qualification", command=add_qualification)
    b4.grid(row=36, column=2)

    b_reg = Button(master, text="Register", command=register)
    b_reg.grid(row=39, column=1)
    master.mainloop()
