from math import inf
def true_divide(first, second):
    if second == 0:
        result = inf
    else:
        result = first / second
    return result

#print(true_divide(15, 0))