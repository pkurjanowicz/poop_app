from flask import Blueprint, jsonify, request, render_template
from db_instance import db
from models import Notifications, Messages
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
    add_email = Notifications(name=name,email=email)
    db.session.add(add_email)
    db.session.commit()
    return jsonify(success=True)

@email_api.route('/unsubscribe', methods=['GET'])
def unsubscribe():
    email = request.args.get('email')
    to_delete_email = Notifications.query.filter_by(email=email).first()
    if to_delete_email != None:
        db.session.delete(to_delete_email)
        db.session.commit()
    else:
        return '<h1> You are already unsubscribed!</h1>'
    return '<h1>Thanks for successfully unsubscribing!</h1>'

def send_notifications(poop_message):
    #get all emails
    emails = Notifications.query.all()
    emails_list = [email.email for email in emails]
    for email in emails_list:
        #send emails
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = email
        msg['Subject'] = 'Shant just Shatted!'
        # Create the body of the message (a plain-text and an HTML version).
        html = """\
        <html>
        <head></head>
        <body>
            <p>Hello loyal poop subscriber!</p>
            <p>Guess what!!!, Shant just sharted, here is his message:</p>
            {}<br>
            <p>Have a very poopy day!</p>
            <p>Sincerely,</p>
            <p>The Poop Team</p><br><br><br>
            <span><a href='http://www.didshantpoop.com/unsubscribe?email={}'>Click here to unsubscribe</a></span>
        </body>
        </html>
        """.format(poop_message,email)

        part2 = MIMEText(html, 'html')

        msg.attach(part2)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user,email,msg.as_string())
        server.close()
    return "Success"