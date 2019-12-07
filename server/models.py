from db_instance import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pooper_name = db.Column(db.String(600),nullable=False)
    poop_date = db.Column(db.String(600),nullable=False)
    poop_message = db.Column(db.String(600),nullable=False)
    poop_rating = db.Column(db.String(100))
    poop_likes = db.Column(db.Integer)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commenter_name = db.Column(db.String(600),nullable=False)
    comment_time = db.Column(db.String(600),nullable=False)
    comment_likes = db.Column(db.Integer)
    comment_message = db.Column(db.Integer, db.ForeignKey('messages.id'),
        nullable=False)
    