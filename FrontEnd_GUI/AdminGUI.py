from tkinter import *
from Entities import Entities
from BusinessLogic import AdministratorBL
import random

def call(username):
    def display():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=30)
        listbox.pack()
        adminobj = AdministratorBL.AdministratorBL().read_administrator(username)
        listbox.insert(END, 'UserName(cannot be updated)-' + adminobj.username)
        listbox.insert(END, '1.Password-' + adminobj.password)
        listbox.insert(END, '2.FirstEmailID-' + adminobj.email1)
        listbox.insert(END, '3.SecondEmailID-' + adminobj.email2)
        listbox.insert(END, '4.FirstName-' + adminobj.firstname)
        listbox.insert(END, '5.LastName-' + adminobj.lastname)
        listbox.insert(END, '6.AboutYou-' + adminobj.aboutme)
        listbox.insert(END, '7.URL1-' + adminobj.photourl1)
        listbox.insert(END, '8.URL2-' + adminobj.photourl2)
        listbox.insert(END, '9.URL3-' + adminobj.photourl3)
        listbox.insert(END, '10.StreetNumber-' + adminobj.streetnumber)
        listbox.insert(END, '11.StreetName-' + adminobj.streetname)
        listbox.insert(END, '12.MajorMunicipality-' + adminobj.majormunicipality)
        listbox.insert(END, '13.Gov. District-' + adminobj.governingdistrict)
        listbox.insert(END, '14.PostalArea-' + adminobj.postalarea)
        listbox.insert(END, '15.Phone-' + adminobj.phone)

    def update():
        adminobj = AdministratorBL.AdministratorBL().read_administrator(username)
        field_no = e1.get()
        var = e2.get()
        if e1.get() and e2.get():
            if field_no == "1":
                adminobj.password = var
            elif field_no == "2":
                adminobj.email1 = var
            elif field_no == "3":
                adminobj.email2 = var
            elif field_no == "4":
                adminobj.firstname = var
            elif field_no == "5":
                adminobj.lastname = var
            elif field_no == "6":
                adminobj.aboutme = var
            elif field_no == "7":
                adminobj.photourl1 = var
            elif field_no == "8":
                adminobj.photourl12 = var
            elif field_no == "9":
                adminobj.photourl13 = var
            elif field_no == "10":
                adminobj.streetnumber = var
            elif field_no == "11":
                adminobj.streetname = var
            elif field_no == "12":
                adminobj.majormunicipality = var
            elif field_no == "13":
                adminobj.governingdistrict = var
            elif field_no == "14":
                adminobj.postalarea = var
            elif field_no == "15":
                adminobj.phone = var
            if AdministratorBL.AdministratorBL().update_administrator(adminobj) is True:
                Label(master, text="Updated").grid(row=5, column=2)
            else:
                Label(master, text="Not Updated").grid(row=5, column=2)
        else:
            Label(master, text="Both fields (Field Id and New value) are mandatory!!", fg="red").grid(row=5, column=1)

    def addqual():
        qual_id = random.randint(1, 1000)
        desc = e3.get()
        if e3.get():
            qo = Entities.Qualification(qual_id, desc)
            if AdministratorBL.AdministratorBL().add_qual(qo) is True:
                Label(master, text="Added").grid(row=8, column=2)
            else:
                Label(master, text="Not Added").grid(row=8, column=2)
        else:
            Label(master, text="Qualification description is mandatory!!", fg="red").grid(row=8, column=1)
    def addprop():
        propid = random.randint(1, 1000)
        name = e4.get()
        desc = e5.get()
        if e4.get() and e5.get():
            po = Entities.Property(propid, name, desc)
            if AdministratorBL.AdministratorBL().add_property(po) is True:
                Label(master, text="Added").grid(row=12, column=2)
            else:
                Label(master, text="Not Added").grid(row=12, column=2)
        else:
            Label(master, text="Both fields (Property name and Description) are mandatory!!", fg="red").grid(row=12, column=1)

    master = Tk()
    Label(master, text="***** Welcome Admin to SmartHealth portal *****").grid(row=0, column=1)
    Button(master, text="Click me to see your details", command=display).grid(row=1, column=1)

    Label(master, text="***** Update your details *****").grid(row=2, column=1)
    Label(master, text="Enter the field ID to be updated").grid(row=3, column=0)
    e1 = Entry(master)
    e1.grid(row=3, column=1)
    Label(master, text="Enter the new value").grid(row=4, column=0)
    e2 = Entry(master)
    e2.grid(row=4, column=1)
    Button(master, text="Update", command=update).grid(row=4, column=2)

    Label(master, text="***** Add qualification for Moderator *****").grid(row=6, column=1)
    Label(master, text="Enter the description for your qualification").grid(row=7, column=0)
    e3 = Entry(master)
    e3.grid(row=7, column=1)
    Button(master, text="Add Qualification", command=addqual).grid(row=7, column=2)

    Label(master, text="***** Add property for End User *****").grid(row=9, column=1)
    Label(master, text="Enter the name for your property").grid(row=10, column=0)
    e4 = Entry(master)
    e4.grid(row=10, column=1)
    Label(master, text="Enter the description for your property").grid(row=11, column=0)
    e5 = Entry(master)
    e5.grid(row=11, column=1)
    Button(master, text="Add Property", command=addprop).grid(row=11, column=2)

    master.mainloop()