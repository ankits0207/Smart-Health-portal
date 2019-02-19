import BusinessLogic, Entities, datetime
from Entities import Entities
from BusinessLogic import DiscussionForumLogic


def call(username):
    business_logic = DiscussionForumLogic.DiscussionForumLogic()
    print('Hi User, Welcome to the discussion forum!!')
    # username = input('Please enter your username: ')
    choice1 = int(input(
        '1.Have a brief look at all the forums     2. Post on a forum     3. View all posts in a forum      4. Comment on a post    5. Give rating to a post      '
        '6. View average of a post    7. View comments on a post     8.Exit discussion forum'))
    if choice1 == 1:
        print('Here are all the forums with')
        forums = business_logic.return_all_forums()
        for forum in forums:
            print('Forum Id: ' + str(forum.forumid) + ', Topic: ' + forum.topic + ', Summary: ' + forum.summary)
        print('You can now post your views on any of these, by choosing appropriate option from the menu!!')
    elif choice1 == 2:
        timecreated = datetime.datetime.now()
        forumid = int(input('Enter the forum id you want to post on: '))
        text = input('Write your post now: ')
        photolocation = None
        linklocation = input('Want to attach any references? paste link here:')
        videolocation = input('Video url here: ')
        post_object = Entities.Post(username, timecreated, forumid, text, photolocation, linklocation, videolocation)
        post_created = business_logic.create_post(post_object)
        if post_created:
            print('Post created!!')
        else:
            print('Invalid forum id or user name!!')
    elif choice1 == 3:
        forumid = int(input('Enter forum id you of which you want to see the posts(integer value): '))
        all_posts = business_logic.return_all_posts_given_forum(forumid)
        for post in all_posts:
            print('Posted By: ' + post.username + ', Created At: ' + str(
                post.timecreated) + ', User wrote: ' + post.textentry + ', '
                                                                        'photo attached: ' + str(
                post.photolocation) + ', References: ' + str(post.linklocation) + ', '
                                                                                  'Videos attached: ' + str(
                post.videolocation))
        print('You can now comment on any of these, by choosing appropriate option from the menu!!')
    elif choice1 == 4:
        print('Please enter details of the post on which you would like to comment on'
              '(you can refer the view all posts option from menu for details): ')
        post_username = input('Enter the user name whose post you want to comment on: ')
        date_input = input('When was it created? ')
        post_timecreated = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
        commenttime = datetime.datetime.now()
        commenttext = input('Write your comment now: ')
        photolocation = None
        linklocation = input('Want to attach any references? paste link here:')
        videolocation = input('Video url here: ')
        comment_object = Entities.Comment(post_username, post_timecreated, username, commenttime, commenttext,
                                          photolocation, linklocation, videolocation)
        comment_created = business_logic.create_comment(comment_object)
        if comment_created:
            print('Comment added to the post!!')
        else:
            print('Sorry, post does not exist. Please refer to view all posts option!!')
    elif choice1 == 5:
        print('Please enter details of the post for which you want to rate'
              '(you can refer the view all posts option from menu for details): ')
        post_username = input('Enter the user name whose post you want to rate: ')
        date_input = input('When was it created? ')
        post_timecreated = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
        stars = int(input('Give rating out of 5: '))
        rating_object = Entities.Rating(post_username, post_timecreated, username, stars)
        if business_logic.give_rating_to_post(rating_object):
            print('Your rating is recorded!!')
            print('You can check the average rating of the post from menu')
        else:
            print('Sorry, post does not exist. Please refer to view all posts option!!')
    elif choice1 == 6:
        print('Please enter details of the post of which you want to see the average rating'
              '(you can refer the view all posts option from menu for details): ')
        post_username = input('Enter the user name whose post you want to comment on: ')
        date_input = input('When was it created? ')
        post_timecreated = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
        average = business_logic.give_average(post_username, post_timecreated)
        print('Average of this post is: ' + str(average))
    elif choice1 == 7:
        print('Please enter details of the post whose comments you want to see'
              '(you can refer the view all posts option from menu for details): ')
        post_username = input('Enter the user name of the person who wrote the post: ')
        date_input = input('When was it created? ')
        post_timecreated = datetime.datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')
        comments = business_logic.return_all_comments_for_given_post(post_username, post_timecreated)
        for comment in comments:
            print(
                'Commenter user name: ' + comment.commenter_username + ', User wrote: ' + comment.commenttext + ', '
                                                                                                                'References: ' +
                str(comment.linklocation) + 'Videos attached: ' + str(comment.videolocation) + ', photo attached' + str(
                    comment.photolocation))
