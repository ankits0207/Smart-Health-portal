from Entities import Entities
from BusinessLogic import DiscussionForumLogic
from tkinter import *
from datetime import datetime


business_logic = DiscussionForumLogic.DiscussionForumLogic()


def call(username):
    def create_forum():
        forumid = int(forum_id_create.get())
        topic = topic_create.get()
        url = url_create.get()
        summary = summary_create.get()
        whencreated = datetime.now()
        whenclosed = None
        createdbymoderator_username = username
        deletedbymoderator_username = None
        forum_object = Entities.Forum(forumid, topic, url, summary, whencreated, whenclosed, createdbymoderator_username,
                                      deletedbymoderator_username)
        forum_created = business_logic.create_forum(forum_object)
        if forum_created is True:
            Label(master, text="Forum Created!!").grid(row=6, column=4)
        else:
            Label(master, text="Either moderator does not exis or forum id is not unique!!").grid(row=6, column=4)


    def drop_forum():
        forumid = int(forum_id_drop.get())
        forum_removed = business_logic.remove_forum(forumid, username)
        if forum_removed:
            Label(master, text="Forum is removed!!").grid(row=9, column=4)
        else:
            Label(master, text="Either moderator or forum id does not exist!!").grid(row=9, column=4)

    master = Tk()
    Label(master, text="****Welcome "+username+" to Discussion forum****").grid(row=0, column=2)
    Label(master, text="").grid(row=1, column=2)
    Label(master, text="****Create A Forum****").grid(row=2, column=2)
    Label(master, text="Forum id(in integer): ").grid(row=3, column=1)
    forum_id_create = Entry(master)
    forum_id_create.grid(row=3, column=2)
    Label(master, text="URL: ").grid(row=4, column=1)
    url_create = Entry(master)
    url_create.grid(row=4, column=2)
    Label(master, text="Topic: ").grid(row=5, column=1)
    topic_create = Entry(master)
    topic_create.grid(row=5, column=2)
    Label(master, text="Summary: ").grid(row=6, column=1)
    summary_create = Entry(master)
    summary_create.grid(row=6, column=2)
    Button(master, text="create forum", command=create_forum).grid(row=6, column=3)

    Label(master, text="").grid(row=7, column=2)
    Label(master, text="Drop a forum").grid(row=8, column=2)
    Label(master, text="Forum id(integer value): ").grid(row=9, column=1)
    forum_id_drop = Entry(master)
    forum_id_drop.grid(row=9, column=2)
    Button(master, text="drop forum", command=drop_forum).grid(row=9, column=3)

    master.mainloop()
