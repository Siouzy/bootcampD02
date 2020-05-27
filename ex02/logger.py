import time
from random import randint
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


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
