import collections


def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError('Parameter must be iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('Elements must be numeric')
        total += v
    return total

vals = [1,2,3,4,6.7,5]
print(sum(vals))