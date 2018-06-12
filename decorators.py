"""
How does @app.route work?

Let's start with a simpler decorator, then work our way up.
How about a timer?
"""
import datetime

def sum_of_squares(n):
    """
    add 1*1 + 2*2 + 3*3 + ... + n*n
    """
    total = 0
    for num in range(n + 1):
        total += (num * num)
    return total

# functions are just values! they can be assigned to a
# new variable like any other value.
s_of_s = sum_of_squares

def product_of_squares(n):
    total = 1
    for num in range(1, n + 1):
        total *= (num * num)
    return total

def timed(func):
    """
    timed eats a function, and produces (returns)
    another function, one that prints out how long
    it took to run.
    """
    def timed_version(n):
        start_time = datetime.datetime.now()
        ret = func(n)
        end_time = datetime.datetime.now()
        print("elapsed time", end_time - start_time)
        return ret
    return timed_version

timed_sum_of_squares = timed(sum_of_squares)

def sum_of_squares(n):
    """
    add 1*1 + 2*2 + 3*3 + ... + n*n
    """
    total = 0
    for num in range(n + 1):
        total += (num * num)
    return total
sum_of_squares = timed(sum_of_squares)

"""
^
totally the same as
v
"""

@timed
def sum_of_squares(n):
    """
    add 1*1 + 2*2 + 3*3 + ... + n*n
    """
    total = 0
    for num in range(n + 1):
        total += (num * num)
    return total


print(sum_of_squares(1000000))
print(product_of_squares(1000000))

"""
so that's decorators. What about app.route?

first thing to notice:
 - there's parens on @app.route('/')
"""

paths = {}

def route(path, handler):
    paths[path] = handler
    return handler

def index():
    return 'hello world'
route('/', index)

def best_cookie():
    return 'chocolate chip'
route('/best/cookie', best_cookie)

"""
improved!
"""


paths = {}

def route(path):
    def register_for_path(handler):
        paths[path] = handler
        return handler
    return register_for_path

def index():
    return 'hello world'
route('/')(index)

def best_cookie():
    return 'chocolate chip'
route('/best/cookie')(best_cookie)

"""
^
same as
v
"""

paths = {}

def route(path):
    def register_for_path(handler):
        paths[path] = handler
        return handler
    return register_for_path

route_to_slash = route('/')

def index():
    return 'hello world'
index = route_to_slash(index)

route_to_best_cookie = route('/best/cookie')
def best_cookie():
    return 'chocolate chip'
best_cookie = route_to_best_cookie(best_cookie)

"""
^
same as
v
"""
route_to_slash = route('/')

@route_to_slash
def index():
    return 'hello world'

route_to_best_cookie = route('/best/cookie')

@route_to_best_cookie
def best_cookie():
    return 'chocolate chip'

"""
^
same as
v
"""

@route('/')
def index():
    return 'hello world'

@route('/fav/cookie')
@route('/best/cookie')
def best_cookie():
    return 'chocolate chip'
