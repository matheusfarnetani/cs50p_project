from math import floor

from .geometry import Geometry
from .limits import Limits
from .ramp import Ramp
from .landing import Landing
from .filler import Filler


class AccessibleRamp(Geometry):
    def __init__(
        self, height: float, width: float, option: str = "COM-C", slope: float = 0
    ):
        # Initialize Variables
        self.__height: float = 0
        self.__width: float = 0
        self.__slope: float = 0
        self.__length: float = 0
        self.__map: list = list()

        # Get limits
        self.limits = Limits.set_by_option(option)

        # Assign Variables
        if not self.set_variables(height, width, slope, self.limits):
            raise ValueError("Unable to set variables")

        # load
        self.load()

    def __str__(self):
        t0 = f"Height={self.height}, Width={self.width}, Slope={self.slope}"
        t1 = f"Num Landings={self.__num_landings}, Segments={self.segments}"
        t2 = f"Length={self.length:.3f}, Final Height={self.final_heigth:.3f}"
        return f"Accessible Ramp\n{t0}\n{self.limits}\n{t1}\n{t2}\n{super().__str__()})"

    def set_variables(self, height: float, width: float, slope: float, limits: Limits) -> bool:
        if type(limits) != Limits:
            return False
        self.height = height
        self.width = width
        if slope:
            self.slope = slope
            if not self.adapt_to_slope(slope, limits):
                return False
            return True
        else:
            self.slope = limits.slope
            return True

    def adapt_to_slope(self, slope: float, limits: Limits) -> bool:
        for option in limits.get_options():
            if slope <= option[0]:
                if limits.max_landing != option[1] or limits.max_segments != option[2]:
                    self.limits = Limits.set_by_value(option)
                return True
        return False

    def load(self) -> None:
        # Calculate number of landings
        if n := self.calc_num_landings(self.height, self.limits.max_landing):
            self.__num_landings = n
        else:
            raise ValueError("Unable to calculate number of landings")

        # Calculate number of segments
        if s := self.calc_num_segments(self.num_landings, self.limits.max_segments):
            self.__segments = s
        else:
            raise ValueError("Unable to calculate number of segments")

        # Create Map (init instances)
        if m := self.create_map(
            self.segments,
            self.num_landings,
            self.limits.max_landing,
            self.height,
            self.width,
            self.slope,
        ):
            self.__map = m
        else:
            raise ValueError("Unable to create and populate map")

        # Calculate length
        if l := self.calculate_length(self.map):
            self.__length = l
        else:
            raise ValueError("Unable to calculate length")

        # Calculate final height
        # Better keep it until no more bugs are find
        if fh := self.calculate_final_height(self.map):
            self.__final_height = fh
        else:
            raise ValueError("Unable to calculate final height")

        # Creates Geometry
        super().__init__()

        # Calculates area
        self.area = self.length * self.width

        # Calculate volume
        if v := self.calculate_volume(self.map):
            self.volume = v

    def calc_num_landings(self, height: float, max_landing: float) -> float | None:
        try:
            return height / max_landing
        except (TypeError, ValueError, ZeroDivisionError):
            return None

    def calc_num_segments(self, num_landings: float, max_segments: float) -> int | None:
        try:
            s: int = 1 + floor(num_landings)
            if max_segments and s > max_segments:
                raise ValueError(f"segments={s} > max_segments={max_segments}")
        except (TypeError, ValueError):
            return None
        return s

    def create_map(
        self,
        segments: int,
        num_landings: float,
        max_landing: float,
        height: float,
        width: float,
        slope: float,
    ) -> list | None:
        try:
            if floor(num_landings) == 0:
                return [Ramp(height, width, slope=slope)]

            map_length: int = segments + floor(num_landings)
        except (TypeError, ValueError):
            return None
        else:
            map: list = [None for _ in range(map_length)]

            if heights := self.calculate_heights(map_length, max_landing, num_landings):
                return self.populate_map(map, heights, width, slope)
            else:
                return None

    def populate_map(self, map: list, heights: list, width: float, slope: float) -> list | None:
        for i in range(len(heights)):
            try:
                if i % 2 == 0:
                    # print(heights[i], width, slope)
                    map[i] = Ramp(heights[i], width, slope=slope)
                    if i != 0:
                        map[i] = (map[i], Filler(map[i].length, width, heights[i - 1]))
                else:
                    map[i] = Landing(width, width, heights[i])
            except (TypeError, ValueError):
                return None
        return map

    def calculate_length(self, map: list) -> float | None:
        l: float = 0
        try:
            for i in map:
                if isinstance(i, tuple):
                    l += i[0].length
                else:
                    l += i.length
        except (AttributeError, TypeError):
            return None
        return l

    def calculate_volume(self, map: list) -> float | None:
        g = Geometry()
        try:
            for i in map:
                if isinstance(i, tuple):
                    g = g.add_volume(i[0])
                    g = g.add_volume(i[1])
                else:
                    g = g.add_volume(i)
        except (AttributeError, TypeError):
            return None
        return g.volume

    def calculate_heights(self, length: int, max_landing: float, num_landings: float) -> list | None:
        heights: list = list()

        # Create height in pairs of ramp and landing
        try:
            for i in range(floor(length / 2)):
                heights.append(max_landing)
                heights.append((max_landing * (i + 1)))
        except (TypeError, ValueError, ZeroDivisionError):
            return None

        # The for loop above creates only lists of even length
        # If the lists is, in fact, odd, this next sequence
        # Will check if the number of landings has decimal values
        # And then calculate the last height and append it
        try:
            n: float = num_landings - floor(num_landings)
            if n != 0:
                heights.append((max_landing * n))
            else:
                heights.append(max_landing)
        except (TypeError, ValueError):
            return None

        return heights

    def calculate_final_height(self, map: list) -> float | None:
        try:
            if len(map) == 1:
                return map[0].height
            elif type(map[-1]) == tuple:
                return map[-1][0].height + map[-1][1].height
            return None
        except TypeError:
            return None

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
    def num_landings(self) -> float:
        return self.__num_landings

    @property
    def segments(self) -> int:
        return self.__segments

    @property
    def map(self) -> list:
        return self.__map

    @property
    def length(self) -> float:
        return self.__length

    @property
    def final_heigth(self) -> float:
        return self.__final_height
