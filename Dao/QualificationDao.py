import mysql.connector
from Entities import Entities

class QualificationDao(object):
    def create(self, obj_to_add):
        # cursor = MySingletonConnection.MySingletonConnection().get_instance().cursor()
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute("insert into smarthealthdb.qualification values(%s, %s)",
                           (obj_to_add.qualificationid, obj_to_add.description))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def readall(self):
        mylist = []
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            query = ("select * from smarthealthdb.qualification")
            cursor.execute(query)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
                for row in result:
                    mylist.append(Entities.Qualification(row[0],row[1]))
                return mylist
            else:
                return None
        except Exception as e:
            raise
        finally:
            cursor.close()

    def is_present(self, id_to_be_checked):
        myflag = 0
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            query = ("select qualificationid from smarthealthdb.qualification")
            cursor.execute(query)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
                for row in result:
                    if row[0] == id_to_be_checked:
                        myflag = 1
                if myflag == 1:
                    return True
                else:
                    return False
            else:
                return None
        except Exception as e:
            raise
        finally:
            cursor.close()
