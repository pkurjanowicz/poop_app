from flask import Flask, request, render_template, Blueprint, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import datetime
from models import Messages
from db_instance import db
import pytz
from pytz import timezone

sms_api = Blueprint('sms_api', __name__)

def get_poop():
    poops = Messages.query.filter_by(pooper_name='Shant').all()
    poop_list_of_dicts=[{'id':poop.id, 'date': poop.poop_date, 'message': poop.poop_message, 'rating': poop.poop_rating} for poop in poops ]
    poop_list_of_dicts_sorted = sorted(poop_list_of_dicts, key = lambda i: i['id'])
    return poop_list_of_dicts_sorted[-1]

def verify_shant(number):
    if number == '+12032312081' or number == "+18186068167":
        return True
    return False

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
    if rating > '5':
        rating = '5'
    if verify_shant(number):
        date_format='%m-%d-%Y'
        date = datetime.datetime.now(tz=pytz.utc)
        date = date.astimezone(timezone('US/Pacific'))
        date_today = date.strftime(date_format)
        new_poop = Messages(pooper_name='Shant',poop_date=date_today, poop_message=body, poop_rating=rating)
        db.session.add(new_poop)
        db.session.commit()
        return 'Success'
    return 'Falure'

    """
    RESPONSE DATA EXAMPLE(QUERY STRING)
    ?ToCountry=US
    &ToState=AL
    &SmsMessageSid=SMc5c48883a3902d997b64e39dca6bd5c9
    &NumMedia=0
    &ToCity=TUSCALOOSA
    &FromZip=06484
    &SmsSid=SMc5c48883a3902d997b64e39dca6bd5c9
    &FromState=CT
    &SmsStatus=received
    &FromCity=DERBY
    &Body=hey+there
    &FromCountry=US
    &To=%2B12052933232
    &ToZip=35405
    &NumSegments=1
    &MessageSid=SMc5c48883a3902d997b64e39dca6bd5c9
    &AccountSid=ACd11feb6ef2a175264fd6e40fc62ad19d
    &From=%2B12032312081
    &ApiVersion=2010-04-01
    """

@sms_api.route('/get-poops', methods=['GET'])
def render_app():
    has_shant_pooped = update_status()
    if has_shant_pooped == True:
        return jsonify({
            'message':'Yes',
            'last_poop_date': get_poop()['date'],
            'poop_message': get_poop()['message'], 
            'poop_rating': get_poop()['rating']
        })
    return jsonify({
            'message':'No',
            'last_poop_date': get_poop()['date'],
            'poop_message': get_poop()['message'], 
            'poop_rating': get_poop()['rating']
        })


