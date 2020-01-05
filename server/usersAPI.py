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
    del session['notloggedin']
    return jsonify(success=True)