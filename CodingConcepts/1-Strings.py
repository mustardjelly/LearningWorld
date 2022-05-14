"""
Author: Sam Powell
Date: 13 May 2022

Small training ground for learning about strings.

The idea is to highlight strings. 
"""


SEPARATOR = "---"

    
def example_1() -> None:
    print("Example 1:")

    try:
        print(x)
    except NameError as ne:
        error_message = f"Could not print 'x': {ne}"
        print(error_message)
        print(SEPARATOR)

    x = "I am a string"
    print (f"printing x: {x}")
    print(SEPARATOR)

    x = "I have been changed"
    print (f"printing x: {x}")

    print()

    
def example_2() -> None:
    print("Example 2:")
    x = "I am a string"
    print(f"example_2_x: {x}")

    def change_string(x):
        x = "CHANGED"
        print(f"change_string_x: {x}")

    # What will be printed?
    # I am string
    # CHANGED

    # Answer:
    # 'I am string' will be printed
    # We are print the value of x in scope.
    # When we pass x into change_string, a new variable is created. 
    # 
    # Think of this as changed_string_x. When we assign 'CHANGED' we are setting 
    # changed_string_x to 'CHANGED', not example_2_x. 
    #
    # When we print, we print example_2_x.

    print(change_string(x)) # Prints None because no value is returned
    print(SEPARATOR)

    print(x)
    print()

def example_3() -> None:
    print("Example 3:")

    x = "I am a string"
    print(f"example_3_x: {x}")
    print(SEPARATOR)

    def change_string(y):
        y = "CHANGED"
        print(f"change_string_x: {y}")
        print(SEPARATOR)

        return y

    x = change_string(x)

    # What will be printed?
    # I am string
    # CHANGED

    # Answer:
    # 'CHANGED' will be printed
    # We are print the value of x in scope.
    # When we pass x into change_string, a new variable is created.
    # This new variable is returned out of our method.
    # This returned value is assigned to x.
    # x is now printed.

    print(f"example_3_x: {x}")

    print()


def example_4() -> None:
    """Strings are immutable (cannot be modified)."""
    print("Example 4:")
    x = "x" # point variable x at string 'x'
    y = x # point variable y at the string variable x is poiinting at, this is string 'x'

    print(f"x: {x}")
    print(f"y: {y}")
    print(SEPARATOR)

    print("Sameness checks")
    x_is_y = x is y # This is true. There is only one 'x' string object ever.
    x_equals_y = x == y # This is true, their values are the same.
    print(f"x_is_y: {x_is_y}")
    print(f"x_equals_y: {x_equals_y}")
    print(SEPARATOR)


    print("Assign 'new value' to x")
    x = "new value"

    print(f"x: {x}")
    print(f"y: {y}")
    print(SEPARATOR)

    print("Sameness checks")
    x_is_y = x is y # This is false, they point at different string objects
    x_equals_y = x == y # This is false, they are not the same value
    print(f"x_is_y: {x_is_y}")
    print(f"x_equals_y: {x_equals_y}")

    print()


def example_5() -> None:
    """Strings are immutable (cannot be modified)."""
    print("Example 5:")
    x = "x" # point variable x at string 'x'
    y = x # point variable y at the string variable x is poiinting at, this is string 'x'
    z = 'x'

    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")
    print(SEPARATOR)

    print("Sameness checks")
    x_is_y = x is y # This is true. There is only one 'x' string object ever.
    x_is_z = x is z # This is true. There is only one 'x' string object ever.
    x_equals_y = x == y # This is true, their values are the same.
    x_equals_z = x == z # This is true, their values are the same.
    print(f"x_is_y: {x_is_y}")
    print(f"x_is_z: {x_is_z}")
    print(f"x_equals_y: {x_equals_y}")
    print(f"x_equals_z: {x_equals_z}")
    print(SEPARATOR)


    print("Assign 'new value' to x")
    x = "new value"
    print(SEPARATOR)

    print(f"x: {x}")
    print(f"y: {y}")

    print()


def main() -> None:
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()

if __name__ == "__main__":
    main()