from .geometry import Geometry


class Landing(Geometry):
    def __init__(self, length: float, width: float, height: float):

        # Initialize Variables
        self.__length = 0
        self.__width = 0
        self.__height = 0

        # Assign Variables
        self.length = length
        self.width = width
        self.height = height

        # Creates Geometry
        super().__init__(self.length, self.width, self.height)

    def __str__(self) -> str:
        return f"Landing(length={self.length}, width={self.width}, height={self.height}, {super().__str__()})"

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, n: int | float | str) -> None:
        self.__length = self.validate_number(n, "Length")

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n: int | float | str) -> None:
        self.__width = self.validate_number(n, "Width")

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n: int | float | str) -> None:
        self.__height = self.validate_number(n, "Height")
