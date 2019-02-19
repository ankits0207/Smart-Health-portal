import Entities
import datetime
import Dao
from Entities import Entities
from Dao import FriendshipDAO, EndUserDao


class SocialNetworkingLogic:
    #returns false if either requester or requested user does not exist.
    def send_request(self, requester_username, requested_username):
        friendship_object = Entities.Friendship(requester_username, requested_username, datetime.datetime.now(), None,
                                                None, None, None)
        friendship_dao = FriendshipDAO.FriendshipDAO()
        enduser_dao = EndUserDao.EndUserDao()
        request_sent = False
        requester_existence = enduser_dao.read(requester_username)
        requested_existence = enduser_dao.read(requested_username)
        if requester_existence != None and requested_existence != None:
            friendship_existing = friendship_dao.read(requester_username, requested_username)
            if friendship_existing == None:
                request_sent = friendship_dao.create(friendship_object)
            else:
                friendship_existing.when_requested = datetime.datetime.now()
                friendship_existing.when_rejected = None
                friendship_existing.when_confirmed = None
                friendship_existing.when_unfriended = None
                friendship_existing.when_withdrawn = None
                friendship_dao.update(friendship_existing)
                request_sent = True
        return request_sent


    #returns true if request is accepted, false if friend request does not exist.
    def accept_request(self, requester_username, requested_username):
        friendship_accepted = False
        friendship_dao = FriendshipDAO.FriendshipDAO()
        friendship_object_to_update = friendship_dao.read(requester_username,requested_username)
        if friendship_object_to_update != None:
            friendship_object_to_update.when_confirmed = datetime.datetime.now()
            friendship_accepted = friendship_dao.update(friendship_object_to_update)
        return friendship_accepted

    #returns all the friend requests that a particular end user has, None if there is no data in friendship table
    def return_my_friend_requests(self, my_username):
        friendship_dao = FriendshipDAO.FriendshipDAO()
        return friendship_dao.return_all_my_friend_requests(my_username)


    #returns true if request is declined, false if friend request does not exist or if request is already accepted
    def decline_request(self, requester_username, requested_username):
        request_declined = False
        friendship_dao = FriendshipDAO.FriendshipDAO()
        friendship_object_to_update = friendship_dao.read(requester_username,requested_username)
        if friendship_object_to_update != None:
            if friendship_object_to_update.when_confirmed == None:
                friendship_object_to_update.when_rejected = datetime.datetime.now()
                request_declined = friendship_dao.update(friendship_object_to_update)
        return request_declined


    #returns true if unfriended, false if both users are not friends
    def unfirend(self, requester_username, requested_username):
        unfriended = False
        friendship_dao = FriendshipDAO.FriendshipDAO()
        friendship_object_to_update = friendship_dao.read(requester_username, requested_username)
        if friendship_object_to_update != None:
            if friendship_object_to_update.when_confirmed != None and friendship_object_to_update.when_rejected == None:
                friendship_object_to_update.when_unfriended = datetime.datetime.now()
                unfriended = friendship_dao.update(friendship_object_to_update)
        else:
            friendship_object_to_update = friendship_dao.read(requested_username, requester_username)
            if friendship_object_to_update != None:
                if friendship_object_to_update.when_confirmed != None and friendship_object_to_update.when_rejected == None:
                    friendship_object_to_update.when_unfriended = datetime.datetime.now()
                    unfriended = friendship_dao.update(friendship_object_to_update)
        return unfriended


    #return list of my friends
    def return_my_friends(self, my_username):
        friendship_dao = FriendshipDAO.FriendshipDAO()
        return friendship_dao.return_my_friends(my_username)

