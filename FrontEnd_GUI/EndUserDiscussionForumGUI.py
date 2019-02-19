from tkinter import *
import BusinessLogic, Entities, datetime
from Entities import Entities
from BusinessLogic import DiscussionForumLogic


business_logic = DiscussionForumLogic.DiscussionForumLogic()

def call(username):
    def display_forums():
        master_display = Tk()
        listbox = Listbox(master_display, width=100, height=100)
        listbox.pack()
        forums = business_logic.return_all_forums()
        i = 0
        for forum in forums:
            i += 1
            listbox.insert(END, "Forum "+str(i)+" details: ")
            listbox.insert(END, "Forum id: "+str(forum.forumid))
            listbox.insert(END, "Forum Topic: "+forum.topic)
            listbox.insert(END, "Forum Summary: "+forum.summary)
        listbox.insert(END, "You can now post your views on any of these")


    def post_forum():
        forumid = int(forum_id.get())
        timecreated = datetime.datetime.now()
        text = forum_text.get()
        photolocation = photo_location.get()
        linklocation = link_location.get()
        videolocation = video_location.get()
        post_object = Entities.Post(username, timecreated, forumid, text, photolocation, linklocation, videolocation)
        post_created = business_logic.create_post(post_object)
        if post_created is True:
            Label(master, text="Posted!!").grid(row=7, column=4)
        else:
            Label(master, text="Could no Post, check forum id!!").grid(row=7, column=4)


    def view_posts():
        forumid = int(forum_id_post.get())
        all_posts = business_logic.return_all_posts_given_forum(forumid)
        master_view_posts = Tk()
        listbox = Listbox(master_view_posts, width=100, height=100)
        listbox.pack()
        i = 0
        for post in all_posts:
            i += 1
            listbox.insert(END, "Post " + str(i) + " details: ")
            listbox.insert(END, "Posted By: " + post.username)
            listbox.insert(END, "User wrote: "+post.textentry)
            listbox.insert(END, 'Created At: ' + str(post.timecreated))
            listbox.insert(END, "Photo attached: " + str(post.photolocation))
            listbox.insert(END, "References: " + str(post.linklocation))
            listbox.insert(END, "Video attached: " + str(post.videolocation))
            listbox.insert(END, "")
        listbox.insert(END, "You can now comment on any of these!!")


    def comment():
        post_username_text = post_username.get()
        date_input_text = date_input.get()
        post_timecreated = datetime.datetime.strptime(date_input_text, '%Y-%m-%d %H:%M:%S')
        commenttime = datetime.datetime.now()
        commenttext = comment_text.get()
        photolocation = photo_location_comment.get()
        linklocation = link_location_comment.get()
        videolocation = video_location_comment.get()
        comment_object = Entities.Comment(post_username_text, post_timecreated, username, commenttime, commenttext,
                                          photolocation, linklocation, videolocation)
        comment_created = business_logic.create_comment(comment_object)
        if comment_created is True:
            Label(master, text="Comment Created!!").grid(row=17, column=4)
        else:
            Label(master, text="Sorry, post does not exist. Please refer to view all posts option!!").grid(row=17, column=4)


    def give_rating():
        post_username = post_username_rating.get()
        post_timecreated = datetime.datetime.strptime(date_input_rating.get(), '%Y-%m-%d %H:%M:%S')
        rating_object = Entities.Rating(post_username, post_timecreated, username, int(stars.get()))
        if business_logic.give_rating_to_post(rating_object):
            Label(master, text="Your rating has been recorded, you can check average rating as well below!!").grid(row=22,
                                                                                                                   column=4)
        else:
            Label(master, text="Sorry, post does not exist. Please refer to view all posts option!!").grid(row=22, column=4)


    def view_average():
        post_username = post_username_average.get()
        post_timecreated = datetime.datetime.strptime(date_input_average.get(), '%Y-%m-%d %H:%M:%S')
        average = business_logic.give_average(post_username, post_timecreated)
        Label(master, text="Average of this post is: "+str(average)).grid(row=25, column=4)


    def view_comments():
        post_username = post_username_comments.get()
        post_timecreated = datetime.datetime.strptime(date_input_comments.get(), '%Y-%m-%d %H:%M:%S')
        comments = business_logic.return_all_comments_for_given_post(post_username, post_timecreated)
        master_view_comments = Tk()
        listbox = Listbox(master_view_comments, width=100, height=100)
        listbox.pack()
        i = 0
        for comment in comments:
            i += 1
            listbox.insert(END, "Comment " + str(i) + " details: ")
            listbox.insert(END, "Commenter user name: " + comment.commenter_username)
            listbox.insert(END, "User wrote: " + comment.commenttext)
            listbox.insert(END, "References: " + str(comment.linklocation))
            listbox.insert(END, "Video attached: " + str(comment.videolocation))
            listbox.insert(END, "Photo attached: " + str(comment.photolocation))
            listbox.insert(END, "")


    master = Tk()
    Label(master, text="****Welcome "+username+" to Discussion forum****").grid(row=0, column=2)
    Button(master, text="Click here to have a brief look at all forums", command=display_forums).grid(row=1, column=2)

    Label(master, text="****Post on a forum****").grid(row=2, column=2)
    Label(master, text="Enter forum id you want to post on: ").grid(row=3, column=1)
    forum_id = Entry(master)
    forum_id.grid(row=3, column=2)
    Label(master, text="Enter text of your post: ").grid(row=4, column=1)
    forum_text = Entry(master)
    forum_text.grid(row=4, column=2)
    Label(master, text="Enter photo location: ").grid(row=5, column=1)
    photo_location = Entry(master)
    photo_location.grid(row=5, column=2)
    Label(master, text="Want to attach any references? paste link here: ").grid(row=6, column=1)
    link_location = Entry(master)
    link_location.grid(row=6, column=2)
    Label(master, text="Video url here: ").grid(row=7, column=1)
    video_location = Entry(master)
    video_location.grid(row=7, column=2)
    Button(master, text="post", command=post_forum).grid(row=7, column=3)

    Label(master, text="****View posts in a forum****").grid(row=9, column=2)
    Label(master, text="Enter forum id you of which you want to see the posts(integer value): ").grid(row=10, column=1)
    forum_id_post = Entry(master)
    forum_id_post.grid(row=10, column=2)
    Button(master, text="view posts", command=view_posts).grid(row=10, column=3)

    Label(master, text="****Comment on a post****").grid(row=11, column=2)
    Label(master, text="Enter the user name whose post you want to comment on: ").grid(row=12, column=1)
    post_username = Entry(master)
    post_username.grid(row=12, column=2)
    Label(master, text="When was it created? ").grid(row=13, column=1)
    date_input = Entry(master)
    date_input.grid(row=13, column=2)
    Label(master, text="Write your comment now: ").grid(row=14, column=1)
    comment_text = Entry(master)
    comment_text.grid(row=14, column=2)
    Label(master, text="Enter photo location: ").grid(row=15, column=1)
    photo_location_comment = Entry(master)
    photo_location_comment.grid(row=15, column=2)
    Label(master, text="Want to attach any references? paste link here: ").grid(row=16, column=1)
    link_location_comment = Entry(master)
    link_location_comment.grid(row=16, column=2)
    Label(master, text="Video url here: ").grid(row=17, column=1)
    video_location_comment = Entry(master)
    video_location_comment.grid(row=17, column=2)
    Button(master, text="comment", command=comment).grid(row=17, column=3)

    Label(master, text="****Give rating to a post****").grid(row=18, column=2)
    Label(master, text="Enter the user name whose post you want to rate: ").grid(row=19, column=1)
    post_username_rating = Entry(master)
    post_username_rating.grid(row=19, column=2)
    Label(master, text="When was it created? ").grid(row=20, column=1)
    date_input_rating = Entry(master)
    date_input_rating.grid(row=20, column=2)
    Label(master, text="Give rating out of 5: ").grid(row=22, column=1)
    stars = Entry(master)
    stars.grid(row=22, column=2)
    Button(master, text="give rating", command=give_rating).grid(row=22, column=3)

    Label(master, text="****View average of a post****").grid(row=23, column=2)
    Label(master, text="Enter the user name whose post you want to rate: ").grid(row=24, column=1)
    post_username_average = Entry(master)
    post_username_average.grid(row=24, column=2)
    Label(master, text="When was it created? ").grid(row=25, column=1)
    date_input_average = Entry(master)
    date_input_average.grid(row=25, column=2)
    Button(master, text="view average", command=view_average).grid(row=25, column=3)

    Label(master, text="****View comments on a post****").grid(row=26, column=2)
    Label(master, text="Enter the user name whose post you want to rate: ").grid(row=27, column=1)
    post_username_comments = Entry(master)
    post_username_comments.grid(row=27, column=2)
    Label(master, text="When was it created? ").grid(row=28, column=1)
    date_input_comments = Entry(master)
    date_input_comments.grid(row=28, column=2)
    Button(master, text="view comments", command=view_comments).grid(row=28, column=3)

    master.mainloop()
