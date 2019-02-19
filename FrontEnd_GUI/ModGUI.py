from tkinter import *
from BusinessLogic import Moderator_BL
from Dao import QualificationDao
from FrontEnd_GUI import ModeratorDiscussionForumGUI

global l9
l9 = None
count = len(QualificationDao.QualificationDao().readall())


def call(username):
    def display():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=50)
        listbox.pack()
        retlist = Moderator_BL.ModeratorBL().read_moderator(username)
        if retlist is not False:
            m = retlist[0]
            qualList = retlist[1]
            for modobj in m:
                listbox.insert(END, 'UserName(cannot be updated)-' + modobj.username)
                listbox.insert(END, '1.Password-' + modobj.password)
                listbox.insert(END, '2.FirstEmailID-' + modobj.email1)
                listbox.insert(END, '3.SecondEmailID-' + modobj.email2)
                listbox.insert(END, '4.FirstName-' + modobj.firstname)
                listbox.insert(END, '5.LastName-' + modobj.lastname)
                listbox.insert(END, '6.AboutYou-' + modobj.aboutme)
                listbox.insert(END, '7.URL1-' + modobj.photourl1)
                listbox.insert(END, '8.URL2-' + modobj.photourl2)
                listbox.insert(END, '9.URL3-' + modobj.photourl3)
                listbox.insert(END, '10.StreetNumber-' + modobj.streetnumber)
                listbox.insert(END, '11.StreetName-' + modobj.streetname)
                listbox.insert(END, '12.MajorMunicipality-' + modobj.majormunicipality)
                listbox.insert(END, '13.Gov. District-' + modobj.governingdistrict)
                listbox.insert(END, '14.PostalArea-' + modobj.postalarea)
                listbox.insert(END, '15.Phone-' + str(modobj.phone))
            listbox.insert(END, '********** Qualifications Data **********')
            for q in qualList:
                listbox.insert(END, 'Qualification Id - ' + str(q))
            listbox.insert(END, '********** Qualifications in Database **********')
            listAll = QualificationDao.QualificationDao().readall()
            for l in listAll:
                listbox.insert(END, 'Qualification Id - ' + str(l.qualificationid) + ' Description - ' + l.description)

    def updatebasic():
        retlist = Moderator_BL.ModeratorBL().read_moderator(username)
        mo = retlist[0]
        qual = retlist[1]
        modobj = mo[0]
        if e1.get() and e2.get():
            try:
                field_no = e1.get()
                var = e2.get()
                if field_no == "1":
                    modobj.password = var
                elif field_no == "2":
                    modobj.email1 = var
                elif field_no == "3":
                    modobj.email2 = var
                elif field_no == "4":
                    modobj.firstname = var
                elif field_no == "5":
                    modobj.lastname = var
                elif field_no == "6":
                    modobj.aboutme = var
                elif field_no == "7":
                    modobj.photourl1 = var
                elif field_no == "8":
                    modobj.photourl12 = var
                elif field_no == "9":
                    modobj.photourl13 = var
                elif field_no == "10":
                    modobj.streetnumber = var
                elif field_no == "11":
                    modobj.streetname = var
                elif field_no == "12":
                    modobj.majormunicipality = var
                elif field_no == "13":
                    modobj.governingdistrict = var
                elif field_no == "14":
                    modobj.postalarea = var
                elif field_no == "15":
                    modobj.phone = var
                if Moderator_BL.ModeratorBL().update_moderator(modobj) is True:
                    Label(master, text="Updated!!").grid(row=5, column=2)
                else:
                    Label(master, text="Not Updated!!").grid(row=5, column=2)
            except Exception as e:
                Label(master, text="Field ID must be integer!!", fg="red").grid(row=10, column=1)
        else:
            Label(master, text="Both fields (Field Id and Value) are mandatory!!", fg="red").grid(row=5, column=1)


    def display_qualifications():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=50)
        listbox.pack()
        retList = QualificationDao.QualificationDao().readall()
        for qual in retList:
            listbox.insert(END, 'Qualification id - ' + str(
                            qual.qualificationid) + ' Description - ' + qual.description)


    def add_qualification():
        global count, l9

        if l9 is not None:
            l9.grid_forget()
        if e3.get() and count>0:
            qid = int(e3.get())
            retList = QualificationDao.QualificationDao().readall()
            if QualificationDao.QualificationDao().is_present(qid) is False:
                l9 = Label(master, text='Qualification id - ' + str(qid) + ' not present in Database ', fg="red")
                l9.grid(row=11, column=1)
            else:
                for qual in retList:
                    if qual.qualificationid == qid:
                        qual_list.append(qual)
                        count -= 1
                        Label(master, text="count=" + str(count) + " left").grid(row=8, column=3)
                        break
        if count == 0:
            e3.grid_forget()
            b3.grid_forget()
            b4.grid_forget()
            l5.grid_forget()
            l6.grid_forget()
            l7.grid_forget()
            l8.grid_forget()


    def update():
        if e3.get():
            retlist = Moderator_BL.ModeratorBL().read_moderator(username)
            if retlist is not False:
                m = retlist[0]
                modobj = m[0]
                if Moderator_BL.ModeratorBL().update_qual(modobj, qual_list) is True:
                    Label(master, text="Updated!!", fg="green").grid(row=40, column=1)
        else:
            Label(master, text="Qualification Id, Value) are mandatory!!", fg="red").grid(row=10, column=1)
        qual_list.clear()
    master = Tk()
    Label(master, text="***** Welcome Moderator to SmartHealth portal *****").grid(row=0, column=1)
    Button(master, text="Click me to see your details", command=display).grid(row=1, column=1)

    Label(master, text="***** Update your basic details *****").grid(row=2, column=1)
    Label(master, text="Enter the field ID to be updated").grid(row=3, column=0)
    e1 = Entry(master)
    e1.grid(row=3, column=1)
    Label(master, text="Enter the new value").grid(row=4, column=0)
    e2 = Entry(master)
    e2.grid(row=4, column=1)
    Button(master, text="Update", command=updatebasic).grid(row=4, column=2)

    Label(master, text="***** Update qualification details *****").grid(row=6, column=1)
    b3 = Button(master, text="Click here to see Available qualifications. ", command=display_qualifications)
    b3.grid(row=7, column=1)

    qual_list = []
    l5 = Label(master, text="count=" + str(count) + " left")
    l5.grid(row=8, column=3)
    l6 = Label(master, text="**You have to select only from the given qualifications. "
                            "If you want to add more to this list, contact the admin..")
    l6.grid(row=8, column=0)
    l8 = Label(master, text="Invalid ID will lead to no entry in the database!!")
    l8.grid(row=9, column=1)
    l7 = Label(master, text="Enter qualificationID to be added")
    l7.grid(row=10, column=0)
    e3 = Entry(master)
    e3.grid(row=10, column=1)
    b4 = Button(master, text="Add", command=add_qualification)
    b4.grid(row=10, column=2)

    Button(master, text="Update", command=update).grid(row=14, column=1)

    Button(master, text="Visit Discussion Forum", command=lambda:ModeratorDiscussionForumGUI.call(username)).grid(row=15, column=1)

    master.mainloop()
