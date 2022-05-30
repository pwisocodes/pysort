from functools import wraps
import logging
from time import time


def timing(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        ts = (time() * 1000)
        result = func(*args, **kwargs)
        te = (time() * 1000)
        logging.debug(
            f"Function: {func.__name__}, args: {args}, kwargs: {kwargs}, Execution Time: {te-ts} msec \n"
        )
        return result

    return wrap
