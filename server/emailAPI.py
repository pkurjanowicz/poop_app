from flask import Blueprint, jsonify, request, render_template
from db_instance import db
from models import Notifications, Messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


email_api = Blueprint('email_api', __name__)
# gmail_user = 'pkurjanowicz10@gmail.com'
# gmail_password = os.environ["GMAIL_PASS"]

@email_api.route('/register-notification', methods=['POST'])
def register_notification():
    email = request.json['email']
    name = request.json['name']
    add_email = Notifications(name=name,email=email)
    db.session.add(add_email)
    db.session.commit()
    return jsonify(success=True)

# @email_api.route('/sendnotifications', methods=['POST'])
# def send_notifications():
#     message_id = request.json['message_id']
#     if emails != '':
#         for email in emails:
#             # Add to DB
#             new_invite = Invites(invitee_email=email,event_id=event_id)
#             db.session.add(new_invite)
#             db.session.commit()
#             #send emails
#             msg = MIMEMultipart()
#             msg['From'] = gmail_user
#             msg['To'] = email
#             msg['Subject'] = 'Please accept this invite to my event!'
#             # Create the body of the message (a plain-text and an HTML version).
#             # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
#             html = """\
#             <html>
#             <head></head>
#             <body>
#                 <p>Hi!<br>
#                 How are you?<br>
#                 <a href='http://127.0.0.1:5000/response?event_id={}&email={}&response=True'><button>Click here to accept</button></a>
#                 <button>Click here to reject</button>
#                 </p>
#             </body>
#             </html>
#             """.format(event_id,email)

#             # Record the MIME types of both parts - text/plain and text/html.
#             # part1 = MIMEText(text, 'plain')
#             part2 = MIMEText(html, 'html')

#             # Attach parts into message container.
#             # According to RFC 2046, the last part of a multipart message, in this case
#             # the HTML message, is best and preferred.
#             # msg.attach(part1)
#             msg.attach(part2)
#             server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#             server.ehlo()
#             server.login(gmail_user, gmail_password)
#             server.sendmail(gmail_user,email,msg.as_string())
#             server.close()
#             print('Success!')
#         return jsonify(success=True)