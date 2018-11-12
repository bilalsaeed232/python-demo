class MyColor():
    def __init__(self):
        self.red = 22
        self.green = 120
        self.blue = 88

# called e.g when object of this class used in print()
    def __str__(self):
        return "Color (red={0}, green={1}, blue={2})".format(self.red, self.green, self.blue)

# called when any attribute is not found by default
    def __getattr__(self, attr):
        if(attr == 'rgb'):
            return "({0},{1},{2})".format(self.red, self.green, self.blue)
        elif(attr == 'hex'):
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError(
                'There is not attribute like: {0}'.format(attr))

# called everytime you want to set an attribute
# useful for computed attributes
    def __setattr__(self, name, value):
        if(name == 'rgb'):
            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]
        else:
            # always mention call to super() otherwise __init__ will not work for default values
            super().__setattr__(name, value)


# always provide "dir" implemenation for other developers to see what kind of attributes are supported


    def __dir__(self):
        return ("red", "green", "blue", "rgb", "hex")


def main():
    color = MyColor()

    print("Your Color object is: ", color, end="\n")

    print("RGB: ", color.rgb)
    print("Hex: ", color.hex)

    print('---------')
    print('After attributes modified')
    color.rgb = (100, 200, 120)

    print("Red:", color.red)
    print("RGB:", color.rgb)
    print("Hex:", color.hex)

    # "dir" is used to print attributes on the object
    print("Dir:", dir(color))


if __name__ == '__main__':
    main()
