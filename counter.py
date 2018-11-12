from collections import Counter


def main():
    box1 = ['apple', 'orange', 'banana',
            'pineapple', 'mango', 'apple', 'banana']
    box2 = ['orange', 'apple', 'kiwi', 'pomgrenate', 'banana']

# create a counter class with values as total occurences
    c1 = Counter(box1)
    c2 = Counter(box2)
    print('box1', c1)

# combines both boxes
    c1.update(c2)
    print(c1)

# sum of both boxes values
# as c1 is has now both box1 and box2 items
    print(sum(c1.values()), ' total fruits in both boxes')

# first three most common fruit in both boxes
    print(c1.most_common(3), ' is most common in both boxes')

# remove box2 items from box1
    c1.subtract(c2)
# most common fruit in box1 only
    print(c1.most_common(3), ' most common fruit in box 1')


# both has these fruits common
    print(c1 & c2, ' exists in both boxes')


main()
