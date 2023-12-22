#!/usr/bin/python
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over each alemant in my_list
    for item in my_list:

        # Check if the element is an integer
        if isinstance(item, int):
