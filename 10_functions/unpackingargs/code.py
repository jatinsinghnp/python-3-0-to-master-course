def multiple(*args):
    total = 1
    for arg in args:
        total = total+arg
    return total


def apply(*args, operator):
    if operator == "*":
        return multiple(args)
    elif operator == '+':
        return sum(args)
    else:
        return "no valid operator provided to apply()"


print(apply(1, 2, 3, 4,operator="+"))
