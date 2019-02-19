import mysql.connector

class UtilityDao(object):
    def my_util(self):
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            #cursor.execute("delete from smarthealthdb.usertype")
            #cursor.execute("insert into smarthealthdb.usertype values(%s, %s)", ("1", "new"))
            #cursor.execute("insert into smarthealthdb.usertype values(%s, %s)", ("2", "mod"))
            #cursor.execute("insert into smarthealthdb.usertype values(%s, %s)", ("3", "admin"))
            #cursor.execute("insert into smarthealthdb.usertype values(%s, %s)", ("4", "middle"))
            #cursor.execute("insert into smarthealthdb.usertype values(%s, %s)", ("5", "old"))
            cursor.execute("update smarthealthdb.user set usertypeid = 4 where username IN (select username from smarthealthdb.enduser where month(curdate()) - month(datecreated) in (6))")
            cursor.execute("update smarthealthdb.user set usertypeid = 5 where username IN (select username from smarthealthdb.enduser where month(curdate()) - month(datecreated) in (12))")
            con.commit()
        except Exception as e:
            raise
        finally:
            cursor.close()