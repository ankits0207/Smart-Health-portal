import abc
from abc import ABCMeta, abstractmethod


# class containing abstract methods to add, update, delete users
class UserLogic(object):

    @abc.abstractmethod
    def insert_user(self,list_of_users,user_to_add):
        pass

    @abc.abstractmethod
    def delete_user(self,list_of_users,email_id_to_delete,password):
        pass

    @abc.abstractmethod
    def is_user_present(self,list_of_users,user_name):
        pass


#Derived class that implements base class functions, implements polymorphism(overriding)
class Implementation(UserLogic):

    def insert_user(self,list_of_users,user_to_add):
        list_of_users.append(user_to_add)
        return list_of_users



    #returns 1 if user is deleted, 0 if user does not exist
    def delete_user(self,list_of_users,email_id_to_delete,password):
        flag = 0
        for user in list_of_users:
            if user.email_id_1 == email_id_to_delete and user.password == password:
                user.deleted = 'Y'
                flag = 1
                break

        return flag

    #returns 1 if user is present in the list, else returns 0
    def is_user_present(self,list_of_users,user_name):
        flag = 0
        for user in list_of_users:
            if user.user_name == user_name:
                flag = 1
                break

        return flag

