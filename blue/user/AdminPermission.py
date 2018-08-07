from flask import Blueprint
from blue .user .permission import *
import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0)

v = r.get('aakash').decode()
admin1 = eval(v)
admin = Blueprint('AdminPermission', __name__)


@admin.route('/initt')
@admin_permission('POST', admin1)
def user_create():
    return "hey aakash user created successfully congrats !!!"


@admin.route('/')
def user_give_permission():
    pass


@admin.route('/')
def user_delete_permission():
    pass


@admin.route('/')
def user_delete():
    pass


@admin.route('/')
def user_view():
    pass
