from Entities import Entities
from BusinessLogic import EndUserBL
from Dao import HealthDataDao
from FrontEnd_Console import FriendshipMain, EndUserDiscussionForumMain
import datetime

def call(username):
    print('Welcome EndUser to SmartHealth')
    #username = input('Enter your username ')
    einput1 = int(input(
        'How can we help you? 1.Display my details 2.Update my details 3.Visit friendship portal 4.Visit Discussion Forum'))
    if einput1 == 1:
        retlist = EndUserBL.EndUserBL().read_end_user(username)
        euobj = retlist[0]
        datumlist = retlist[1]
        print(
            'UserName-' + euobj.username + ' Password-' + euobj.password + ' FirstEmailID-' + euobj.email1 + ' SecondEmailID-' + euobj.email2 + ' FirstName-' + euobj.firstname + ' LastName-' + euobj.lastname + ' AboutYou-' + euobj.aboutme + ' URL1-' + euobj.photourl1 + ' URL2-' + euobj.photourl2 + ' URL3-' + euobj.photourl3 + ' StreetNumber-' + euobj.streetnumber + ' StreetName-' + euobj.streetname + ' MajorMunicipality-' + euobj.majormunicipality + ' Gov. District-' + euobj.governingdistrict + ' PostalArea-' + euobj.postalarea + ' Karma-' + str(euobj.karma))
        print('Following is the Activity Mapping with legend..')
        for d in datumlist:
            print('Property ID-' + str(d.propertyid) + ' Value-'+d.value)
        print(
            '*************************************************************************************************************')
        print('Properties in Database-')
        myproplist = HealthDataDao.HealthDataDao().read_properties()
        for prop in myproplist:
            print('Property id - ' + str(
                prop.propertyid) + ' Property name - ' + prop.name + ' Property description - ' + prop.description)
    elif einput1 == 2:
        retlist = EndUserBL.EndUserBL().read_end_user(username)
        euobj = retlist[0]
        datumlist = retlist[1]
        einput2 = int(input('What do you wish to update? 1.Basic details 2.Activities'))
        if einput2 == 1:
            field_no = int(input(
                "Enter the field number that you wish to update:- 1.Password 2.FirstEmailId 3.SecondEmailId 4.FirstName 5.LastName 6.AboutMe 7.Url1 8.Url2 9.Url3 10.StreetNumber 11.StreetName 12.MajorMunicipality 13.GoverningDistrict 14.PostalArea"))
            if field_no == 1:
                var = input("Enter the new value ")
                euobj.password = var
            elif field_no == 2:
                var = input("Enter the new value ")
                euobj.email1 = var
            elif field_no == 3:
                var = input("Enter the new value ")
                euobj.email2 = var
            elif field_no == 4:
                var = input("Enter the new value ")
                euobj.firstname = var
            elif field_no == 5:
                var = input("Enter the new value ")
                euobj.lastname = var
            elif field_no == 6:
                var = input("Enter the new value ")
                euobj.aboutme = var
            elif field_no == 7:
                var = input("Enter the new value ")
                euobj.photourl1 = var
            elif field_no == 8:
                var = input("Enter the new value ")
                euobj.photourl12 = var
            elif field_no == 9:
                var = input("Enter the new value ")
                euobj.photourl13 = var
            elif field_no == 10:
                var = input("Enter the new value ")
                euobj.streetnumber = var
            elif field_no == 11:
                var = input("Enter the new value ")
                euobj.streetname = var
            elif field_no == 12:
                var = input("Enter the new value ")
                euobj.majormunicipality = var
            elif field_no == 13:
                var = input("Enter the new value ")
                euobj.governingdistrict = var
            elif field_no == 14:
                var = input("Enter the new value ")
                euobj.postalarea = var
            if EndUserBL.EndUserBL().update_end_user(euobj) is True:
                print('Updated!')
        elif einput2 == 2:
            retlist = EndUserBL.EndUserBL().read_end_user(username)
            euobj = retlist[0]
            datumlist = retlist[1]
            print(
                'UserName-' + euobj.username + ' Password-' + euobj.password + ' FirstEmailID-' + euobj.email1 + ' SecondEmailID-' + euobj.email2 + ' FirstName-' + euobj.firstname + ' LastName-' + euobj.lastname + ' AboutYou-' + euobj.aboutme + ' URL1-' + euobj.photourl1 + ' URL2-' + euobj.photourl2 + ' URL3-' + euobj.photourl3 + ' StreetNumber-' + euobj.streetnumber + ' StreetName-' + euobj.streetname + ' MajorMunicipality-' + euobj.majormunicipality + ' Gov. District-' + euobj.governingdistrict + ' PostalArea-' + euobj.postalarea + ' Karma-' + str(
                    euobj.karma))
            print('Following is the Activity Mapping with legend..')
            for d in datumlist:
                print('Datum ID-' + str(d.datumid) +' Property ID-' + str(d.propertyid) + ' Value-' + d.value)
            print(
                '*************************************************************************************************************')
            print('Properties in Database-')
            myproplist = HealthDataDao.HealthDataDao().read_properties()
            for prop in myproplist:
                print('Property id - ' + str(
                    prop.propertyid) + ' Property name - ' + prop.name + ' Property description - ' + prop.description)
            print(
                '*************************************************************************************************************')
            print('To update activity, simply insert the  Datum ID,Property ID and its new value')
            did = int(input('Enter the DatumID'))
            pid = int(input('Enter the PropertyID'))
            val = input('Enter value')
            do = Entities.Datum(did,username,pid,val,datetime.date.today())
            if EndUserBL.EndUserBL().update_datum(do) is True:
                print('Updated!')
    elif einput1 == 3:
        FriendshipMain.call(username)
    elif einput1 == 4:
        EndUserDiscussionForumMain.call(username)