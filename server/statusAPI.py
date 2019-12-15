from models import Messages, Comments
from db_instance import db
from flask import Flask, request, render_template, Blueprint, jsonify

status_api = Blueprint('status_api', __name__)

@status_api.route('/get-top-liked', methods=['GET'])
def get_top_liked():
    messages = Messages.query.all()
    list_of_dicts = []
    for message in messages:
        if message.poop_likes == None: #this is the null value from the DB
            message.poop_likes = 0
            list_of_dicts.append({'id':message.id, 
            'message': message.poop_message,
            'date': message.poop_date, 
            'rating': message.poop_rating, 
            'likes': message.poop_likes})
        else:
            list_of_dicts.append({'id':message.id, 
            'message': message.poop_message,
            'date': message.poop_date, 
            'rating': message.poop_rating, 
            'likes': message.poop_likes})
    list_of_dicts_sorted = sorted(list_of_dicts, key = lambda i: i['likes'])[-5:][::-1] #only returns the last 5 items in reverse order
    return jsonify(list_of_dicts_sorted)
