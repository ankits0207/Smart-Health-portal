from Entities import Entities
import mysql.connector

class CommentDAO:
    def create(self, object_to_add):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("insert into smarthealthdb.comment values "
                           "(%s, %s, %s, %s, %s, %s, %s, %s)", (object_to_add.post_username, object_to_add.post_timeCreated,
                                                                object_to_add.commenter_username, object_to_add.commenttime,
                                                                object_to_add.commenttext, object_to_add.photolocation,
                                                                object_to_add.linklocation, object_to_add.videolocation))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read_comments_of_post(self, post_username, post_timecreated):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        comments = []
        try:
            cursor.execute("select * from smarthealthdb.comment")
            results = cursor.fetchall()
            if cursor.rowcount >= 1:
                for row in results:
                    got_post_username = row[0]
                    got_post_timeCreated = row[1]
                    commenter_username = row[2]
                    commenttime = row[3]
                    commenttext = row[4]
                    photolocation = row[5]
                    linklocation = row[6]
                    videolocation = row[7]
                    if post_username == got_post_username and post_timecreated == got_post_timeCreated:
                        comment_object = Entities.Comment(post_username, post_timecreated, commenter_username, commenttime, commenttext, photolocation, linklocation, videolocation)
                        comments.append(comment_object)
            return comments
        except Exception as e:
            raise
        finally:
            cursor.close()