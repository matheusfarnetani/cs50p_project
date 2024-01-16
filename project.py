import argparse
import sys

from models.accessible_ramp import AccessibleRamp

MAX_HEIGHT_START = 1
MAX_HEIGHT_INCREMENT = 0.5
MAX_SLOPE_START = 5
MAX_SLOPE_INCREMENT = 0.2


def main():
    args = arguments()
    
    height = args.height if args.height else get_float("Height: ")
    width = args.width if args.width else get_float("Width: ")
    slope = args.slope if args.slope else get_float("Slope: ")
    option = args.opt if args.opt else input("Option: ").upper()

    max_height = max_possible_height(width, slope, MAX_HEIGHT_START, MAX_HEIGHT_INCREMENT)
    print(f"In a total, {len(max_height)} ramps were calculated.",
          f"\nThe count started from {MAX_HEIGHT_START:.2f}m and was incremented, within each loop, by {MAX_HEIGHT_INCREMENT:.2f}m"
          f"\nThe last ramp calculated, with a slope of {slope:.2f}%, has a height of {max_height[-1].height:.2f}m"
    )

    print("")

    max_slope = max_possible_slope(height, width, MAX_SLOPE_START, MAX_SLOPE_INCREMENT)
    print(f"In a total, {len(max_slope)} ramps were calculated.",
          f"\nThe count started from {MAX_SLOPE_START:.2f}% and was incremented, within each loop, by {MAX_SLOPE_INCREMENT:.2f}%",
          f"\nThe last ramp calculated, with a height of {height:.2f}m, has a slope of {max_slope[-1].slope:.2f}%"
    )

    ar = AccessibleRamp(height, width, option, slope)

    print("\n", ar)

def max_possible_height(width: float, slope: float, start: float, increment: float) -> list:
    results = list()
    height = start
    while True:
        try:
            results.append(AccessibleRamp(height=height, width=width, slope=slope))
        except ValueError:
            break
        height += increment
    return results


def max_possible_slope(height: float, width: float, start: float, increment: float) -> list:
    results = list()
    slope = start
    while True:
        try:
            results.append(AccessibleRamp(height=height, width=width, slope=slope))
        except ValueError:
            break
        slope += increment
    return results


def arguments():
    parser = argparse.ArgumentParser(
        description="Calculates values for a accessible ramp, following the standard ABNT NBR 9050:2020"
    )
    parser.add_argument(
        "-v, --version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    parser.add_argument(
        "-o, --option",
        type=str,
        help=" See ABNT NBR 9050:2020 6.6.2.1 and 6.6.2.2. 'COM' means 'common' and, 'exp', 'exception'. The default is 'COM-C'",
        choices=["COM-A", "COM-B", "COM-C", "EXP-A", "EXP-B"],
        dest="opt"
    )
    parser.add_argument(
        "--height",
        type=float,
        help="define value for height",
        dest="height"
    )
    parser.add_argument(
        "-w, --width",
        type=float,
        help="define value for width",
        dest="width"
    )
    parser.add_argument(
        "-s, --slope",
        type=float,
        help="define value for slope",
        dest="slope"
    )

    return parser.parse_args()


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
