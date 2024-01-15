from math import floor

from .geometry import Geometry
from .limits import Limits
from .ramp import Ramp
from .landing import Landing
from .filler import Filler


class AccessibleRamp(Geometry):
    def __init__(self, height: float, width: float, option: str, slope: float = 0):
        # Initialize Variables
        self.__height: float = 0
        self.__width: float = 0
        self.__slope: float = 0
        self.__length: float = 0
        self.__map: list = list()

        # Get limits
        self.limits = Limits.set_by_option(option)

        # Assign Variables
        if not self.set_variables(height, width, slope):
            raise ValueError("Unable to set variables")

        # load
        self.load()

    def __str__(self):
        t0 = f"Height={self.height}, Width={self.width}, Slope={self.slope}"
        t1 = f"Num Landings={self.num_landings}, Segments={self.segments}, Length={self.length:.3f}"
        t2 = ""
        for obj in self.map:
            t2 += "\n"
            if isinstance(obj, tuple):
                t2 += str(obj[0]) + "\n" + str(obj[1]) + "\n"
            else:
                t2 += str(obj) + "\n"
        return f"Accessible Ramp({t0}, {self.limits}, {t1}, {super().__str__()})\n\n--Map--{t2}"

    def set_variables(self, height: float, width: float, slope: float) -> bool:
        self.height = height
        self.width = width
        if slope:
            if not self.adapt_to_slope(slope):
                return False
            return True
        else:
            self.slope = self.limits.slope
            return True

    def adapt_to_slope(self, slope: float) -> bool:
        for option in self.limits.get_options():
            if slope <= option[0]:
                if (
                    self.limits.max_landing != option[1]
                    or self.limits.max_segments != option[2]
                ):
                    self.limits = Limits.set_by_value(option)
                self.slope = slope
                return True
        return False

    def load(self):
        # Calculate number of landings
        self.calc_num_landing()

        # Calculate number of segments
        self.calc_num_segments()

        # Create Map (init instances)
        self.create_map()

        # Calculate length
        self.calculate_length()

        # Creates Geometry
        super().__init__()

        # Calculates area
        self.area = self.length * self.width

        # Calculate volume
        self.calculate_volume()

    def calc_num_landing(self) -> None:
        self.num_landings = self.height / self.limits.max_landing

    def calc_num_segments(self) -> None:
        self.segments = 1 + (floor(self.num_landings) * 2)
        if self.limits.max_segments and self.segments > self.limits.max_segments:
            raise ValueError(
                f"A ramp of height={self.height} cannot be created with slope={self.slope}%. Because segments={self.segments} > max_segments={self.limits.max_segments}"
            )

    def create_map(self) -> None:
        self.__map = [None for _ in range(self.segments)]

        if floor(self.num_landings) == 0:
            self.__map[0] = Ramp(self.height, self.width, slope=self.slope)

        heights = self.calculate_heights()
        for i in range(len(heights)):
            if i % 2 == 0:
                self.__map[i] = Ramp(heights[i], self.width, slope=self.slope)
                if i != 0:
                    self.__map[i] = (
                        self.__map[i],
                        Filler(self.__map[i].length, self.width, heights[i - 1]),
                    )
            else:
                self.__map[i] = Landing(self.width, self.width, heights[i])

    def calculate_length(self):
        for i in self.map:
            if isinstance(i, tuple):
                self.__length += i[0].length
            else:
                self.__length += i.length

    def calculate_volume(self):
        g = Geometry()
        for i in self.map:
            if isinstance(i, tuple):
                g = g.add_volume(i[0])
                g = g.add_volume(i[1])
            else:
                g = g.add_volume(i)
        self.volume = g.volume

    def calculate_heights(self) -> list:
        heights = list()

        for i in range(floor(self.segments / 2)):
            heights.append(self.limits.max_landing)
            heights.append((self.limits.max_landing * (i + 1)))

        n = self.num_landings - floor(self.num_landings)
        if n != 0:
            heights.append((self.limits.max_landing * n))

        return heights

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, n: int | float | str) -> None:
        self.__height = self.validate_number(n, "Height")

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, n: int | float | str) -> None:
        self.__width = self.validate_number(n, "Width")

    @property
    def slope(self) -> float:
        return self.__slope

    @slope.setter
    def slope(self, n: int | float | str) -> None:
        self.__slope = self.validate_number(n, "Slope")

    @property
    def length(self) -> float:
        return self.__length

    @property
    def map(self) -> list:
        return self.__map
