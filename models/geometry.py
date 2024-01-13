class Geometry:
    def __init__(self, x: float, y: float, z: float = None, area: float = None, volume: float = None):
        """
        Initializes a Geometry object with specified dimensions.

        :param x: Length in meters.
        :param y: Width in meters.
        :param z: Height in meters. Defaults to None.
        :param area: Surface area in square meters. Defaults to None.
        :param volume: Volume in cubic meters. Defaults to None.

        If 'z' is not provided, it is set to 0. If 'area' or 'volume' is not provided, they are calculated
        based on 'x', 'y', and 'z' values.

        :raises ValueError: If 'x', 'y', 'z', 'area', or 'volume' is not a valid int, float, or numeric string,
                            or if any of them is not a positive number.
        """

        # Initialize variables
        self.__x: float = 0
        self.__y: float = 0
        self.__z: float = 0
        self.__area: float = 0
        self.__volume: float = 0

        # Assign values to variables
        self.x = x
        self.y = y
        self.z = z if z else 0
        self.area = area if area else x * y
        self.volume = volume if volume else x * y * z if z else 0

    def __str__(self) -> str:
        return f"Geometry(x={self.x}, y={self.y}, z={self.z}, area={self.area}, volume={self.volume})"

    def validate_number(self, n: int | float | str, variable: str) -> float:
        """
        Validates if n is a valid int, float, or numeric string and ensures it is positive.

        :param n: The number to be validated, can be an int, float, or numeric string.
        :param variable: Name of the variable being validated.
        
        :return: The validated and converted float value of n.

        :raises ValueError: If n is not a valid int, float, or numeric string,
                        or if it is not a positive number.
        """
        try:
            num = float(n)
        except ValueError:
            raise ValueError(f"{variable}: n must be a valid int, float, or a numeric string")
        else:
            if num < 0:
                raise ValueError(f"{variable}: n must be positive.")
            return num

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, n: int | float | str) -> None:
        self.__x = self.validate_number(n, "x")

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, n: int | float | str) -> None:
        self.__y = self.validate_number(n, "y")

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, n: int | float | str) -> None:
        self.__z = self.validate_number(n, "z")

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
