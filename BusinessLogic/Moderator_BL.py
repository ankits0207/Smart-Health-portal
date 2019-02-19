from Dao import ModeratorDao


class ModeratorBL(object):

    # This method creates mod
    def create_moderator (self, modobj, qual_list):
        try:
            ModeratorDao.ModeratorDao().create(modobj)
            for q in qual_list:
                ModeratorDao.ModeratorDao().add_qual(modobj,q)
        except Exception as e:
            raise

    # This method reads mod
    def read_moderator(self, myusername):
        try:
            retlist = []
            mymod = ModeratorDao.ModeratorDao().read(myusername)
            myqual = ModeratorDao.ModeratorDao().read_qual(myusername)
            if (mymod is None) or (not myqual):
                return False
            else:
                retlist.append(mymod)
                retlist.append(myqual)
                return retlist
        except Exception as e:
            raise

    # This method updates mod
    def update_moderator(self, modobj):
        try:
            return ModeratorDao.ModeratorDao().update(modobj)
        except Exception as e:
            raise

    # This method updates qual
    def update_qual(self, modobj, qual_list):
        try:
            ModeratorDao.ModeratorDao().delete_qual(modobj)
            for q in qual_list:
                ModeratorDao.ModeratorDao().add_qual(modobj,q)
        except Exception as e:
            raise