
# Object.method()
# However, math.sqrt() is from a library, so not an object
# str(55) is calling the initializer for the string class


# Terminology:

# Class: a template for making a new object of a given type (like an int, str) but programmer defines the type

# Instance: an object made from a class is an /instance/ of that class (student_name is an instance of a string)

# Using a class, a programmer can "stamp" create instances (infinite number of them), like a cookie cutter

class Rectangle:
    def __init__(self, height=1, width=1, color='gray'):

        if type(color) != str:
            raise TypeError("Not a String!")

        self.height = height
        self.width = width
        self.color = color

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_area(self):
        return self.height * self.width

    def __str__(self):
        return 'height: ' + str(self.height) + ", width: " + str(self.width) + ", color: " + str(self.color)


def main():

    try:
        rect1 = Rectangle(5, 10, 1)
    except TypeError as type_error:
        print("That's not a color! The error is:", type_error)
    else:
        print(rect1)
        print('rect1 has an area of:', rect1.get_area())
    finally:
        print('Goodbye.')


if __name__ == "__main__":
    main()

