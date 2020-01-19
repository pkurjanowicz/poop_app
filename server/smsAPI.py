from flask import Flask, request, render_template, Blueprint, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import datetime
from models import Messages
from db_instance import db
import pytz
from pytz import timezone
from emailAPI import send_notifications

sms_api = Blueprint('sms_api', __name__)

def get_poop():
    poops = Messages.query.filter_by(pooper_name='Shant').all()
    poop_list_of_dicts=[{'id':poop.id, 'date': poop.poop_date, 'message': poop.poop_message, 'rating': poop.poop_rating} for poop in poops ]
    poop_list_of_dicts_sorted = sorted(poop_list_of_dicts, key = lambda i: i['id'])
    return poop_list_of_dicts_sorted[-1]

def get_specific_poop(message):
    poop = Messages.query.filter_by(poop_message=message).first()
    poop_dict=[{'id':poop.id, 'name': poop.pooper_name, 'date': poop.poop_date, 'message': poop.poop_message, 'rating': poop.poop_rating, 'poop_likes': poop.poop_likes}]
    return poop_dict

def get_all_poops():
    poops = Messages.query.all()
    poop_list_of_dicts=[{'id':poop.id, 'name': poop.pooper_name, 'date': poop.poop_date, 'message': poop.poop_message, 'rating': poop.poop_rating, 'poop_likes': poop.poop_likes} for poop in poops ]
    poop_list_of_dicts_sorted = sorted(poop_list_of_dicts, key = lambda i: -i['id'])
    return poop_list_of_dicts_sorted

def verify_shant(number):
    if number == '+12032312081' or number == "+18186068167":
        return True
    return True

def update_status():
    date_format='%m-%d-%Y'
    date = datetime.datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    date_today = date.strftime(date_format)
    if date_today != get_poop()['date']:
        return False
    return True

#main route
@sms_api.route("/sms", methods=['GET'])
def sms_ahoy_reply():
    number = request.args.get('From')
    body = request.args.get('Body')
    rating = request.args.get('poop_rating')
    if rating == '0' or rating == '1' or rating == '2' or rating == '3' or rating == '4' or rating == '5':
        rating = rating
    else:
        rating = '5'
    if verify_shant(number):
        date_format='%m-%d-%Y'
        date = datetime.datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        date_today = date.strftime(date_format)
        new_poop = Messages(pooper_name='Shant',poop_date=date_today, poop_message=body, poop_rating=rating)
        db.session.add(new_poop)
        db.session.commit()
        send_notifications(body)
        return 'Success'
    return 'Falure'

@sms_api.route('/get-poops', methods=['GET'])
def render_app():
    has_shant_pooped = update_status()
    if has_shant_pooped == True:
        return jsonify({
            'message':'Yes',
            'last_poop_date': get_poop()['date'],
            'poop_message': get_poop()['message'], 
            'poop_rating': get_poop()['rating'],
            'poop_id': get_poop()['id']
        })
    return jsonify({
            'message':'No',
            'last_poop_date': get_poop()['date'],
            'poop_message': get_poop()['message'], 
            'poop_rating': get_poop()['rating'],
            'poop_id': get_poop()['id']
        })

@sms_api.route('/get-all-poops', methods=['GET'])
def render_poops():
    all_poops = get_all_poops()
    return_value = [{'name': poop['name'],'last_poop_date': poop['date'],'poop_message': poop['message'], 'poop_rating': poop['rating'],'poop_id': poop['id'], 'poop_likes': poop['poop_likes']} for poop in all_poops]
    return jsonify(return_value)

@sms_api.route('/get-specific-poop', methods=['POST'])
def get_specific_poop_value():
    message = request.json['message']
    poop = get_specific_poop(message)
    return jsonify(poop)