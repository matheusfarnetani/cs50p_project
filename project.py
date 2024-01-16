import argparse

from models.accessible_ramp import AccessibleRamp


def main():
    args = arguments()
    print(args.opt if args.opt else "")
    print(args.height if args.height else "")
    print(args.width if args.width else "")
    print(args.slope if args.slope else "")

    height = get_float("Height: ")
    width = get_float("Width: ")
    slope = get_float("Slope: ")

    ar = AccessibleRamp(height, width, "COM-C", slope)

    print(ar)


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
        default="COM-C",
        help="for ramps in new constructions",
        choices=["COM-A", "COM-B", "COM-C", "EXP-A", "EXP-B"],
        dest="opt"
    )
    parser.add_argument(
        "-he --height",
        type=float,
        default=1,
        help="define value for height",
        dest="height"
    )
    parser.add_argument(
        "-w, --width",
        type=float,
        default=1.2,
        help="define value for width",
        dest="width"
    )
    parser.add_argument(
        "-s, --slope",
        type=float,
        default=8.33,
        help="define value for slope",
        dest="slope"
    )

    return parser.parse_args()


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            continue


if __name__ == "__main__":
    main()
