from functools import wraps
from time import sleep


def meh(fn=None, *a, **kw):
    if a or kw:
        return meh_with(*a, **kw)
    return gimme(None)(fn)


def meh_with(*a, **kw):
    return gimme(None, *a, **kw)


def gimme(value, *a, **kw):
    def default(*a, **kw):
        return value

    return maybe(default, *a, **kw)


def again(call_limit, when=Exception, backoff=0):
    def wrapper(fn):
        @wraps(fn)
        def wrapped(*a, **kw):
            calls = 0
            while True:
                calls += 1
                try:
                    return fn(*a, **kw)
                except when as e:
                    if calls >= call_limit:
                        raise
                    sleep(backoff)

        return wrapped

    return wrapper


def maybe(default, when=Exception):
    def wrapper(fn):
        @wraps(fn)
        def wrapped(*a, **kw):
            try:
                return fn(*a, **kw)
            except when as e:
                return default(*a, **kw)

        return wrapped

    return wrapper
