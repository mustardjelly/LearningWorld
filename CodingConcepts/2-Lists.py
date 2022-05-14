"""
Author: Sam Powell
Date: 13 May 2022

Small training ground for learning about lists.

The idea is to highlight lists. 
"""


SEPARATOR = "---"


def example_1() -> None:
    """Create a simple list."""
    print("Example 1")

    numbered_list = [1, 2, 3]
    string_list = ['a', 'b', 'c']
    mixed_list = [1, 'a', 2, 'b']
    range_list = list(range(10))

    print(f"numbered_list: {numbered_list}")
    print(f"string_list: {string_list}")
    print(f"mixed_list: {mixed_list}")
    print(f"range_list: {range_list}")

    print()


def example_2() -> None:
    """Iterate (cycle) through a list."""
    print("Example 2")

    mixed_list = [1, 'a', 2, 'b']

    print(f"mixed_list: {mixed_list}")

    for value in mixed_list:
        print(f"value: {value}")

    print()


def example_3() -> None:
    """Looped logic.
    
    Only print strings.
    """
    print("Example 3")

    mixed_list = [1, 'a', 2, 'b']

    print(f"mixed_list: {mixed_list}")

    for value in mixed_list:
        if isinstance(value, int):
            # Go to next value in mixed list (break)
            # Stop excuting this iteration of the loop.
            continue
        
        print(f"value: {value}")

    print()


def example_4() -> None:
    """Adding values.
    Mutating (changing) a list.
    """
    print("Example 4")

    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")

    # Add 4 to the end of our list
    numbered_list.append(4)

    print(f"appended_list: {numbered_list}")

    print()


def example_5() -> None:
    """Getting values.
    """
    print("Example 5")
    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")


    for i in range(3):
        print(f"index {i}: {numbered_list[i]}")

    print()


def example_6() -> None:
    """Removing values.
    """
    print("Example 6")
    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")

    # We want to remove the 3
    # 3 sits at index 2. Coders count from 0.
    index = 2
    print(f"Value at Index 2: {numbered_list[index]}")

    numbered_list.pop(index)
    print(f"popped_list: {numbered_list}")

    print()


def example_7() -> None:
    """Removing non-existent values.
    """
    print("Example 7")
    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")

    # We want to remove the 3
    # 3 sits at index 2. Coders count from 0.
    # We forget this and try to remove the 3 from the 3rd value in the list.
    index = 3 # This is a mistake!
    try:
        value = numbered_list[index]
    except IndexError as ie:
        # except prevents code from stopping
        print(f"exception: {ie}")


    try:
        numbered_list.pop(index)
    except IndexError as ie:
        # except prevents code from stopping
        print(f"exception: {ie}")

    print(f"nothing modified: {numbered_list}")

    print()


def example_8() -> None:
    """Lists are MUTABLE (subject to change).
    """
    print("Example 8")
    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")
    print(SEPARATOR)

    # Assign copy_list to numbered list. This means 2 variables
    # point at the same list in memory.
    #
    # numbered_list -> space in computer memory
    # a_list = numbered_list
    # a_list -> the same space in computer memory
    print(f"Setting copy_list = numbered_list")
    copy_list = numbered_list
    print(f"copy_list: {copy_list}")
    print(f"numbered_list: {numbered_list}")
    same_check = copy_list is numbered_list
    print(f"copy_list is numbered_list: {same_check}")
    print(SEPARATOR)
    
    # Changes to either list affect them both. They point at the same object
    # in memory.
    print("Append 4 to copy_list")
    copy_list.append(4)
    print(SEPARATOR)
    
    print(f"modified numbered_list: {numbered_list}")
    print(f"modified copy_list: {copy_list}")

    print()


def example_9() -> None:
    """Lists are MUTABLE (subject to change).
    """
    print("Example 9")
    numbered_list = [1, 2, 3]
    print(f"numbered_list: {numbered_list}")

    # Make a method to change our list
    def list_changer(a_list: list) -> None:
        """Takes a list and adds a value to the end."""
        thing_to_add = 4
        a_list.append(thing_to_add)

        # no return

    # This method can change our list, even though it feels out of scope.
    # This is because lists are mutable (subject to change).
    # This of this computer trick like this.
    #
    # numbered_list -> space in computer memory
    # a_list = numbered_list
    # a_list -> the same space in computer memory
    #
    # Changes to either list affect them both. They point at the same object
    # in memory.
    list_changer(numbered_list)
    print(f"modified_list: {numbered_list}")

    print()


def example_10() -> None:
    """is vs ==
    
    When we assign an existing list to a variable, it is like we have
    given that list two names.
    a = []
    b = a
    a is b because they are the same list object
    a == b because they lists look the same
    a's list has two names, a, or b. Either can be used to modify the same list.

    When we create two lists which are the same, however they are different objects.
    a = []
    b = []
    a is not b because they are not the same list object
    a == b because the lists look the same
    """
    print("Example 10")

    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a

    print("Current lists")
    print(f"list_a: {list_a}")
    print(f"list_b: {list_b}")
    print(f"list_c: {list_c}")
    print(SEPARATOR)

    print("Same checks")
    a_is_b = list_a is list_b
    a_is_c = list_a is list_c
    print(f"a_is_b: {a_is_b}")
    print(f"a_is_c: {a_is_c}")
    print(SEPARATOR)

    print("Equal checks")
    a_equals_b = list_a == list_b
    a_equals_c = list_a == list_c
    print(f"a_equals_b: {a_equals_b}")
    print(f"a_equals_c: {a_equals_c}")

    print()


def example_11():
    """is vs ==
    What happens we we change objects which are the same?
    
    When we assign an existing list to a variable, it is like we have
    given that list two names.
    a = []
    b = a
    a is b because they are the same list object
    a == b because they lists look the same
    a's list has two names, a, or b. Either can be used to modify the same list.

    When we create two lists which are the same, however they are different objects.
    a = []
    b = []
    a is not b because they are not the same list object
    a == b because the lists look the same
    """
    print("Example 11")

    list_a = [1, 2, 3] # a's list
    list_b = [1, 2, 3] # b's list
    list_c = list_a # a's list (called list_a and list_c)

    print("Current lists")
    print(f"list_a: {list_a}")
    print(f"list_b: {list_b}")
    print(f"list_c: {list_c}")
    print(SEPARATOR)

    print("Append 4 to list_a")
    list_a.append(4)
    # Since list_a and c are the same list, they are both modified.
    # list_b looks like list a, but it is not the same object. It is a new
    # object that looks the same. Therefore it is not modified by appending.
    print(f"list_a: {list_a}")
    print(f"list_b: {list_b}")
    print(f"list_c: {list_c}")
    print(SEPARATOR)

    print("Same checks")
    a_is_b = list_a is list_b
    a_is_c = list_a is list_c
    print(f"a_is_b: {a_is_b}")
    print(f"a_is_c: {a_is_c}")
    print(SEPARATOR)

    print("Equal checks")
    a_equals_b = list_a == list_b
    a_equals_c = list_a == list_c
    print(f"a_equals_b: {a_equals_b}")
    print(f"a_equals_c: {a_equals_c}")

    print()


def main() -> None:
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()
    example_6()
    example_7()
    example_8()
    example_9()
    example_10()
    example_11()


if __name__ == "__main__":
    main()