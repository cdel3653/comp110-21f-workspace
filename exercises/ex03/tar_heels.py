"""An exercise in remainders and boolean logic."""

__author__ = "730320843"


int_prompt = int(input("Enter an int: "))
if int_prompt % 2 != 0 and int_prompt % 7 != 0:
    print("CAROLINA")
if int_prompt % 2 == 0:
    print("TAR ", end="")
if int_prompt % 7 == 0:
    print("HEELS")