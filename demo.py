import itertools


def filterEven(num):
    """
    used as a callback for filter function which filters out the even numbers from a list or sequence

    Parameters:
    num: current number passed by python filter function of list/sequence

    Return Value:
    boolean: returns either true or false based on the condition
    """
    if num % 2 == 0:
        return True
    return False


def filterOdd(num):
    if num % 2 == 0:
        return False
    return True


def main():
    ls = [2, 542, 1, 4, 0, 11]

    # i = iter(ls)
    # print(i)
    # with open('data.txt', 'r') as fp:
    #     for line in (iter(fp.readline, '')):
    #         print(line)

    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    chainList = itertools.chain(days, ls)
    # print(list(chainList))

    # for i, m in enumerate(zip(days, daysFr), start=1):
    #     print(i, m[0], ' in French: ', m[1])

    # num = iter(range(100, 1000, 10))
    # print(next(num))
    # print(next(num))
    # print(next(num))
    # print(next(num))
    # print(next(num))
    names = ['bilal', 'saeed', 'khan']

    cycle1 = itertools.cycle(names)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # for name in cycle1:
    #     print(name)

    print("Even Numbers:", list(filter(filterEven, ls)))
    print("Odd Numbers:", list(filter(filterOdd, ls)))
    print(filterEven.__doc__)
    print(filterOdd.__doc__)


main()
