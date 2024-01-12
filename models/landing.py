from .geometry import Geometry


class Landing(Geometry):
    def __init__(self, length: float, width: float, height: float):
        self.__length = 0
        self.__width = 0
        self.__height = 0

    def __str__(self) -> str:
        return f"Landing(length={self.length}, width={self.width}, height={self.height}, {super().__str__()}, {__name__})"

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, n) -> None:
        self.validate_number(n, "Length")
        self.__length = n

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n) -> None:
        self.validate_number(n, "Width")
        self.__width = n

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n) -> None:
        self.validate_number(n, "Height")
        self.__height = n
