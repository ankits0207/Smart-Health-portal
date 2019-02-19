from Entities import Entities
import mysql.connector

class RatingDAO:
    def create(self, object_to_add):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor();
        try:
            cursor.execute("insert into smarthealthdb.rating values "
                           "(%s, %s, %s, %s)", (object_to_add.post_username,
                                                object_to_add.post_timecreated, object_to_add.rater_username,
                                                object_to_add.stars))
            connection.commit()
            return True
        except Exception as e:
            raise
        finally:
            cursor.close()


    def read(self, post_username, post_timecreated, rater_username):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.rating where post_username = %s "
                           "and post_timecreated = %s and rater_username = %s", (post_username, post_timecreated, rater_username))
            results = cursor.fetchall()
            rating_row = None
            if cursor.rowcount == 1:
                for row in results:
                    post_username = row[0]
                    post_timecreated = row[1]
                    rater_username = row[2]
                    stars = row[3]
                    rating_row = Entities.Rating(post_username, post_timecreated, rater_username, stars)
            connection.commit()
            return rating_row
        except Exception as e:
            raise
        finally:
            cursor.close()

    def return_ratings_for_a_post(self, post_username, post_timecreated):
        connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', database='smarthealthdb')
        cursor = connection.cursor()
        try:
            cursor.execute("select * from smarthealthdb.rating where post_username = %s "
                           "and post_timecreated = %s",
                           (post_username, post_timecreated))
            results = cursor.fetchall()
            ratings = []
            row_count = cursor.rowcount
            if row_count > 0:
                for row in results:
                    post_username = row[0]
                    post_timecreated = row[1]
                    rater_username = row[2]
                    stars = row[3]
                    rating_row = Entities.Rating(post_username, post_timecreated, rater_username, stars)
                    ratings.append(rating_row)
            connection.commit()
            return ratings
        except Exception as e:
            raise
        finally:
            cursor.close()
