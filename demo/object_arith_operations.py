

class Point():
    """
        This example is used to define object arithmetic operations
        using builting numeric operations
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x={0}, y={1})'.format(self.x, self.y)

    # to support p1 + p2 operation
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # to support p1 - p2 operation
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    # to multiply two point p1*p2
    def __mul__(self, other):
        return Point(self.x * other.x, self.y*other.y)

    # inplace subtraction
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self


def main():
    p1 = Point(20, 30)
    p2 = Point(40, 60)
    print('Original = {0}, {1}'.format(p1, p2))

    # works after overriding __add__ function
    print('Addition = ', p1+p2)

    # subtracting two points
    print('Subtraction = ', p1-p2)

    # in-place addition
    # p1 += p2
    # print('In-place addition = ', p1)

    # in-place subtraction
    # p1 -= p2
    # print('in-place subtraction = ', p1)

    # multiplying two points
    print('Multiplication = ', p1*p2)


if __name__ == '__main__':
    main()
