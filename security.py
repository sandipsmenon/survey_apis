from werkzeug.security import safe_str_cmp
from models.user import UserModel
from pprint import pprint

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    pprint(user)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
