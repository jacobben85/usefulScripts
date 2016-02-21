arr = [1, 3, 5, 9, 11, 22, 122, 100, 66317]


def decide(y):
    print('y=', y)
    z = y
    while z % 3 != 0:
        z -= 5
        if z < 0:
            return '-1'
        else:
            return z * '5' + (y - z) * '3'
    else:
        return y * '5'


for x in arr:
    print(decide(x))
