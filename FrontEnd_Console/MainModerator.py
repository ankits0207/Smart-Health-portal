from Entities import Entities
from BusinessLogic import Moderator_BL
from Dao import QualificationDao
from FrontEnd_Console import ModeratorDiscussionForumMain
import random

def call(username):
    print('Welcome Moderator to SmartHealth')
    #username = input('Enter your username ')
    minput1 = int(input(
        'How can we help you? 1.Display my details 2.Update my details 3.Visit Discussion Forum'))
    if minput1 == 1:
        retlist = Moderator_BL.ModeratorBL().read_moderator(username)
        if retlist is not False:
            modobj = retlist[0]
            qual = retlist[1]
            for m in modobj:
                print(
                    'UserName-' + m.username + ' Password-' + m.password + ' FirstEmailID-' + m.email1 + ' SecondEmailID-' + m.email2 + ' FirstName-' + m.firstname + ' LastName-' + m.lastname + ' AboutYou-' + m.aboutme + ' URL1-' + m.photourl1 + ' URL2-' + m.photourl2 + ' URL3-' + m.photourl3 + ' StreetNumber-' + m.streetnumber + ' StreetName-' + m.streetname + ' MajorMunicipality-' + m.majormunicipality + ' Gov. District-' + m.governingdistrict + ' PostalArea-' + m.postalarea + ' Phone-' + m.phone)
            print('Following is the list of Qualifications with legend..')
            if qual is not None:
                for q in qual:
                    print('Qualification ID-' + str(q))
                listall = QualificationDao.QualificationDao().readall()
                print('*************************************************************************************************************')
                print('Qualifications in Database-')
                for l in listall:
                    print('Qualification ID-' + str(l.qualificationid) + ' Description-' + l.description)
        else:
            print("Database altered or user not found!")
    elif minput1 == 2:
        retlist = Moderator_BL.ModeratorBL().read_moderator(username)
        mo = retlist[0]
        qual = retlist[1]
        minput2 = int(input('What do you wish to update? 1.Basic details 2.Qualifications'))
        modobj = mo[0]
        if minput2 == 1:
            field_no = int(input(
                "Enter the field number that you wish to update:- 1.Password 2.FirstEmailId 3.SecondEmailId 4.FirstName 5.LastName 6.AboutMe 7.Url1 8.Url2 9.Url3 10.StreetNumber 11.StreetName 12.MajorMunicipality 13.GoverningDistrict 14.PostalArea 15.EmergencyContact"))
            if field_no == 1:
                var = input("Enter the new value ")
                modobj.password = var
            elif field_no == 2:
                var = input("Enter the new value ")
                modobj.email1 = var
            elif field_no == 3:
                var = input("Enter the new value ")
                modobj.email2 = var
            elif field_no == 4:
                var = input("Enter the new value ")
                modobj.firstname = var
            elif field_no == 5:
                var = input("Enter the new value ")
                modobj.lastname = var
            elif field_no == 6:
                var = input("Enter the new value ")
                modobj.aboutme = var
            elif field_no == 7:
                var = input("Enter the new value ")
                modobj.photourl1 = var
            elif field_no == 8:
                var = input("Enter the new value ")
                modobj.photourl12 = var
            elif field_no == 9:
                var = input("Enter the new value ")
                modobj.photourl13 = var
            elif field_no == 10:
                var = input("Enter the new value ")
                modobj.streetnumber = var
            elif field_no == 11:
                var = input("Enter the new value ")
                modobj.streetname = var
            elif field_no == 12:
                var = input("Enter the new value ")
                modobj.majormunicipality = var
            elif field_no == 13:
                var = input("Enter the new value ")
                modobj.governingdistrict = var
            elif field_no == 14:
                var = input("Enter the new value ")
                modobj.postalarea = var
            elif field_no == 15:
                var = input("Enter the new value ")
                modobj.phone = var
            if Moderator_BL.ModeratorBL().update_moderator(modobj) is True:
                print('Updated!')
        elif minput2 == 2:
            no_of_qual = int(input('Enter count of the qualifications '))
            print('Select from the following qualifications. If you want to add more to this list, contact the admin..')
            myquallist = QualificationDao.QualificationDao().readall()
            myinputlist = []
            for qual1 in myquallist:
                print('Qualification id - ' + str(
                    qual1.qualificationid) + ' Description - ' + qual1.description)
            while no_of_qual > 0:
                qualification_id = int(
                    input('Enter Qualification ID.Invalid ID will not lead to an entry in the database!!'))
                if QualificationDao.QualificationDao().is_present(qualification_id) is False:
                    print('Qualification id - ' + str(qualification_id) + ' not present in Database ')
                else:
                    for qual2 in myquallist:
                        if qual2.qualificationid == qualification_id:
                            myinputlist.append(qual2)
                no_of_qual -= 1
            if Moderator_BL.ModeratorBL().update_qual(modobj,myinputlist) is True:
                print('Updated!')
    elif minput1 == 3:
        ModeratorDiscussionForumMain.call(username)