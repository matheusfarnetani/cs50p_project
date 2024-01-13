from .geometry import Geometry


class Ramp(Geometry):
    def __init__(self, height: float, width: float, length: float = 0, slope: float = 0):

        # Initialize Variables
        self.__height: float = 0
        self.__width: float = 0
        self.__length: float = 0
        self.__slope: float = 0

        # Assign Variables
        self.height = height
        self.width = width

        # Calculate slope or length
        if slope and not length:
            self.slope = slope
            self.lack_length()
        elif length and not slope:
            self.length = length
            self.lack_slope()
        else:
            raise KeyError("Initialize a ramp object with height, width and length or slope")

        # Creates Geometry
        super().__init__(self.length, self.width, self.height)

        # Calculates Geometry specific volume
        self.volume = (1/2 * (self.length * self.height)) * self.width

    def __str__(self) -> str:
        return f"Ramp(height={self.height}, width={self.width}, length={self.length}, slope={self.slope}, {super().__str__()},"

    def lack_length(self) -> None:
        """
        Calculates the length of a ramp using the height and slope percentage.

        The function assumes that self.height and self.slope are already set.

        :raises ZeroDivisionError: If self.slope is 0, as it would result in division by zero.
        """
        try:
            self.length = self.height / (self.slope / 100)
        except ZeroDivisionError:
            raise ZeroDivisionError("Slope cannot be zero for length calculation.")

    def lack_slope(self) -> None:
        """
        Calculates the slope percentage of a ramp using the height and length.

        The function assumes that self.height and self.length are already set.

        :raises ZeroDivisionError: If self.length is 0, as it would result in division by zero.
        """
        try:
            self.slope = (self.height / self.length) * 100
        except ZeroDivisionError:
            raise ZeroDivisionError("Length cannot be zero for slope calculation.")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n: int | float | str) -> None:
        self.__height = self.validate_number(n, "Height")

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n: int | float | str) -> None:
        self.__width = self.validate_number(n, "Width")

    @property
    def slope(self) -> float:
        return self.__slope

    @slope.setter
    def slope(self, n: int | float | str) -> None:
        self.__slope = self.validate_number(n, "Slope")

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, n: int | float | str) -> None:
        self.__length = self.validate_number(n, "Length")
