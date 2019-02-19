import Entities, BusinessLogic, datetime
from Entities import Entities
from BusinessLogic import DiscussionForumLogic


def call(username):
    print('Welcome Moderator to the discussion forum!!')
    #username = input('Please enter your user name: ')
    choice1 = int(input('1. Create a forum      2. Drop a forum'))
    business_logic = DiscussionForumLogic.DiscussionForumLogic()
    if choice1 == 1:
        forumid = int(input('Give a unique forum id to your forum: '))
        topic = input('What would be its topic: ')
        url = input('Enter URL')
        summary = input('Summarise your topic: ')
        whencreated = datetime.datetime.now()
        whenclosed = None
        createdbymoderator_username = username
        deletedbymoderator_username = None
        forum_object = Entities.Forum(forumid, topic, url, summary, whencreated, whenclosed, createdbymoderator_username,
                                      deletedbymoderator_username)
        forum_created = business_logic.create_forum(forum_object)
        if forum_created:
            print('Forum Created!!')
        else:
            print('Either moderator does not exist or forum id is not unique!!')
    elif choice1 == 2:
        forumid = int(input('Enter the forum id you want to remove from system: '))
        forum_removed = business_logic.remove_forum(forumid, username)
        if forum_removed:
            print('Forum is removed!!')
        else:
            print('Either moderator or forum id does not exist!!')
