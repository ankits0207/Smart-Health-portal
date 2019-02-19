from Entities import Entities
import mysql.connector


class AdministratorDao(object):
    def create(self, obj_to_add):
        # cursor = MySingletonConnection.MySingletonConnection().get_instance().cursor()
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute("insert into smarthealthdb.administrator values(%s, %s)",
                           (obj_to_add.username, obj_to_add.phone))
            cursor.execute(
                "insert into smarthealthdb.user values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    obj_to_add.username, obj_to_add.password, obj_to_add.email1, obj_to_add.email2,
                    obj_to_add.firstname,
                    obj_to_add.lastname, obj_to_add.aboutme, obj_to_add.photourl1, obj_to_add.photourl2,
                    obj_to_add.photourl3,
                    obj_to_add.streetnumber, obj_to_add.streetname, obj_to_add.majormunicipality,
                    obj_to_add.governingdistrict,
                    obj_to_add.postalarea, obj_to_add.usertypeid, obj_to_add.status))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read(self, username):
        myflag = 0
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor(buffered=True)
        try:
            query = "select a.*,b.phone from smarthealthdb.user a join smarthealthdb.administrator b on a.username=b.username"
            cursor.execute(query)
            if cursor.rowcount > 0:
                result = cursor.fetchall()
                for row in result:
                    if row[0] == username:
                        read_username = row[0]
                        read_password = row[1]
                        read_email1 = row[2]
                        read_email2 = row[3]
                        read_firstname = row[4]
                        read_lastname = row[5]
                        read_aboutme = row[6]
                        read_photourl1 = row[7]
                        read_photourl2 = row[8]
                        read_photourl3 = row[9]
                        read_street_num = row[10]
                        read_street_name = row[11]
                        read_majormunicipality = row[12]
                        read_governing_district = row[13]
                        read_postal_area = row[14]
                        read_user_type_id = row[15]
                        read_status = row[16]
                        read_phone = row[17]
                        myflag = 1
                if myflag == 1:
                    read_obj = Entities.Administrator(read_phone, read_username, read_password,
                                            read_email1, read_email2, read_firstname, read_lastname, read_aboutme,
                                            read_photourl1, read_photourl2, read_photourl3, read_street_num,
                                            read_street_name, read_majormunicipality, read_governing_district,
                                            read_postal_area, read_user_type_id, read_status)
                    return read_obj
                else:
                    return None
            else:
                return None
        except Exception as e:
            raise
        finally:
            cursor.close()

    def update(self, obj_to_update):
        con = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = con.cursor()
        try:
            cursor.execute(
                "update smarthealthdb.administrator set phone = %s where username = %s",
                (
                    obj_to_update.phone, obj_to_update.username))
            cursor.execute(
                "update smarthealthdb.user set password = %s, email1 = %s, email2 = %s, firstname = %s, lastname = %s, aboutme = %s, photourl1 = %s, photourl2 = %s, photourl3 = %s, streetnumber = %s, streetname = %s, majormunicipality = %s, governingdistrict = %s, postalarea = %s, status = %s where username = %s",
                (
                    obj_to_update.password, obj_to_update.email1, obj_to_update.email2,
                    obj_to_update.firstname,
                    obj_to_update.lastname, obj_to_update.aboutme, obj_to_update.photourl1, obj_to_update.photourl2,
                    obj_to_update.photourl3,
                    obj_to_update.streetnumber, obj_to_update.streetname, obj_to_update.majormunicipality,
                    obj_to_update.governingdistrict,
                    obj_to_update.postalarea, obj_to_update.status, obj_to_update.username))
            con.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()
