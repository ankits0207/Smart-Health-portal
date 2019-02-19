from tkinter import *
from Entities import Entities
from BusinessLogic import EndUserBL
from Dao import HealthDataDao
import datetime
from FrontEnd_GUI import FriendshipGUI, EndUserDiscussionForumGUI


def call(username):
    def display():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=50)
        listbox.pack()
        retlist = EndUserBL.EndUserBL().read_end_user(username)
        enduserobj = retlist[0]
        datumlist = retlist[1]
        listbox.insert(END, 'UserName(cannot be updated)-' + enduserobj.username)
        listbox.insert(END, '1.Password-' + enduserobj.password)
        listbox.insert(END, '2.FirstEmailID-' + enduserobj.email1)
        listbox.insert(END, '3.SecondEmailID-' + enduserobj.email2)
        listbox.insert(END, '4.FirstName-' + enduserobj.firstname)
        listbox.insert(END, '5.LastName-' + enduserobj.lastname)
        listbox.insert(END, '6.AboutYou-' + enduserobj.aboutme)
        listbox.insert(END, '7.URL1-' + enduserobj.photourl1)
        listbox.insert(END, '8.URL2-' + enduserobj.photourl2)
        listbox.insert(END, '9.URL3-' + enduserobj.photourl3)
        listbox.insert(END, '10.StreetNumber-' + enduserobj.streetnumber)
        listbox.insert(END, '11.StreetName-' + enduserobj.streetname)
        listbox.insert(END, '12.MajorMunicipality-' + enduserobj.majormunicipality)
        listbox.insert(END, '13.Gov. District-' + enduserobj.governingdistrict)
        listbox.insert(END, '14.PostalArea-' + enduserobj.postalarea)
        listbox.insert(END, '15.Karma Score-' + str(enduserobj.karma))
        listbox.insert(END, '********** Health Data **********')
        for d in datumlist:
            listbox.insert(END, 'Datum Id - ' + str(d.datumid) + ' Property ID-' + str(d.propertyid) + ' Value-' + d.value)
        listbox.insert(END, '********** Properties in Database **********')
        myproplist = HealthDataDao.HealthDataDao().read_properties()
        for prop in myproplist:
            listbox.insert(END, 'Property id - ' + str(
                prop.propertyid) + ' Property name - ' + prop.name + ' Property description - ' + prop.description)

    def updatebasic():
        retlist = EndUserBL.EndUserBL().read_end_user(username)
        enduserobj = retlist[0]
        datumlist = retlist[1]
        field_no = e1.get()
        var = e2.get()
        if e1.get() and e2.get():
            if field_no == "1":
                enduserobj.password = var
            elif field_no == "2":
                enduserobj.email1 = var
            elif field_no == "3":
                enduserobj.email2 = var
            elif field_no == "4":
                enduserobj.firstname = var
            elif field_no == "5":
                enduserobj.lastname = var
            elif field_no == "6":
                enduserobj.aboutme = var
            elif field_no == "7":
                enduserobj.photourl1 = var
            elif field_no == "8":
                enduserobj.photourl12 = var
            elif field_no == "9":
                enduserobj.photourl13 = var
            elif field_no == "10":
                enduserobj.streetnumber = var
            elif field_no == "11":
                enduserobj.streetname = var
            elif field_no == "12":
                enduserobj.majormunicipality = var
            elif field_no == "13":
                enduserobj.governingdistrict = var
            elif field_no == "14":
                enduserobj.postalarea = var
            if EndUserBL.EndUserBL().update_end_user(enduserobj) is True:
                Label(master, text="Updated").grid(row=5, column=2)
            else:
                Label(master, text="Not Updated").grid(row=5, column=2)
        else:
            Label(master, text="Both fields (Field Id and Value) are mandatory!!", fg="red").grid(row=5, column=1)

    def updatedatum():
        if e3.get() and e4.get() and e5.get():
            try:
                did = int(e3.get())
                pid = int(e4.get())
                val = e5.get()
                do = Entities.Datum(did, username, pid, val, datetime.date.today())
                if EndUserBL.EndUserBL().update_datum(do) is True:
                    Label(master, text="Updated").grid(row=10, column=2)
                else:
                    Label(master, text="Not Updated").grid(row=10, column=2)
            except Exception as e:
                Label(master, text="Both fields (Datum Id and Product Id) must be integers!!", fg="red").grid(row=10, column=1)
        else:
            Label(master, text="All fields (Datum Id, Property Id, Value) are mandatory!!", fg="red").grid(row=10, column=1)


    master = Tk()
    Label(master, text="***** Welcome EndUser to SmartHealth portal *****").grid(row=0, column=1)
    Button(master, text="Click me to see your details", command=display).grid(row=1, column=1)

    Label(master, text="***** Update your basic details *****").grid(row=2, column=1)
    Label(master, text="Enter the field ID to be updated").grid(row=3, column=0)
    e1 = Entry(master)
    e1.grid(row=3, column=1)
    Label(master, text="Enter the new value").grid(row=4, column=0)
    e2 = Entry(master)
    e2.grid(row=4, column=1)
    Button(master, text="Update", command=updatebasic).grid(row=4, column=2)

    Label(master, text="***** Update your health data details *****").grid(row=6, column=1)
    Label(master, text="Enter the datum ID to be updated").grid(row=7, column=0)
    e3 = Entry(master)
    e3.grid(row=7, column=1)
    Label(master, text="Enter the property id to be updated").grid(row=8, column=0)
    e4 = Entry(master)
    e4.grid(row=8, column=1)
    Label(master, text="Enter the new value").grid(row=9, column=0)
    e5 = Entry(master)
    e5.grid(row=9, column=1)
    Button(master, text="Update", command=updatedatum).grid(row=9, column=2)
    Button(master, text="Visit Friendship Portal", command=lambda:FriendshipGUI.call(username)).grid(row=11, column=1)
    Button(master, text="Visit Discussion Forum", command=lambda:EndUserDiscussionForumGUI.call(username)).grid(row=12, column=1)

    master.mainloop()
