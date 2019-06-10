# *args and **kwargs
# Pass multiple arguments and Keyword arguments



# *args is a tuple
# args is unpacked tuple
def summation(*args):
    # print(type(args))
    # print(args, *args)

    sum = 0
    for arg in args:
        sum += arg

    return sum


def

print(summation(1, 2, 50, 100))