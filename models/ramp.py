from .geometry import Geometry


class Ramp(Geometry):
    def __init__(self, height: float | int, width: float | int, length: float | int = 0, slope: float | int = 0):
        self.__height: float = 0
        self.__width: float = 0
        self.__length: float = 0
        self.__slope: float = 0

        self.height = height
        self.width = width

        # i = (h/d) x 100
        if slope and not length:
            self.slope = slope
            self.length = self.lack_length(self.height, self.slope)
        elif length and not slope:
            self.length = length
            self.slope = self.lack_slope(self.height, self.length)
        else:
            raise KeyError("Initialize a ramp object with height, width and length or slope")

        super().__init__(self.length, self.width, self.height)
        self.area = self.length * self.width
        self.volume = (1/2 * (self.length * self.height)) * self.width

    def __str__(self) -> str:
        return f"Ramp(height={self.height}, width={self.width}, length={self.length}, slope={self.slope}, {super().__str__()},"

    def lack_length(self, height: float, slope: float) -> float:
        return height / (slope / 100)

    def lack_slope(self, height: float, length: float) -> float:
        return (height / length) * 100

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n: float) -> None:
        self.validate_number(n, "Height")
        self.__height = n

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n: float) -> None:
        self.validate_number(n, "Width")
        self.__width = n

    @property
    def slope(self) -> float:
        return self.__slope

    @slope.setter
    def slope(self, n: float) -> None:
        self.validate_number(n, "Slope")
        self.__slope = n

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, n: float) -> None:
        self.validate_number(n, "Length")
        self.__length = n
