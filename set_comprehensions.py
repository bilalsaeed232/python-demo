def main():
    # TODO: extract unique characters into a set
    text = "The quick brown fox jumps over the lazy dog"

    # note: if '{}' are used without key value pair format it is considered a set
    # to exclude whitespace use builtin function 'isspace()' in predicate expression
    uniqueChars = {t.upper() for t in text if not t.isspace()}

    print(sorted(uniqueChars))
    print(len(uniqueChars))


if __name__ == '__main__':
    main()
