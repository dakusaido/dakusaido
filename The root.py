import math


def find_disc(n1, n2, n3):
    discriminant = int((n2 ** 2) - (4 * n1 * n3))
    print(discriminant)
    if discriminant < 0: return 'There is no solution'
    if discriminant > 0: return f'x1 = {(-n2 + math.sqrt(make_sqrt(discriminant))) / (2 * n1)}\nx2 = {(-n2 - math.sqrt(make_sqrt(discriminant))) / (2 * n1)}\n '
    if discriminant == 0: return f'x1 = {-n2 / (n1 * 2)}\n'


def make_sqrt(discrim):
    if math.sqrt(discrim) == round(math.sqrt(discrim)): return discrim
    aa = 0
    for x in range(2, round(math.sqrt(discrim))):
        if discrim % x == 0: aa = 1
    if aa == 0:
        return discrim


while True:
    try:
        num1, num2, num3 = map(float, [input('a is '), input('b is '), input('c is ')])
        print(find_disc(num1, num2, num3))

    except:
        print('Add int!!!')
