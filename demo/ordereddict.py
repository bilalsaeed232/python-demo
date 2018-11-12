from collections import OrderedDict


def main():
    a = {"a": 1, "b": 5, "c": 0}
    b = {"a": 1, "c": 0, "b": 5}

    print("a = ", a, " b = ", b)

    # check if both a and sortedcol are equal
    print("Equality test:", a == b)


# now using OrderedDict
    sortedColR = sorted(a, key=lambda t: t, reverse=True)

    od1 = OrderedDict(sortedColR)

    print("od1 = ", od1)


main()
