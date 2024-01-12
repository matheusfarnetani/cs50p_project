import argparse

from models.ramp import Ramp


def main():
    height = float(input("Height: "))
    width = float(input("Width: "))
    slope = float(input("Slope: "))
    # length = float(input("Length: "))

    r = Ramp(height, width, slope=slope)
    # r = Ramp(height, width, length=length)
    print(r)


if __name__ == "__main__":
    main()