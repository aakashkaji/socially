
# This tutorial is for decorator

from functools import wraps


def decorator_name(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        print('doing some thing before original function execute')
        return fun(*args, **kwargs)
    return decorated


@decorator_name
def require_decorator():
    print("i need decorator")


require_decorator()
