#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this function calculates area of octagon

import math


def main():
    # main function
    print("We will be calculating the area of octagon. ")
    # input
    side = int(input("Enter the side of octagon: "))
    # process
    area = 2 * (1 + (math.sqrt(2))) * side * side
    # output
    print("Area is {} mm²".format(area))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
