from .geometry import Geometry


class Filler(Geometry):
    def __init__(self, length: float, width: float, height: float):
        # Initialize Variables
        self.__length: float = self.validate_number(length, "Filler: Length:")
        self.__width: float = self.validate_number(width, "Filler: Width:")
        self.__height: float = self.validate_number(height, "Filler: Height:")

        # Creates Geometry
        super().__init__()

        # Calculates area and volume
        self.area = self.length * self.width
        self.volume = self.length * self.width * self.height

    def __str__(self) -> str:
        return f"Filler Geometry(length={self.length:.3f}, width={self.width}, height={self.height:.3f}, area={self.area:.3f}, volume={self.volume:.3f})"

    @property
    def length(self) -> float:
        return self.__length

    @property
    def width(self) -> float:
        return self.__width

    @property
    def height(self) -> float:
        return self.__height
