from collections import Counter


def extracthours(item):
    return item[:2]


def main():

    # TODO: extract hours and make a dict of it counting number of occurences of hours
    l = ['02:22', '08:44', '11:00', '02:54', '08:01']

    # hours = map(extracthours, l)
    # Same thing for extraction of hours but with lambda expressions
    hours = map(lambda x: x[:2], l)

    result = {}
    # Same thing for uniquehours but with 'Counter' collection
    # result = Counter(hours)

    for hour in hours:
        if hour in result:
            result[hour] = result[hour] + 1
        else:
            result[hour] = 1

    # Same thing for counting hours occurences but with dict expressions
    # result = { k:v for k in hours   }

    print(result)


main()
