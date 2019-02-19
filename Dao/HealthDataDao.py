import mysql.connector
from Entities import Entities


class HealthDataDao(object):
    def create_property(self, obj_to_add):
        # cursor = MySingletonConnection.MySingletonConnection().get_instance().cursor()
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute("insert into smarthealthdb.property values(%s, %s, %s)",
                           (obj_to_add.propertyid, obj_to_add.name, obj_to_add.description))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def create_datum_mapping(self,obj_to_add):
        # cursor = MySingletonConnection.MySingletonConnection().get_instance().cursor()
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute("insert into smarthealthdb.datum values(%s, %s, %s, %s, %s)",
                           (obj_to_add.datumid, obj_to_add.username, obj_to_add.propertyid, obj_to_add.value, obj_to_add.whensaved))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read_properties(self):
        mypropertylist = []
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            query = ("select * from smarthealthdb.property")
            cursor.execute(query)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
                for row in result:
                    myboj = Entities.Property(row[0], row[1], row[2])
                    mypropertylist.append(myboj)
                return mypropertylist
            else:
                return None
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read_datum(self,username):
        myflag = 0
        mydatumlist = []
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            query = ("select * from smarthealthdb.datum")
            cursor.execute(query)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
                for row in result:
                    if row[1] == username:
                        myflag = 1
                        myboj = Entities.Datum(row[0], row[1], row[2], row[3], row[4])
                        mydatumlist.append(myboj)
                if myflag == 0:
                    return None
                else:
                    return mydatumlist
            else:
                return None
        except Exception as e:
            raise
        finally:
            cursor.close()

    def update_datum(self, obj_to_update):
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute(
                "update smarthealthdb.datum set value = %s where datumid = %s",
                (
                    obj_to_update.value, obj_to_update.datumid))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()