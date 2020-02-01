from db_instance import db
from hashutils import make_pw_hash, check_pw_hash

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pooper_name = db.Column(db.String(600),nullable=False)
    poop_date = db.Column(db.String(600),nullable=False)
    poop_message = db.Column(db.String(600),nullable=False)
    poop_rating = db.Column(db.String(100))
    poop_likes = db.Column(db.Integer)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(600),nullable=False)
    commenter_name = db.Column(db.String(600),nullable=False)
    comment_time = db.Column(db.String(600),nullable=False)
    comment_likes = db.Column(db.Integer)
    comment_message = db.Column(db.Integer, db.ForeignKey('messages.id'),
        nullable=False)

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(600),nullable=False)
    email = db.Column(db.String(600),nullable=False)
    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    pw_hash = db.Column(db.String(500))
    profile_image = db.Column(db.String(120))
    profile_bio = db.Column(db.String(1000))

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)

class PhoneNumber(db.Model): #helper DB so I don't have to add another column to the users database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    phone_number = db.Column(db.String(120))

class Notifications_v2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(600),nullable=False)
    email = db.Column(db.String(600),nullable=False)
    subscribed_to = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Users_v2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    pw_hash = db.Column(db.String(500))
    profile_image = db.Column(db.String(120))
    profile_bio = db.Column(db.String(1000))
    phone_number = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)