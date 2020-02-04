from flask import Blueprint, jsonify, request, render_template
from db_instance import db
from models import Notifications_v2, Messages, Users_v2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from sqlalchemy.exc import IntegrityError



email_api = Blueprint('email_api', __name__)
gmail_user = os.environ["GMAIL_USERNAME"]
gmail_password = os.environ["GMAIL_PASS"]

@email_api.route('/register-notification', methods=['POST'])
def register_notification():
    email = request.json['email']
    name = request.json['name']
    subscribed_to = request.json['subscribed_to']
    find_subscribed_to_user = Messages.query.filter_by(id=subscribed_to).first().pooper_name
    find_subscribed_to_user_id = Users_v2.query.filter_by(username=find_subscribed_to_user).first().id
    check_email = Notifications_v2.query.filter(Notifications_v2.email==email, Notifications_v2.subscribed_to==find_subscribed_to_user_id).first() 
    if check_email == None:
        add_email = Notifications_v2(name=name,email=email, subscribed_to=find_subscribed_to_user_id)
        db.session.add(add_email)
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False)

@email_api.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    user = request.args.get('user')
    to_delete_email = Notifications_v2.query.filter(Notifications_v2.email==email, Notifications_v2.subscribed_to==user).first() 
    if to_delete_email != None:
        db.session.delete(to_delete_email)
        db.session.commit()
    else:
        return '<h1> You are already unsubscribed!</h1>'
    return '<h1>Thanks for successfully unsubscribing!</h1>'

def send_notifications(poop_message,user):
    #get all emails
    emails = Notifications_v2.query.filter_by(subscribed_to=user).all()
    subscribed_to_user = Users_v2.query.filter_by(id=user).first().username
    emails_list = [email.email for email in emails]
    for email in emails_list:
        #send emails
        name = Notifications_v2.query.filter_by(email=email).first().name
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = email
        msg['Subject'] = '{} just Shatted!'.format(subscribed_to_user)
        # Create the body of the message (a plain-text and an HTML version).
        html = """\
        <html>
        <head></head>
        <body>
            <p>Hi {},</p>
            <p>Guess what!!!, {} just sharted, here is his message:</p>
            <p><em>"{}"</em></p>
            <p>Sincerely,</p>
            <p>The Poop Team</p><br><br><br>
            <span><a href='http://www.didshantpoop.com/unsubscribe?email={}&user={}'>Click here to unsubscribe</a></span>
        </body>
        </html>
        """.format(name,subscribed_to_user,poop_message,email,user)

        part2 = MIMEText(html, 'html')

        msg.attach(part2)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,email,msg.as_string())
        server.close()
    return "Success"