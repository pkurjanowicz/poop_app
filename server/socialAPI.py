from models import Messages, Comments,Users_v2
from db_instance import db
from flask import Flask, request, render_template, Blueprint, jsonify, session
from datetime import datetime


social_api = Blueprint('social_api', __name__)

def checksession():
    if 'notloggedin' in session:
        return True
    else:
        return False

@social_api.route('/like-post', methods=['POST'])
def like_post():
    poop_message = request.json['post_message']
    find_post = Messages.query.filter_by(poop_message=poop_message).first()
    num_of_likes = find_post.poop_likes
    if not checksession():
        try: 
            num_likes = Messages.query.filter_by(poop_message=poop_message).first().poop_likes
            num_likes += 1
            update_like = Messages.query.filter_by(poop_message=poop_message).first().poop_likes = num_likes
            db.session.commit()
        except TypeError:
            update_like = Messages.query.filter_by(poop_message=poop_message).first().poop_likes = 1
            db.session.commit()
    find_post = Messages.query.filter_by(poop_message=poop_message).first()
    num_of_likes = find_post.poop_likes
    return jsonify(likes=num_of_likes)

@social_api.route('/like-post-stream', methods=['POST'])
def like_post_stream():
    poop_message = request.json['post_message']
    find_post = Messages.query.filter_by(poop_message=poop_message).first()
    num_of_likes = find_post.poop_likes
    try: 
        num_likes = Messages.query.filter_by(poop_message=poop_message).first().poop_likes
        num_likes += 1
        update_like = Messages.query.filter_by(poop_message=poop_message).first().poop_likes = num_likes
        db.session.commit()
    except TypeError:
        update_like = Messages.query.filter_by(poop_message=poop_message).first().poop_likes = 1
        db.session.commit()
    find_post = Messages.query.filter_by(poop_message=poop_message).first()
    num_of_likes = find_post.poop_likes
    return jsonify(likes=num_of_likes)

@social_api.route('/get-likes', methods=['POST'])
def get_likes():
    poop_message = request.json['post_message']
    find_post = Messages.query.filter_by(poop_message=poop_message).first()
    num_of_likes = find_post.poop_likes
    return jsonify(likes=num_of_likes)

@social_api.route('/submit-comment', methods=['POST']) #from Shants status page
def submit_comment():
    comment = request.json['comment']
    commenter_name = request.json['name']
    comment_time = datetime.utcnow()
    comment_message = request.json['message']
    if comment != '': 
        if commenter_name == '':
            commenter_name = 'Anonymous'
        new_comment = Comments(comment=comment,commenter_name=commenter_name, comment_time=comment_time, comment_message=comment_message)
        db.session.add(new_comment)
        db.session.commit()
        return jsonify(success=True)

@social_api.route('/submit-comment-poopstream', methods=['POST']) #from the poopstream page
def submit_comment_poopstream():
    comment = request.json['comment']
    commenter_id = request.json['session_id']
    comment_time = datetime.utcnow()
    comment_message = request.json['message']
    if comment != '': 
        if commenter_id == '':
            commenter_id = 'Anonymous'
            new_comment = Comments(comment=comment,commenter_name=commenter_id, comment_time=comment_time, comment_message=comment_message)
            db.session.add(new_comment)
            db.session.commit()
            return jsonify(success=True)
        else:
            find_user_name = Users_v2.query.filter_by(id=commenter_id).first().username
            new_comment = Comments(comment=comment,commenter_name=find_user_name, comment_time=comment_time, comment_message=comment_message)
            db.session.add(new_comment)
            db.session.commit()
            return jsonify(success=True)
    return jsonify(success=False)

@social_api.route('/get-comments', methods=['POST'])
def get_comments():
    comment_message = request.json['message']
    comments = Comments.query.filter_by(comment_message=comment_message).all()
    comments_list_of_dicts=[{'id':comment.id, 'message': comment.comment,'name': comment.commenter_name, 'time': comment.comment_time, 'likes': comment.comment_likes} for comment in comments ]
    comments_list_of_dicts_sorted = sorted(comments_list_of_dicts, key = lambda i: i['id'])
    return jsonify(comments_list_of_dicts_sorted)