# * defines that this is keyarg and
# should be mentioned while calling this function


def substring(s, start, *, end=0):
    result = ""
    for ss in range(start, end):
        result += s[ss]

    print(s, start, end)
    return result


def main():
    text = "My name is Bilal"
    print(substring(text, 11, end=len(text)))


main()
