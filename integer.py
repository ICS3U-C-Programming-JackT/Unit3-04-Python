#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 19th, 2025

# Integer relation to 0 program in python

import random


def main():
    # Variables for user number
    user_number = int(input("Enter a number here: "))

    # If Statements to display the numbers relation to 0
    if user_number < 0:
        print("Your number is less than 0")
    elif user_number > 0:
        print("Your number is greater than 0")
    else:
        print("Your number is 0")


if __name__ == "__main__":
    main()
