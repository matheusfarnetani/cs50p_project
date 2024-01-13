from .geometry import Geometry


class Ramp(Geometry):
    def __init__(self, height: float, width: float, length: float = 0, slope: float = 0):

        # Initialize Variables
        self.__height: float = self.validate_number(height, "Ramp: Height")
        self.__width: float = self.validate_number(width, "Ramp: Width")

        # Calculate slope or length
        if slope and not length:
            self.__slope: float = slope
            self.lack_length()
        elif length and not slope:
            self.__length: float = length
            self.lack_slope()
        else:
            raise KeyError("Initialize a ramp object with height, width and length or slope")

        # Creates Geometry
        super().__init__()

        # Calculates area and volume
        self.area = self.length * self.width
        self.volume = (1/2 * (self.length * self.height)) * self.width

    def __str__(self) -> str:
        return f"Ramp(height={self.height}, width={self.width}, length={self.length:.3f}, slope={self.slope}, {super().__str__()},"

    def lack_length(self) -> None:
        """
        Calculates the length of a ramp using the height and slope percentage.
        The function assumes that self.height and self.slope are already set.

        :raises ZeroDivisionError: If self.slope is 0, as it would result in division by zero.
        """
        try:
            self.__length: float = self.height / (self.slope / 100)
        except ZeroDivisionError:
            raise ZeroDivisionError("Slope cannot be zero for length calculation.")

    def lack_slope(self) -> None:
        """
        Calculates the slope percentage of a ramp using the height and length.

        The function assumes that self.height and self.length are already set.

        :raises ZeroDivisionError: If self.length is 0, as it would result in division by zero.
        """
        try:
            self.__slope: float = (self.height / self.length) * 100
        except ZeroDivisionError:
            raise ZeroDivisionError("Length cannot be zero for slope calculation.")

    @property
    def height(self) -> float:
        return self.__height

    @property
    def width(self) -> float:
        return self.__width

    @property
    def slope(self) -> float:
        return self.__slope

    @property
    def length(self) -> float:
        return self.__length
