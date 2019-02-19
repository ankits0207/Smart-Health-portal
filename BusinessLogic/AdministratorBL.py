from Dao import AdministratorDao
from Dao import QualificationDao
from Dao import HealthDataDao

class AdministratorBL(object):

    #This method creates an admin
    def create_administrator (self, adminobj):
        try:
            return AdministratorDao.AdministratorDao().create(adminobj)
        except Exception as e:
            raise

    # This method reads an admin
    def read_administrator(self, myusername):
        try:
            return AdministratorDao.AdministratorDao().read(myusername)
        except Exception as e:
            raise

    # This method updates an admin
    def update_administrator(self, adminobj):
        try:
            return AdministratorDao.AdministratorDao().update(adminobj)
        except Exception as e:
            raise

    # This method adds qual for mod
    def add_qual(self, qualobj):
        try:
            return QualificationDao.QualificationDao().create(qualobj)
        except Exception as e:
            raise

    # This method adds property for enduser
    def add_property(self, propobj):
        try:
            return HealthDataDao.HealthDataDao().create_property(propobj)
        except Exception as e:
            raise
