from flask import Blueprint, jsonify, request, session
from db_instance import db
import random
import string
from models import Users
from hashutils import make_pw_hash, check_pw_hash
import os


users_api = Blueprint('users_api', __name__)


def randomString():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(20))


@users_api.route('/nonloggedinsession', methods=['GET'])
def nonloggedinsession():
    if 'notloggedin' in session:
        return jsonify(session = session['notloggedin'])
    else:
        session['notloggedin'] = randomString()
        not_logged_in_session = session['notloggedin']
        return jsonify(session=not_logged_in_session)

@users_api.route('/deletenonloggedinsession', methods=['GET'])
def deletenonloggedinsession():
    try:
        del session['notloggedin']
        return jsonify(success=True)
    except KeyError:
        return jsonify(success=False)

@users_api.route('/checklogin', methods=['POST'])
def check_user():
        session['user'] = ''
        username = request.json["username"]
        password = request.json["password"]
        user = Users.query.filter_by(username=username).first()
        if check_pw_hash(password, user.pw_hash):
                session['user'] = user.id
                usernamesession = session['user']
                return jsonify(session=usernamesession) #this is used to pass session to vue


@users_api.route('/checksession', methods=["GET"])
def check_session():
        if 'user' in session:
                return jsonify(
                        session = True,
                        user = session['user']
                )
        else:
                return jsonify(session = False)


@users_api.route('/adduser', methods=['POST'])
def add_user():
        username = request.json["username"]
        password = request.json["password"]
        code = request.json["code"]
        if code == os.environ["CODE"]:
                new_user = Users(username=username,password=password)
                db.session.add(new_user)
                db.session.commit()
                user = Users.query.filter_by(username=username).first()
                session['user'] = user.id
                usernamesession = session['user']
                return jsonify(session=usernamesession)
        return jsonify(success=False)

@users_api.route("/logout", methods=["GET"])
def logout():
        del session['user']
        return jsonify(success=True)

@users_api.route('/addimage', methods=['POST', 'GET'])
def add_image():
        link = request.json["link"]
        user_id = request.json["user_id"]
        Users.query.filter_by(id=user_id).first().profile_image = link
        db.session.commit()
        return jsonify(success=True)

@users_api.route('/getimgurkey', methods=['POST'])
def getimgurkey():
        user_id=request.json['user_id']
        key = os.environ["IMGUR_SECRET"]
        print(key)
        try:
                user = Users.query.filter_by(id=user_id).first() 
                if user.id == session['user']:
                        return jsonify(key=key)
        except KeyError:
                return jsonify(key=False)