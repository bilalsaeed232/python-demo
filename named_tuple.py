import collections


def main():
    # best for not using whole class structure for simple types
    # x y are the custom properties provided for user defined namedtuple
    Viewport = collections.namedtuple("Viewport", "x y")

    # can create different objects passing different values just like normal class
    p1 = Viewport(x=10, y=20)
    p2 = Viewport(100, 50)

    print(p1, p2)
    p1 = p1._replace(x=20)
    print(p1)


main()
