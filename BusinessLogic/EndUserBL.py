from Dao import EndUserDao
from Dao import HealthDataDao


class EndUserBL(object):

    # This method adds enduser
    def create_end_user (self, enduserobj):
        try:
            return EndUserDao.EndUserDao().create(enduserobj)
        except Exception as e:
            raise

    # This method creates datum mapping enduser
    def create_user_datum_mapping(self, datumobj):
        try:
            return HealthDataDao.HealthDataDao().create_datum_mapping(datumobj)
        except Exception as e:
            raise

    # This method reads enduser
    def read_end_user(self, myusername):
        my_read_list =[]
        try:
            myobj = EndUserDao.EndUserDao().read(myusername)
            my_read_list = HealthDataDao.HealthDataDao().read_datum(myusername)
            if (myobj is None) or (not my_read_list):
                return False
            else:
                myreturnlist = []
                myreturnlist.append(myobj)
                myreturnlist.append(my_read_list)
                return myreturnlist
        except Exception as e:
            raise

    # This method updates enduser
    def update_end_user(self, enduserobj):
        try:
            return EndUserDao.EndUserDao().update(enduserobj)
        except Exception as e:
            raise

    # This method updates datum
    def update_datum(self, datumobj):
        try:
            return HealthDataDao.HealthDataDao().update_datum(datumobj)
        except Exception as e:
            raise