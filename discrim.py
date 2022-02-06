import math


class FindTheRoots(object):

    def __init__(self):
        self.x2 = None
        self.x1 = None
        self.x = None
        self.discrim = None
        self.num3 = None
        self.num2 = None
        self.num1 = None

    def make(self):
        while True:
            self.num1, self.num2, self.num3 = map(float, [input('a is '), input('b is '), input('c is ')])
            self.discrim = (self.num2 ** 2) - 4 * self.num1 * self.num3
            if self.make_the_roots() is False:
                print('There is not solution')
            else:
                if self.x is None:
                    print(self.x1, self.x2)
                else:
                    print(self.x)

    def make_the_roots(self):
        if self.discrim < 0: return False
        if self.discrim == 0:
            self.x = -self.num2 / (2 * self.num1)
        if self.discrim > 0:
            self.x = None
            self.x1 = (-self.num2 + math.sqrt(self.discrim)) / (2 * self.num1)
            self.x2 = (-self.num2 - math.sqrt(self.discrim)) / (2 * self.num1)


if __name__ == '__main__':
    obj = FindTheRoots()
    obj.make()
