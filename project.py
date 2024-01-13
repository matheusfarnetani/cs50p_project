import argparse

from models.ramp import Ramp
from models.landing import Landing
from models.accessible_ramp import AccessibleRamp


def main():
    # print("Landing:")
    # height = float(input("Height: "))
    # width = float(input("Width: "))
    # length = float(input("Length: "))
    # l = Landing(length, width, height)
    # print(l)

    # print("Ramp:")
    # height = float(input("Height: "))
    # width = float(input("Width: "))
    # slope = float(input("Slope: "))
    # r = Ramp(height, width, slope=slope)
    # print(r)

    print("Accessible Ramp:")
    height = float(input("Height: "))
    width = float(input("Width: "))
    slope = float(input("Slope: "))
    ar = AccessibleRamp(height, width,"COM-C", slope)
    print(ar)

if __name__ == "__main__":
    main()
