# Common base class for all users
class User(object):
    def __init__(self, username, password, email1, email2, firstname, lastname, aboutme, photourl1, photourl2, photourl3, streetnumber, streetname, majormunicipality, governingdistrict, postalarea, usertypeid, status):
        self.username = username
        self.password = password
        self.email1 = email1
        self.email2 = email2
        self.firstname = firstname
        self.lastname = lastname
        self.aboutme = aboutme
        self.photourl1 = photourl1
        self.photourl2 = photourl2
        self.photourl3 = photourl3
        self.streetnumber = streetnumber
        self.streetname = streetname
        self.majormunicipality = majormunicipality
        self.governingdistrict = governingdistrict
        self.postalarea = postalarea
        self.usertypeid = usertypeid
        self.status = status


# Derived class for customers
class EndUser(User):
    def __init__(self, karma, datecreated, *args, **kwargs):
        super(EndUser, self).__init__(*args, **kwargs)
        self.karma = karma
        self.datecreated = datecreated


# Derived class moderators
class Moderator(User):
    def __init__(self, phone, *args, **kwargs):
        self.phone = phone
        super(Moderator,self).__init__(*args,**kwargs)


# Derived class administrators
class Administrator(User):
    def __init__(self, phone, *args, **kwargs):
        self.phone = phone
        super(Administrator, self).__init__(*args, **kwargs)


class Friendship(object):
    def __init__(self, requester_username, requested_username, when_requested, when_withdrawn, when_rejected,
                 when_confirmed, when_unfriended):
        self.requester_username = requester_username
        self.requested_username = requested_username
        self.when_requested = when_requested
        self.when_withdrawn = when_withdrawn
        self.when_rejected = when_rejected
        self.when_confirmed = when_confirmed
        self.when_unfriended = when_unfriended


class Forum(object):
    def __init__(self, forumid, topic, url, summary, whencreated, whenclosed, createdbymoderator_username, deletedbymoderator_username):
        self.forumid = forumid
        self.topic = topic
        self.url = url
        self.summary = summary
        self.whencreated = whencreated
        self.whenclosed = whenclosed
        self.createdbymoderator_username = createdbymoderator_username
        self.deletedbymoderator_username = deletedbymoderator_username


class Post(object):
    def __init__(self, username, timecreated, forumid, textentry, photolocation, linklocation, videolocation):
        self.username = username
        self.timecreated = timecreated
        self.forumid = forumid
        self.textentry = textentry
        self.photolocation = photolocation
        self.linklocation = linklocation
        self.videolocation = videolocation


class Comment(object):
    def __init__(self, post_username, post_timeCreated, commenter_username, commenttime, commenttext, photolocation, linklocation, videolocation):
        self.post_username = post_username
        self.post_timeCreated = post_timeCreated
        self.commenter_username = commenter_username
        self.commenttime = commenttime
        self.commenttext = commenttext
        self.photolocation = photolocation
        self.linklocation = linklocation
        self.videolocation = videolocation


class Rating(object):
    def __init__(self, post_username, post_timecreated, rater_username, stars):
        self.post_username = post_username
        self.post_timecreated = post_timecreated
        self.rater_username = rater_username
        self.stars = stars

# Base class qualification
class Qualification(object):
    def __init__(self, qualificationid, description):
        self.qualificationid = qualificationid
        self.description = description


# Base class for property
class Property(object):
    def __init__(self, propertyid, name, description):
        self.propertyid = propertyid
        self.name = name
        self.description = description


# Base class for datum
class Datum(object):
    def __init__(self, datumid, username, propertyid, value, whensaved):
        self.datumid = datumid
        self.username = username
        self.propertyid = propertyid
        self.value = value
        self.whensaved = whensaved