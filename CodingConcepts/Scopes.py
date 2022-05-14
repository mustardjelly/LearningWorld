"""
Author: Sam Powell
Date: 13 May 2022

Small training ground for learning about variable scope.

The idea is to highlight how to determine when a variable is in scope. 
"""

# Scopes

from typing import Any


def example_1() -> None:
    """Simple scope example. We must define variables before we call them."""
    function_name = "Example 1"
    print(f">>> {function_name}")

    # Fails because x is undefined
    try:
        print(x)
    except NameError as e:
        # catch the exception so execution can continue.
        print (e)
        pass

    x = "Hello World"
    # Passes because x has been defined.
    print(x)
    print(f"<<< {function_name}", end="\n\n")


def example_2() -> None:
    """Scope is inherited. This means unindented code is inhertied by indented
    code. 
    
    Example:
        |---x = 1
        |-------# x is defined at this tabbing
        |# x is not defined at this tabbing

    
    
    When we use functions, variables defined before the function call
    will be inherited.

    Example:
        x = 1

        def printer():
            print(x)
            print(y)

        y = 2

        printer()
        # 1
        # 2
    
    """
    function_name = "Example 2"
    print(f">>> {function_name}")

    def print_x() -> None:
        print(x)

    # This fails because x is not in scope when the function print_x() is called.
    try:
        print(x)
    except NameError as e:
        # catch the exception so execution can continue.
        print (e)
        pass

    x = 'Hello World'

    # This works, x is in scope and has been defined before print_x is called.
    print_x()
    print(f"<<< {function_name}", end="\n\n")


def example_3() -> None:
    """We can pass variables into functions. Variables are defined for the
    scope of the function."""
    function_name = "Example 3"
    print(f">>> {function_name}")

    def print_var(x: str) -> None:
        """Prints a passed in string.
        
        x is defined as the argument passed to this function.
        """
        x_exists = x is not None
        print(f"x is defined: {x_exists}")
        if x_exists:
            print(x)

    # We pass a hard coded string "Hello World"
    print_var("Hello World")

    # Define a variable y
    y = "y variable"

    # Pass y into function
    # y is mapped to x in the function, and then is printed.
    print_var(y)

    # This fails to print. We have never defined x at this tabbing leve (1 tab).
    # x only ever existed in the print_var method. When we exist print_var, x is
    # deconstructed.
    try:
        print(x)
    except NameError as e:
        # catch the exception so execution can continue.
        print (e)
        pass
    print(f"<<< {function_name}", end="\n\n")


def example_4() -> None:
    """Variables created in a method."""
    
    function_name = "Example 4"
    print(f">>> {function_name}")

    def make_variables() -> None:
        x = "make_variables"
        global y 
        y = "make_variables"

        # Internal to the function, print variables to show they are defined:
        print("Inside make_variables")
        print(f"x: {x}")
        print(f"y: {y}")

    make_variables()
    
    print("Outside make_variables")
    # We cannot do this. x has never been defined.
    # print(x)

    # This works because y was declared global. This means all methods can 
    # access this variable. This may seem good but it does have performance
    # implications.
    print(f"y: {y}")

    print(f"<<< {function_name}", end="\n\n")


def example_5() -> None:
    """Pass a variable into a method and exhibit and consume its return value.
    """
    function_name = "Example 5"
    print(f">>> {function_name}")

    def define_variable(y) -> Any:
        """Takes a parameter y,
        sets it to an internally scoped variable z,
        and then return z.
        """
        z = y

        return z

    # Define a variable outside
    x = "x defined outside"
    
    # Pass it into a method, and that method returns a value. Assign that 
    # returned value outside the method and print it.
    return_value = define_variable(x)
    print(f"Printing return value outside: '{return_value}'")

    print(f"<<< {function_name}", end="\n\n")



def main():
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()

if __name__ == "__main__":
    main()