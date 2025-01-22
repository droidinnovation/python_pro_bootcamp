
# *args: Many Positional Arguments
def add(*args):
    print(type(args))

    # _sum = 0
    # for n in args:
    #     _sum += n
    # return _sum

add(2,3,6,7,8)