def fToC(t):
    return (t-32)*5/9


def cToF(t):
    return (t*9/5)+32


def main():
    ftemp = [200, 300, 100, 250]
    ctemp = [25, 50, 49, 70]

# without using lambda
    print(map(fToC, ftemp))
    print(map(cToF, ctemp))

# same thing with lambda functions
    print(map(lambda t: (t-32)*5/9, ftemp))
    print(map(lambda t: (t*9/5)+32, ctemp))


main()
