"""
Author: Sam Powell
Date: 13 May 2022

Small training ground for learning about strings.

The idea is to highlight strings. 
"""


from dataclasses import dataclass


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

    change_string(x)
    print(x)
    print()


def main() -> None:
    example_1()
    example_2()

if __name__ == "__main__":
    main()