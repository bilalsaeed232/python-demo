def addition(*args):
    result = 0
    for arg in args:
        result += arg

    return result


def main():
    l = [2, 6, 1]
    print(addition(*l))


main()
