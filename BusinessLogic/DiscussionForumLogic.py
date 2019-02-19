import Dao, Entities, datetime
from Dao import ModeratorDao, ForumDAO, PostDAO, CommentDAO, RatingDAO, UserDao


class DiscussionForumLogic(object):
    #returns true if a forum is created, false if forum id already exists or moderator is invalid.
    def create_forum(self, forum_object):
        forum_created = False
        forum_dao = ForumDAO.ForumDAO()
        moderator_dao = ModeratorDao.ModeratorDao()
        forum_existing = forum_dao.read(forum_object.forumid)
        if forum_existing == None:
            moderator_exists = moderator_dao.read(forum_object.createdbymoderator_username)
            if moderator_exists != None:
                forum_created = forum_dao.create(forum_object)
        return forum_created

    #returns true if a forum is deleted, false if forum does not exist or moderator is invalid.
    def remove_forum(self, forum_id, moderator_username):
        forum_deleted = False
        forum_dao = ForumDAO.ForumDAO()
        moderator_dao = ModeratorDao.ModeratorDao()
        forum_existing = forum_dao.read(forum_id)
        if forum_existing != None:
            moderator_exists = moderator_dao.read(moderator_username)
            if moderator_exists != None:
                forum_existing.deletedbymoderator_username = moderator_username
                forum_existing.whenclosed = datetime.datetime.now()
                forum_deleted = forum_dao.update(forum_existing)
        return forum_deleted

    #returns true if post is created, false if forum does not exist or if username is invalid
    def create_post(self, post_object):
        post_created = False
        forum_dao = ForumDAO.ForumDAO()
        post_dao = PostDAO.PostDAO()
        user_dao = UserDao.UserDao()
        forum_existing = forum_dao.read(post_object.forumid)
        if forum_existing != None:
            if (user_dao.check_if_user_exists(post_object.username) == True):
                post_created = post_dao.create(post_object)
        return post_created

    #returns true if comment is created, false is post does not exist or commenter is invalid
    def create_comment(self, comment_object):
        comment_created = False
        comment_dao = CommentDAO.CommentDAO()
        post_dao = PostDAO.PostDAO()
        user_dao = UserDao.UserDao()
        post_existing = post_dao.read(comment_object.post_username, comment_object.post_timeCreated)
        if post_existing != None:
            if (user_dao.check_if_user_exists(comment_object.commenter_username) == True):
                comment_created = comment_dao.create(comment_object)
        return comment_created

    #returns true if rating is given, false if post does not exist or rater is invalid
    def give_rating_to_post(self, rating_object):
        rating_given = False
        rating_dao = RatingDAO.RatingDAO()
        post_dao = PostDAO.PostDAO()
        user_dao = UserDao.UserDao()
        post_existing = post_dao.read(rating_object.post_username, rating_object.post_timecreated)
        if post_existing != None:
            if (user_dao.check_if_user_exists(rating_object.rater_username) == True):
                rating_given = rating_dao.create(rating_object)
        return rating_given

    #returns average of a post
    def give_average(self, post_username, post_timecreated):
        rating_dao = RatingDAO.RatingDAO()
        ratings = rating_dao.return_ratings_for_a_post(post_username, post_timecreated)
        count = 0
        sum = 0
        for rating in ratings:
            count += 1
            sum += rating.stars
        average_rating = 0
        if count > 0:
            average_rating = sum/count
        return average_rating

    def return_all_forums(self):
        return ForumDAO.ForumDAO().return_all_forums()

    def return_all_posts_given_forum(self, forumid):
        return PostDAO.PostDAO().return_all_posts_for_a_forum(forumid)

    def return_all_comments_for_given_post(self, post_username, post_timecreated):
        post_dao = PostDAO.PostDAO()
        post_existing = post_dao.read(post_username, post_timecreated)
        if post_existing != None:
            return CommentDAO.CommentDAO().read_comments_of_post(post_username=post_username, post_timecreated=post_timecreated)
