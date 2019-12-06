from models import Messages
from db_instance import db
from flask import Flask, request, render_template, Blueprint, jsonify


social_api = Blueprint('social_api', __name__)


@social_api.route('/like-post', methods=['POST'])
def like_post():
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