# This tutorial is for decorator

from functools import wraps


def decorator_name(fun):
    @wraps(fun)
    def decorated(*args, **kwargs):
        print('doing some thing before original function execute')
        for i in args:
            print(i)
        return fun(*args, **kwargs)

    return decorated


@decorator_name
def require_decorator(a, b):
    print("i need decorator")


# require_decorator(4, 5)


# decorators take parameters in it


def add_tags(*tags):
    def decorator(oldfun):
        def inside(*args, **kwargs):
            print(args)
            code = oldfun(*args, **kwargs)
            print(code)
            for tag in reversed(tags):
                code = '<{0}>{1}</{0}>'.format(tag, code)
            return code

        return inside

    return decorator


@add_tags('p', 'i', 'b')
def my_name(n, y,k):
    return "welcome "+y+" my blog"


print(my_name('ff','aakash', 5))

# decorators in depth


def bread(func):
    def wrapper():
        print("</'''''''''''/>")
        func()
        print("<\___________/")
    return wrapper


def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper


def sandwhich(food = '--ham--'):
    print(food)


#sandwhich() # output: --ham--
sandwhich = bread(ingredients(sandwhich))
sandwhich()

# using python decorator syntax


@bread
@ingredients
def strange_sandwhich(food='--hitchi--'):
    print(food)


strange_sandwhich()


def my_decorator(func):
    print("i'm ordinary function")
    def wrapper():
        print("wrapper function")
        func()
    return  wrapper

@my_decorator
def lazy():
    print('lazy function')


lazy()


def decorator_maker(a):
    print(
    'I make decorators! I am executed only once: ' + \
    'when you make me create a decorator.')

    def my_decorator(func):
        print('I am a decorator! I am executed only when you decorate a function.')

        def wrapped():
            print('I am the wrapper around the decorated function. '
                  'I am called when you call the decorated function. '
                  'As the wrapper, I return the RESULT of the decorated function.')
            return func()

        print('As the decorator, I return the wrapped function.')

        return wrapped

    print('As a decorator maker, I return a decorator')
    return my_decorator

@decorator_maker('a')
def decorated_function():
    print ('I am the decorated function.')


decorated_function()