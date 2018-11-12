def main():
    nums = [2, 5, 3, 6, 7, 11]

    # TODO: grab numbers between 5 and 10 and square them
    # using normal map and filter
    # map function takes a func or lambda exp and the list (in this case a filter is applied to filter the list) as arguments
    # squared = list(
    #     map(lambda x: x**2, filter(lambda x: x >= 5 and x <= 10, nums)))

    # same above thing with 'list-comprehension'
    # filter using predicate
    squared = list([x**2 for x in nums if x >= 5 and x <= 10])

    print(squared)


if __name__ == '__main__':
    main()
