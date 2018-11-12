class Employee():
    def __init__(self, fname, lname, certs, experience):
        self.fname = fname
        self.lname = lname
        self.certs = certs
        self.experience = experience

    # to compensate '>' between the objects of this same class
    # based on 'experience' & 'certification' if experience is same
    def __gt__(self, other):
        if self.experience == other.experience:
            return self.certs > other.certs
        return self.experience > other.experience

    def __repr__(self):
        return 'Employee({0},{1},{2},{3})'.format(self.fname, self.lname, self.certs, self.experience)


def main():
    e = []
    e.append(Employee('adamn', 'william', 700, 2))
    e.append(Employee('bilal', 'saeed', 100, 5))
    e.append(Employee('john', 'doe', 20, 6))
    e.append(Employee('james', 'williamson', 100, 6))

    # only possible if we have __gt__ func implemented in Employee class
    # 'bilal' is senior than 'john'?
    print('Bilal is senior than john?', e[1] > e[2])
    print('James is senior than john?', e[3] < e[2])

    # can also be helpful in sorting
    seniorEmployees = reversed(sorted(e))

    for employee in seniorEmployees:
        print(employee.fname)


if __name__ == '__main__':
    main()
