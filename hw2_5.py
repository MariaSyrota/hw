# def nsd(x, y):
#     if y == 0:
#         return x
#     else:
#         return nsd(y, x % y)



def nsd(a, b):
    if a == 0 or b == 0:
        return [a, b]

    if a >= 2 * b:
        return nsd(a - 2 * b, b)

    if b >= 2 * a:
        return nsd(a, b - 2 * a)

    return [a, b]
print(nsd(5, 7))