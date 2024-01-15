from .geometry import Geometry


class Landing(Geometry):
    def __init__(self, length: float, width: float, height: float):
        # Initialize Variables
        self.__length: float = (
            self.validate_number(length, "Landing: Length") if length > 1.1 else 1.1
        )  # NBR 9077 - 4.6.2.3
        self.__width: float = self.validate_number(width, "Landing: Width")
        self.__height: float = self.validate_number(height, "Landing: Height")

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

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height
