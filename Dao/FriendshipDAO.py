from Entities import Entities
import mysql.connector


class FriendshipDAO(object):
    def create(self, object_to_add):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("insert into smarthealthdb.friendship values (%s, %s, %s, %s, %s, %s, %s)",
                           (object_to_add.requester_username,
                            object_to_add.requested_username, object_to_add.when_requested,
                            object_to_add.when_withdrawn,
                            object_to_add.when_rejected, object_to_add.when_confirmed, object_to_add.when_unfriended))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def update(self, object_to_update):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute(
                "update smarthealthdb.friendship set requester_username = %s, requested_username = %s, whenrequested = %s, "
                "whenwithdrawn = %s, whenrejected = %s, whenconfirmed = %s, whenunfriended = %s "
                "where requester_username = %s and requested_username = %s",
                (object_to_update.requester_username,
                 object_to_update.requested_username, object_to_update.when_requested,
                 object_to_update.when_withdrawn,
                 object_to_update.when_rejected, object_to_update.when_confirmed, object_to_update.when_unfriended,
                 object_to_update.requester_username,object_to_update.requested_username))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()

    def read(self, requester_username, requested_username):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.friendship")
            friendship_row = None
            results = cursor.fetchall()
            if cursor.rowcount > 0:
                for row in results:
                    got_requester_username = row[0]
                    got_requested_username = row[1]
                    when_requested = row[2]
                    when_withdrawn = row[3]
                    when_rejected = row[4]
                    when_confirmed = row[5]
                    when_unfriended = row[6]
                    if requester_username == got_requester_username and requested_username == got_requested_username:
                        friendship_row = Entities.Friendship(requester_username,requested_username,when_requested,when_withdrawn,
                                            when_rejected,when_confirmed,when_unfriended)
            connection.commit()
            return friendship_row
        except Exception as e:
            raise
        finally:
            cursor.close()


    def return_all_my_friend_requests(self, my_username):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.friendship")
            my_friendship_requests = []
            results = cursor.fetchall()
            if cursor.rowcount >= 1:
                for row in results:
                    requester_username = row[0]
                    requested_username = row[1]
                    when_requested = row[2]
                    when_withdrawn = row[3]
                    when_rejected = row[4]
                    when_confirmed = row[5]
                    when_unfriended = row[6]
                    if requested_username == my_username and when_confirmed == None and when_unfriended == None and when_rejected == None:
                        friendship_row = Entities.Friendship(requester_username, requested_username, when_requested,
                                                             when_withdrawn,
                                                             when_rejected, when_confirmed, when_unfriended)
                        my_friendship_requests.append(friendship_row)
            connection.commit()
            return my_friendship_requests
        except Exception as e:
            raise
        finally:
            cursor.close()

    def return_my_friends(self, my_username):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute(
                "select * from smarthealthdb.friendship")
            my_friendships = []
            results = cursor.fetchall()
            if cursor.rowcount >= 1:
                for row in results:
                    requester_username = row[0]
                    requested_username = row[1]
                    when_requested = row[2]
                    when_withdrawn = row[3]
                    when_rejected = row[4]
                    when_confirmed = row[5]
                    when_unfriended = row[6]
                    if (requester_username == my_username or requested_username == my_username) and when_unfriended == None and when_confirmed != None:
                        friendship_row = Entities.Friendship(requester_username, requested_username, when_requested,
                                                             when_withdrawn,
                                                             when_rejected, when_confirmed, when_unfriended)
                        my_friendships.append(friendship_row)
            connection.commit()
            return my_friendships
        except Exception as e:
            raise
        finally:
            cursor.close()
