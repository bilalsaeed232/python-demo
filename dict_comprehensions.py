def main():

    box1 = {'apples': 3, 'oranges': 2, 'banana': 4}
    box2 = {'strawberries': 1, 'lemons': 10}

    # using dictionary-comprehensions to combine both dicts
    # the order of execution is first for, then second for then it comes to k:v
    # should not be more complicated than two expressions
    box = {k: v for fruit in (box1, box2) for k, v in fruit.items()}
    print(box)


if __name__ == '__main__':
    main()
