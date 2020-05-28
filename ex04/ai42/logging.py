import time
import os
import getpass
from timeit import timeit


def log(func):
    user = getpass.getuser()
    funct_name = func.__name__.replace('_', ' ').title()
    format_str = '({:s})Running: {: <18s} [ exec-time = {:.3f} {:s} ]\n'

    def wrapper_log(*args, **kwargs):

        ts = time.time() * 1000.0
        result = func(*args, **kwargs)
        te = time.time() * 1000.0
        exec_time = te - ts
        char_time = 'ms'
        if exec_time >= 1000.:
            exec_time /= 1000.
            char_time = 's '
        file = open('machine.log', 'a')
        file.write(format_str.format(user, funct_name, exec_time, char_time))
        file.close()
        return result

    return wrapper_log
