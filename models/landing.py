from .geometry import Geometry


class Landing(Geometry):
    def __init__(self, length: float, width: float, height: float):
        # Initialize Variables
        self.__length: float = 0
        self.__width: float = 0
        self.__height: float = 0

        self.length = length
        # NBR 9077 - 4.6.2.3
        if self.length > 1.1:
            self.length = 1.1

        self.width = width
        self.height = height

        # Creates Geometry
        super().__init__()

        # Calculates area and volume
        self.area = self.length * self.width
        self.volume = self.length * self.width * self.height

    def __str__(self) -> str:
        return f"Landing(length={self.length}, width={self.width}, height={self.height:.3f}, {super().__str__()})"

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, n) -> None:
        self.__length = self.validate_number(n, "Length")

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n) -> None:
        self.__width = self.validate_number(n, "Width")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n) -> None:
        self.__height = self.validate_number(n, "Height")