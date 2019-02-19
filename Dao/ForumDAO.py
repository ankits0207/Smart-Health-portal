from Entities import Entities
import mysql.connector


class ForumDAO(object):
    def create(self, object_to_add):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("insert into smarthealthdb.forum values (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (object_to_add.forumid, object_to_add.topic, object_to_add.url,
                            object_to_add.summary, object_to_add.whencreated,
                            object_to_add.whenclosed, object_to_add.createdbymoderator_username,
                            object_to_add.deletedbymoderator_username))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def update(self, object_to_update):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("update smarthealthdb.forum set forumid = %s, topic = %s, url = %s, summary = %s, whencreated = %s, whenclosed = %s, createdbymoderator_username = %s, "
                           "deletedbymoderator_username = %s where forumid = %s",
                           (object_to_update.forumid, object_to_update.topic, object_to_update.url,
                            object_to_update.summary, object_to_update.whencreated,
                            object_to_update.whenclosed, object_to_update.createdbymoderator_username,
                            object_to_update.deletedbymoderator_username, object_to_update.forumid))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read(self, forumid):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.forum")
            results = cursor.fetchall()
            forum_row = None
            if cursor.rowcount >= 1:
                for row in results:
                    got_forumid = row[0]
                    topic = row[1]
                    url = row[2]
                    summary = row[3]
                    whencreated = row[4]
                    whenclosed = row[5]
                    createdbymoderator_username = row[6]
                    deletedbymoderator_username = row[7]
                    if forumid == got_forumid:
                        forum_row = Entities.Forum(forumid, topic, url, summary, whencreated, whenclosed, createdbymoderator_username, deletedbymoderator_username)
            connection.commit()
            return forum_row
        except Exception as e:
            raise
        finally:
            cursor.close()

    def return_all_forums(self):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.forum")
            results = cursor.fetchall()
            all_forums = []
            if cursor.rowcount >= 1:
                for row in results:
                    forumid = row[0]
                    topic = row[1]
                    url = row[2]
                    summary = row[3]
                    whencreated = row[4]
                    whenclosed = row[5]
                    createdbymoderator_username = row[6]
                    deletedbymoderator_username = row[7]
                    forum_row = Entities.Forum(forumid, topic, url, summary, whencreated, whenclosed,
                                                   createdbymoderator_username, deletedbymoderator_username)
                    all_forums.append(forum_row)
            connection.commit()
            return all_forums
        except Exception as e:
            raise
        finally:
            cursor.close()

