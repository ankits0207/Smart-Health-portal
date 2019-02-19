from Entities import Entities
from BusinessLogic import EndUserBL
from BusinessLogic import Moderator_BL
from BusinessLogic import AdministratorBL
from Dao import HealthDataDao
from Dao import QualificationDao
from Dao import UserDao
import datetime
import random

def call():
    datumkey = random.randint(1,100000)
    username = input("Enter the username ")
    if not UserDao.UserDao().check_if_user_exists(username):
        password = input('Enter your password ')
        eid_1 = input("Enter the first email id ")
        eid_2 = input("Enter the second email id ")
        fname = input("Enter the first name ")
        lname = input("Enter the last name ")
        about_me = input("Tell us something about yourself ")
        url_1 = input("Enter the URL for your first profile photo ")
        url_2 = input("Enter the URL for your second profile photo ")
        url_3 = input("Enter the URL for your third profile photo ")
        street_num = input("Enter the street number ")
        street_name = input("Enter the street name ")
        major_municipality = input("Enter the major municipality ")
        gov_district = input("Enter the governing district ")
        post_area = input("Enter the postal area ")
        #status = int(input("Enter the status-Should be tinyint.. "))
        print("Which type of user do you wish to add?")
        print("1.End User 2.Moderator 3.Administrator")
        command_var_2 = int(input())
        if command_var_2 == 1:
            user_type_id = 1
            print('Enter the values for the following properties-')
            myproplist = HealthDataDao.HealthDataDao().read_properties()
            mypropidlist = []
            propvallist = []
            if myproplist is not None:
                for prop in myproplist:
                    mypropidlist.append(prop.propertyid)
                    print('Property id - ' + str(
                        prop.propertyid) + ' Property name - ' + prop.name + ' Property description - ' + prop.description)
                looplen = len(myproplist)
                while looplen > 0:
                    propvallist.append(int(input('Enter the value for the property in order')))
                    looplen -= 1
                karma = 0
                enduserobj = Entities.EndUser(karma, datetime.date.today(), username, password, eid_1, eid_2, fname, lname,
                                              about_me, url_1,
                                              url_2, url_3, street_num, street_name, major_municipality, gov_district, post_area,
                                              user_type_id, 1)
                olooplen = len(myproplist)
                mlooplen = len(myproplist)
                if EndUserBL.EndUserBL().create_end_user(enduserobj) is True:
                    while mlooplen > 0:
                        datumobj = Entities.Datum(datumkey, username, mypropidlist[olooplen - mlooplen], propvallist[olooplen - mlooplen], datetime.date.today())
                        EndUserBL.EndUserBL().create_user_datum_mapping(datumobj)
                        datumkey += 1
                        mlooplen -= 1
                    print("Added!")
            else:
                print("No properties exist! Ask admin to add properties")
        elif command_var_2 == 2:
            user_type_id = 2
            emergency_no = input('Enter your emergency contact number ')
            no_of_qual = int(input('Enter count of the qualifications '))
            myquallist = QualificationDao.QualificationDao().readall()
            myinputlist = []
            if myquallist != None:
                print(
                    'Select from the following qualifications. If you want to add more to this list, contact the admin..')
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
                modobj = Entities.Moderator(emergency_no, username, password, eid_1, eid_2, fname, lname,
                                            about_me, url_1,
                                            url_2, url_3, street_num, street_name, major_municipality, gov_district,
                                            post_area,
                                            user_type_id, 1)
                Moderator_BL.ModeratorBL().create_moderator(modobj, myinputlist)
                print("Added!")
            else:
                print("No qualification found! Ask the admin to add a qualification")
        elif command_var_2 == 3:
            user_type_id = 3
            emergency_no = input("Enter your emergency contact number ")
            adminobj = Entities.Administrator(emergency_no, username, password, eid_1, eid_2, fname, lname,
                                          about_me, url_1,
                                          url_2, url_3, street_num, street_name, major_municipality, gov_district, post_area,
                                          user_type_id, 1)
            if AdministratorBL.AdministratorBL().create_administrator(adminobj) is True:
                print("Added!")
    else:
        print('User name already exists! Try again')
        call()