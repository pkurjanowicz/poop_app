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

    def __init__(self, username, password,profile_image):
        self.username = username
        self.pw_hash = make_pw_hash(password)
        self.profile_image = profile_image