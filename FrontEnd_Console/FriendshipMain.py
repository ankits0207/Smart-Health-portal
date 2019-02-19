from Dao import HealthDataDao
from BusinessLogic import SocialNetworkingLogic

def call(username):
    print('Manage your friends from here!!')
    business_logic = SocialNetworkingLogic.SocialNetworkingLogic()
    #username = input('Enter your username please: ')
    choice1 = int(input('1. Display my friends    2. Send friend request to someone   '
                        '3. Display pending requests     4. Accept friend request   5. Decline friend request    '
                        ' 6. Un-friend someone      7. View health data of your friend '
                        '8. Exit social networking portal'))
    if choice1 == 1:
        my_friends = business_logic.return_my_friends(username)
        i = 0
        print('Following are your friends: ')
        for friend in my_friends:
            i += 1
            if username == friend.requester_username:
                print(str(i) + '. ' + friend.requested_username)
            elif username == friend.requested_username:
                print(str(i) + '. ' + friend.requester_username)
    elif choice1 == 2:
        requested_username = input('Enter username you want to befriend with: ')
        sent = business_logic.send_request(username, requested_username)
        if sent:
            print('Friend request is sent.')
        else:
            print('Either your or yours to be friend''s username is incorrect!!')
    elif choice1 == 3:
        my_pending_requests = business_logic.return_my_friend_requests(username)
        i = 0
        for pending_request in my_pending_requests:
            i += 1
            print(str(i) + '. ' + pending_request.requester_username)
    elif choice1 == 4:
        requester_username = input('Enter the username of the person whose friend request you want to accept: ')
        accepted = business_logic.accept_request(requester_username, username)
        if accepted:
            print('Friend request accepted!!')
        else:
            print('Request does not exist!!')
    elif choice1 == 5:
        requester_username = input('Enter the username of the person whose friend request you want to reject: ')
        rejected = business_logic.decline_request(requester_username, username)
        if rejected:
            print('Friend request rejected!!')
        else:
            print('Request does not exist!!')
    elif choice1 == 6:
        friend_username = input('Enter username of your ''to be ex-friend:'' ')
        unfriended = business_logic.unfirend(username,friend_username)
        if unfriended:
            print('You are no longer friends with '+friend_username)
        else:
            print('You already are not friends with '+friend_username)
    elif choice1 == 7:
        print('Here is the health data of all your active friends: ')
        health_dao = HealthDataDao.HealthDataDao()
        my_friends = business_logic.return_my_friends(username)
        for friend in my_friends:
            if friend.requester_username == username:
                mydatumlist = health_dao.read_datum(friend.requested_username)
                for datum in mydatumlist:
                    print('Property id: '+str(datum.propertyid)+'     Value: '+str(datum.value))
            elif friend.requested_username == username:
                mydatumlist = health_dao.read_datum(friend.requester_username)
                for datum in mydatumlist:
                    print('Property id: ' + str(datum.propertyid) + '     Value: ' + str(datum.value))
        print('***********************************************')
        properties = health_dao.read_properties()
        for property in properties:
            print('Property id: '+str(property.propertyid)+', Name: '+property.name+', Description: '+property.description)