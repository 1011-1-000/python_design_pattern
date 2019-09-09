from functools import wraps


def decorate(func):

    @wraps(func)
    def decorated(*args, **kwargs):
        print("before run the function")
        r = func(*args, **kwargs)
        print("execute the function")
        print("after run the function")
        return r

    return decorated


@decorate
def add(a, b):
    return a + b


def test_decorator():
    print(add(1, 2))
