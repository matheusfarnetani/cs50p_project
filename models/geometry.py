class Geometry:
    def __init__(self, x: float, y: float, z: float, area: float = 0, volume: float = 0):
        self.__x: float = 0
        self.__y: float = 0
        self.__z: float = 0
        self.__area: float = 0
        self.__volume: float = 0

        self.x = x
        self.y = y
        self.z = z
        self.area = area or x * y
        self.volume = volume or x * y * z

    def __str__(self) -> str:
        return f"Geometry(x={self.x}, y={self.y}, z={self.z}, area={self.area}, volume={self.volume})"

    def validate_number(self, n, variable):
        if not (isinstance(n, int) or isinstance(n, float)):
            raise ValueError(f"{variable}: n must be int or float")
        elif n < 0:
            raise ValueError(f"{variable}: n must be positive.")

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, n: float) -> None:
        self.__x = n

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, n: float) -> None:
        self.__y = n

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, n: float) -> None:
        self.__z = n

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, n: float) -> None:
        self.__area = n

    @property
    def volume(self) -> float:
        return self.__volume

    @volume.setter
    def volume(self, n: float) -> None:
        self.__volume = n
