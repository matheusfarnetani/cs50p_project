class Geometry:
    def __init__(self, area: float = None, volume: float = None):
        
        # Initialize variables
        self.__area: float = 0
        self.__volume: float = 0

        # Assign values to variables
        self.area = area if area else 0
        self.volume = volume if volume else 0

    def __str__(self) -> str:
        return f"Geometry(area={self.area:.3f}, volume={self.volume:.3f})"

    def validate_number(self, n: int | float | str, variable: str) -> float:
        """
        Validates if n is a valid int, float, or numeric string and ensures it is positive.

        :param n: The number to be validated, can be an int, float, or numeric string.
        :param variable: Name of the variable being validated.
        :raises ValueError: If n is not a valid int, float, or numeric string,
                            or if it is not a positive number.
        :return: The validated and converted float value of n.
        :rtype: float
        """
        try:
            num = float(n)
        except ValueError:
            raise ValueError(f"{variable}: n must be a valid int, float, or a numeric string")
        else:
            if num < 0:
                raise ValueError(f"{variable}: n must be positive.")
            return num

    @classmethod
    def add_area(cls, other):
        area = cls.area + other.area
        volume = cls.volume + other.volume
        return Geometry(area, volume)
    
    @classmethod
    def add_volume(cls, other):
        area = cls.area
        volume = cls.volume + other.volume
        return Geometry(area, volume)

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, n: int | float | str) -> None:
        self.__area = self.validate_number(n, "area")

    @property
    def volume(self) -> float:
        return self.__volume

    @volume.setter
    def volume(self, n: int | float | str) -> None:
        self.__volume = self.validate_number(n, "volume")
