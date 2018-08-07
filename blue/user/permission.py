# create objects of permission
from functools import wraps
from flask import flash

user = {

    'resource1': {
        'GET': 1,
        'POST': 1,
        'PUT': 0
    },
    'resource2': {
        'GET': 1,
        'POST': 1
    }

}


# this for method levels i.e routes level


def check_permission(rs):
    def decorated(afun):
        @wraps(afun)
        def decorator(*args, **kwargs):
            get = user.get(rs).get('GET')
            post = user.get(rs).get('POST')
            put = user.get(rs).get('PUT')
            delete = user.get(rs).get('DELETE')
            if get or post or put or delete:
                return afun(*args, **kwargs)
            else:
                flash('you are not authorised to access this page')

        return decorator

    return decorated


# Decorator for admin permission here

def admin_permission(op, permission):
    def decorated(afun):
        @wraps(afun)
        def decorator(*args, **kwargs):
            get = permission.get('key1')
            post = permission.get('key2')
            put = permission.get('key3')
            delete = permission.get('key4')

            if op == get or op == post or op == put or op == delete:
                return afun(*args, **kwargs)
            else:
                flash('sorry your are not eligiable to access this permission')
        return decorator
    return decorated


@check_permission('resource1')
def user1():
    print("resource is access")


def user2():
    print("resource is not access")
    pass


# user getter and setter to acces the resource


class Privacy:

    def __init__(self, ):
        pass
