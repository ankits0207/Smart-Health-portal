from Entities import Entities
import mysql.connector


class PostDAO:
    def create(self, object_to_add):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("insert into smarthealthdb.post values "
                           "(%s, %s, %s, %s, %s, %s, %s )", (object_to_add.username, object_to_add.timecreated,
                                                              object_to_add.forumid,
                                                              object_to_add.textentry, object_to_add.photolocation,
                                                              object_to_add.linklocation,
                                                              object_to_add.videolocation))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read(self, username, timecreated):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from smarthealthdb.post")
            results = cursor.fetchall()
            forum_row = None
            if cursor.rowcount >= 1:
                for row in results:
                    got_username = row[0]
                    got_timecreated = row[1]
                    forumid = row[2]
                    textentry = row[3]
                    photolocation = row[4]
                    linklocation = row[5]
                    videolocation = row[6]
                    if got_username == username and got_timecreated == timecreated:
                        post_row = Entities.Post(username, timecreated, forumid, textentry, photolocation, linklocation, videolocation)
            connection.commit()
            return post_row
        except Exception as e:
            raise
        finally:
            cursor.close()

    def return_all_posts_for_a_forum(self, forumid):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from smarthealthdb.post")
            results = cursor.fetchall()
            all_posts = []
            if cursor.rowcount >= 1:
                for row in results:
                    username = row[0]
                    timecreated = row[1]
                    got_forumid = row[2]
                    textentry = row[3]
                    photolocation = row[4]
                    linklocation = row[5]
                    videolocation = row[6]
                    if got_forumid == forumid:
                        post_row = Entities.Post(username, timecreated, forumid, textentry, photolocation, linklocation,
                                             videolocation)
                        all_posts.append(post_row)
            connection.commit()
            return all_posts
        except Exception as e:
            raise
        finally:
            cursor.close()
