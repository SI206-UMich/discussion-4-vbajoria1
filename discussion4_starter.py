class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE
    #declaring all parts of self
    def __init__(self,width,height):
        self.width = width
        self.height = height

    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)

    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise
    #checking if input is valid
    def verify_input(self):
        isPositive = False
        if self.width > 0 and self.height > 0:
            isPositive = True
        return isPositive

    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.
    #calculating area
    def area(self):
        if Rectangle.verify_input(self) == False:
            return "Invalid input"
        else:
            return self.width * self.height


    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    def perimeter(self):
        if Rectangle.verify_input(self) == False:
            return "Invalid input"
        else:
            return self.width + self.height + self.width + self.height
    

#execution of functions
def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()