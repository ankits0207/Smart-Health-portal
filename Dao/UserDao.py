import mysql.connector


class UserDao(object):
    def check_if_user_exists(self, username):
        exists = False
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            cursor.execute("select * from smarthealthdb.user")
            con.commit()
            results = cursor.fetchall()
            if cursor.rowcount > 0:
                for row in results:
                    got_username = row[0]
                    if got_username == username:
                        exists = True
            return exists
        except Exception as e:
            raise
        finally:
            cursor.close()

    def login(self, username, password):
        exists = False
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            cursor.execute("select * from smarthealthdb.user")
            con.commit()
            results = cursor.fetchall()
            if cursor.rowcount > 0:
                for row in results:
                    got_username = row[0]
                    got_password = row[1]
                    if got_username == username and got_password == password:
                        return row[15]
            return exists
        except Exception as e:
            raise
        finally:
            cursor.close()