from flask import Blueprint, jsonify, request, session
from db_instance import db
import random
import string


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