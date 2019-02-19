from Entities import Entities
from BusinessLogic import AdministratorBL
import random

def call(username):
    print('Welcome Administrator to SmartHealth')
    #username = input('Enter your username ')
    ainput1 = int(input(
        'How can we help you? 1.Display my details 2.Update my details 3.Add Qualification for moderator 4.Add Property for End User '))
    if ainput1 == 1:
        adminobj = AdministratorBL.AdministratorBL().read_administrator(username)
        print(
            'UserName-' + adminobj.username + ' Password-' + adminobj.password + ' FirstEmailID-' + adminobj.email1 + ' SecondEmailID-' + adminobj.email2 + ' FirstName-' + adminobj.firstname + ' LastName-' + adminobj.lastname + ' AboutYou-' + adminobj.aboutme + ' URL1-' + adminobj.photourl1 + ' URL2-' + adminobj.photourl2 + ' URL3-' + adminobj.photourl3 + ' StreetNumber-' + adminobj.streetnumber + ' StreetName-' + adminobj.streetname + ' MajorMunicipality-' + adminobj.majormunicipality + ' Gov. District-' + adminobj.governingdistrict + ' PostalArea-' + adminobj.postalarea+ ' Phone-' + adminobj.phone)
    elif ainput1 == 2:
        adminobj = AdministratorBL.AdministratorBL().read_administrator(username)
        field_no = int(input(
            "Enter the field number that you wish to update:- 1.Password 2.FirstEmailId 3.SecondEmailId 4.FirstName 5.LastName 6.AboutMe 7.Url1 8.Url2 9.Url3 10.StreetNumber 11.StreetName 12.MajorMunicipality 13.GoverningDistrict 14.PostalArea 15.EmergencyContact"))
        if field_no == 1:
            var = input("Enter the new value ")
            adminobj.password = var
        elif field_no == 2:
            var = input("Enter the new value ")
            adminobj.email1 = var
        elif field_no == 3:
            var = input("Enter the new value ")
            adminobj.email2 = var
        elif field_no == 4:
            var = input("Enter the new value ")
            adminobj.firstname = var
        elif field_no == 5:
            var = input("Enter the new value ")
            adminobj.lastname = var
        elif field_no == 6:
            var = input("Enter the new value ")
            adminobj.aboutme = var
        elif field_no == 7:
            var = input("Enter the new value ")
            adminobj.photourl1 = var
        elif field_no == 8:
            var = input("Enter the new value ")
            adminobj.photourl12 = var
        elif field_no == 9:
            var = input("Enter the new value ")
            adminobj.photourl13 = var
        elif field_no == 10:
            var = input("Enter the new value ")
            adminobj.streetnumber = var
        elif field_no == 11:
            var = input("Enter the new value ")
            adminobj.streetname = var
        elif field_no == 12:
            var = input("Enter the new value ")
            adminobj.majormunicipality = var
        elif field_no == 13:
            var = input("Enter the new value ")
            adminobj.governingdistrict = var
        elif field_no == 14:
            var = input("Enter the new value ")
            adminobj.postalarea = var
        elif field_no == 15:
            var = input("Enter the new value ")
            adminobj.phone = var
        if AdministratorBL.AdministratorBL().update_administrator(adminobj) is True:
            print('Updated!')
    elif ainput1 == 3:
        qual_id = random.randint(1,1000)
        desc = input('Enter the desciption')
        qo = Entities.Qualification(qual_id,desc)
        if AdministratorBL.AdministratorBL().add_qual(qo) is True:
            print('Added!')
    elif ainput1 == 4:
        propid = random.randint(1,1000)
        name = input("Enter name ")
        desc = input("Enter description ")
        po = Entities.Property(propid, name, desc)
        if AdministratorBL.AdministratorBL().add_property(po) is True:
            print('Added')

