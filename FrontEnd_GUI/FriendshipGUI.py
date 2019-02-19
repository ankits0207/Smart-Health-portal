from tkinter import *
from BusinessLogic import SocialNetworkingLogic
from Dao import HealthDataDao

business_logic = SocialNetworkingLogic.SocialNetworkingLogic()
def call(username):
    def display():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=30)
        listbox.pack()
        my_friends = business_logic.return_my_friends(username)
        if len(my_friends) == 0:
            listbox.insert(END, "Sorry, you do not have any friend :-(")
        else:
            listbox.insert(END, "Following are your friends:-")
            for friend in my_friends:
                if username == friend.requester_username:
                    listbox.insert(END, friend.requested_username)
                elif username == friend.requested_username:
                    listbox.insert(END, friend.requester_username)

    def sendreq():
        requested_username = e1.get()
        if requested_username:
            mstr = Tk()
            listbox = Listbox(mstr, width=100, height=30)
            listbox.pack()
            sent = business_logic.send_request(username, requested_username)
            if sent:
                listbox.insert(END, "Friend request is sent.")
            else:
                listbox.insert(END, "Either your or yours to be friend's username is incorrect!!")
        else:
            Label(master, text="User Id cannot be null!!", fg="red").grid(row=3, column=3)

    def displaypending():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=30)
        listbox.pack()
        my_pending_requests = business_logic.return_my_friend_requests(username)
        if len(my_pending_requests) == 0:
            listbox.insert(END, "Sorry, you do not have any pending requests :-(")
        else:
            for pending_request in my_pending_requests:
                listbox.insert(END, pending_request.requester_username)

    def acceptreq():
        if e2.get():
            accepted = business_logic.accept_request(e2.get(), username)
            if accepted:
                Label(master, text="Friend request accepted!!").grid(row=8, column=1)
            else:
                Label(master, text="Request does not exist!!").grid(row=8, column=1)
        else:
            Label(master, text="User Id cannot be null!!", fg="red").grid(row=8, column=1)

    def rejectreq():
        if e3.get():
            rejected = business_logic.decline_request(e3.get(), username)
            if rejected:
                Label(master, text="Friend request rejected!!").grid(row=11, column=1)
            else:
                Label(master, text="Request does not exist!!").grid(row=11, column=1)
        else:
            Label(master, text="User Id cannot be null!!", fg="red").grid(row=11, column=1)

    def unfriend():
        friend_username = e4.get()
        if friend_username:
            unfriended = business_logic.unfirend(username, friend_username)
            if unfriended:
                Label(master, text="Unfriended").grid(row=14, column=1)
            else:
                Label(master, text="You were already not friends with this person!").grid(row=14, column=1)
        else:
            Label(master, text="User Id cannot be null!!", fg="red").grid(row=14, column=1)

    def viewhealthdata():
        mstr = Tk()
        listbox = Listbox(mstr, width=100, height=30)
        listbox.pack()
        health_dao = HealthDataDao.HealthDataDao()
        my_friends = business_logic.return_my_friends(username)
        for friend in my_friends:
            if friend.requester_username == username:
                mydatumlist = health_dao.read_datum(friend.requested_username)
                for datum in mydatumlist:
                    listbox.insert(END, 'Username of the friend-' + friend.requested_username)
                    listbox.insert(END, 'Property id: ' + str(datum.propertyid) + '     Value: ' + str(datum.value))
            elif friend.requested_username == username:
                mydatumlist = health_dao.read_datum(friend.requester_username)
                for datum in mydatumlist:
                    listbox.insert(END, 'Username of the friend-' + friend.requester_username)
                    listbox.insert(END, 'Property id: ' + str(datum.propertyid) + '     Value: ' + str(datum.value))
        listbox.insert(END, '*************************************************************************************')
        properties = health_dao.read_properties()
        for property in properties:
            listbox.insert(END, 'Property id: ' + str(
                property.propertyid) + ', Name: ' + property.name + ', Description: ' + property.description)

    master = Tk()
    Label(master, text="***** Welcome to SmartHealth Friendship portal *****").grid(row=0, column=1)
    Button(master, text="Click me to see your friends", command=display).grid(row=1, column=1)

    Label(master, text="***** Enter username you want to befriend with and press the button below- *****").grid(row=2, column=1)
    Label(master, text="Username of your to be friend:").grid(row=3, column=0)
    e1 = Entry(master)
    e1.grid(row=3, column=1)
    Button(master, text="Send Friend Request", command=sendreq).grid(row=3, column=2)

    Label(master, text="***** Display Pending requests *****").grid(row=4, column=1)
    Button(master, text="Click me to see pending requests", command=displaypending).grid(row=5, column=1)

    Label(master, text="***** Accept Pending requests *****").grid(row=6, column=1)
    Label(master, text="Username of the request to be accepted:").grid(row=7, column=0)
    e2 = Entry(master)
    e2.grid(row=7, column=1)
    Button(master, text="Accept Friend Request", command=acceptreq).grid(row=7, column=2)

    Label(master, text="***** Reject Pending requests *****").grid(row=9, column=1)
    Label(master, text="Username of the request to be rejected:").grid(row=10, column=0)
    e3 = Entry(master)
    e3.grid(row=10, column=1)
    Button(master, text="Reject Friend Request", command=rejectreq).grid(row=10, column=2)

    Label(master, text="***** Unfriend someone *****").grid(row=12, column=1)
    Label(master, text="Username of the friend to be un friended:").grid(row=13, column=0)
    e4 = Entry(master)
    e4.grid(row=13, column=1)
    Button(master, text="Unfriend", command=unfriend).grid(row=13, column=2)

    Label(master, text="***** View Health Data of your active friends *****").grid(row=15, column=1)
    Button(master, text="View Health Data", command=viewhealthdata).grid(row=16, column=1)

    master.mainloop()


