from models import Messages, Comments, Users_v2
from db_instance import db
from flask import Flask, request, render_template, Blueprint, jsonify
from datetime import date
import datetime
import pytz
from pytz import timezone
from collections import Counter
from emailAPI import send_notifications


status_api = Blueprint('status_api', __name__)

#helper function, counts the poop streak
def find_start_end_dates(dates):
    current_streak = 0
    date = datetime.datetime.today()
    date_pacific = date.astimezone(timezone('US/Pacific'))
    if str( date_pacific.strftime ('%m-%d-%Y') ) == str(dates[-1:][0]):
        start_date = dates[0]
        transpose_start_date = start_date.split('-')
        start_date = datetime.datetime(int(transpose_start_date[2]), int(transpose_start_date[0]), int(transpose_start_date[1]))
        next_day = ''
        for date in dates:
            transpose_date = date.split('-')
            date = datetime.datetime(int(transpose_date[2]), int(transpose_date[0]), int(transpose_date[1]))
            if next_day == '':
                next_day = date + datetime.timedelta(days=1)
            if date == next_day:
                next_date = date + datetime.timedelta(days=1)
                current_streak += 1
                next_day = next_date
            elif date != next_day:
                next_date = date + datetime.timedelta(days=1)
                current_streak = 0
                next_day = next_date
    return current_streak


@status_api.route('/get-top-liked', methods=['GET']) #this is for the topRated.vue page
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

@status_api.route('/streak', methods=['GET']) #this is for the poopStreak.vue page
def streak():
    messages = Messages.query.all()
    dates = [{"id": message.id, "date": message.poop_date} for message in messages]
    dates_sorted = sorted(dates, key = lambda i: i['id'])
    dates = [date['date'] for date in dates_sorted]
    dates_list = []
    [dates_list.append(x) for x in dates if x not in dates_list] 
    streak = find_start_end_dates(dates_list)
    return jsonify(streak=streak)
        

@status_api.route('/consecutive-days', methods=['GET']) #this is for the poopStreak.vue page
def consecutive_days():
    messages = Messages.query.all()
    list_of_dates = []
    for message in messages:
        list_of_dates.append(message.poop_date)
    dates = list(Counter(list_of_dates).keys()) # equals to list(set(words))
    counts = list(Counter(list_of_dates).values()) # counts the elements' frequency
    max_pos = counts.index(max(counts))
    most_poops_date = dates[max_pos]

    list_of_dicts = []
    for message in messages:
        if message.poop_date == most_poops_date:
            if message.poop_likes == None:
                message.poop_likes = 0
            list_of_dicts.append({'id':message.id, 
                    'message': message.poop_message,
                    'date': message.poop_date, 
                    'rating': message.poop_rating, 
                    'likes': message.poop_likes})

    return jsonify(list_of_dicts)



@status_api.route("/update-status", methods=['POST'])
def update_status():
    message = request.json['message']
    rating = request.json['rating']
    session_id = request.json['session_id']
    if rating == 0 or rating == 1 or rating == 2 or rating == 3 or rating == 4 or rating == 5:
        rating = rating
    else:
        rating = 5
    if session_id != '':
        user_name = Users_v2.query.filter_by(id=session_id).first().username
        user_id = Users_v2.query.filter_by(id=session_id).first().id
        date_format='%m-%d-%Y'
        date = datetime.datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        date_today = date.strftime(date_format)
        new_poop = Messages(pooper_name=user_name,poop_date=date_today, poop_message=message, poop_rating=rating)
        db.session.add(new_poop)
        db.session.commit()
        send_notifications(message,user_id)
        return 'Success'
    return 'Falure'

@status_api.route("/get-specific-user-latest-poop", methods=['POST'])
def get_specific_user_latest_poop():
    session_id = request.json['session_id']
    user_name = Users_v2.query.filter_by(id=session_id).first().username
    poops = Messages.query.filter_by(pooper_name=user_name).order_by(Messages.id.desc()).limit(1).all()
    poop_dict=[{'id':poop.id, 'name': poop.pooper_name, 'date': poop.poop_date, 'message': poop.poop_message, 'rating': poop.poop_rating} for poop in poops]
    return jsonify(poop_dict)