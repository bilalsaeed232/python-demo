from enum import Enum, auto, unique


class Days(Enum):
    SUNDAY = 1
    MONDAY = 2
    TUESDAY = 3
    WEDNESDAY = 4
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()

# can override for any class
    def __str__(self):
        return "Day of Week {0}".format(self.name)


def main():
    partyDay = Days.FRIDAY

    # by default print calls the __str__ method of object
    print(partyDay)

    print("Instance Test:", isinstance(partyDay, Days))

    # can iterate all enum values
    for day in Days:
        print(day)


if __name__ == '__main__':
    main()
