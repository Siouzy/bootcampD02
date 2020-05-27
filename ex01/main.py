class ObjectC(object):
    def __init__(self):
        pass


def what_are_the_vars(*arg, **kwarg):
    obj = ObjectC()
    index = 0
    var_format = 'var_{:d}'
    for k, w in kwarg.items():
        obj.__setattr__(k, w)
    for a in arg:
        key = var_format.format(index)
        if key in kwarg.keys():
            return
        obj.__setattr__(key, a)
        index += 1
    return obj


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
