from collections import defaultdict


def main():
    # wants to count the number of time each item occurs
    colors = ['blue', 'orange', 'black', 'orange', 'blue']

    # without using defaultdict only normal dictionary
    colorCounter = {}

    for color in colors:
        if color in colorCounter:
            colorCounter[color] += 1
        else:
            colorCounter[color] = 1

    print(colorCounter)

    # with defaultdict
    # it takes a type like int provides default value for all keys
    # much more readable
    colorCounter = defaultdict(int)
    for color in colors:
        colorCounter[color] += 1

    print(colorCounter)

    # can also pass lambda expression as well for custom default values
    colorCounter = defaultdict(lambda: 200)
    for color in colors:
        colorCounter[color] += 1

    print(colorCounter)


main()
