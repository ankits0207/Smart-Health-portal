# Submitted by Ankit Sharma MT16121 and Ankit Rehani MT16085
import FrontEnd_Console, Dao
from FrontEnd_Console import Main_Signup, MainEndUser, MainModerator, MainAdmin
from Dao import UserDao, UtilityDao

UtilityDao.UtilityDao().my_util()
print('Welcome to Smart Health portal!!')
choice1 = 0

while choice1 <= 2:
    var = 1
    choice1 = int(input('1. Register    2. Login    3. Exit'))
    if choice1 == 1:
        Main_Signup.call()
    elif choice1 == 2:
        username = input('Enter your user name: ')
        password = input('Enter your password: ')
        user_type = UserDao.UserDao().login(username,password)
        if user_type == 1:
            while var == 1:
                MainEndUser.call(username)
                var = int(input('Enter 1 to continue!!'))
        elif user_type == 2:
            while var == 1:
                MainModerator.call(username)
                var = int(input('Enter 1 to continue!!'))
        elif user_type == 3:
            while var == 1:
                MainAdmin.call(username)
                var = int(input('Enter 1 to continue!!'))
        else:
            print('Invalid user name or password!!')
