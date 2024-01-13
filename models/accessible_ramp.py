from math import floor

from .geometry import Geometry
from .limits import Limits
from .ramp import Ramp
from .landing import Landing


class AccessibleRamp(Geometry):

    def __init__(self, height: float, width: float, option: str, slope: float = 0):

        # Initialize Variables
        self.__height: float = 0
        self.__width: float = 0
        self.__slope: float = 0
        self.__length: float = 0

        # Get limits
        if option:
            self.limits = Limits.set_by_option(option)

        # Assign Variables
        if not self.set_variables(height, width, slope):
            raise ValueError("Unable to set variables")
        
        # load
        self.load()

    def __str__(self):
        limits = f"Limits(slope={self.limits.slope}, max_landing={self.limits.max_landing}, max_segments={self.limits.max_segments})"
        return f"Ramp\nHeight={self.height}, Width={self.width}, Slope={self.slope}, {limits}"

    def load(self):
        # Calculates everything
        ...
        # self.rampSegmentLength = self.calcDistance(self.height, self.slope)
        # self.numLanding = self.calcNumLanding(self.height, self.max_landing)
        # self.mapLength = self.calcMapLength(self.numLanding)
        # self.validatedMapLength = self.validateMapLength(self.mapLength, self.numLanding, self.max_segments)
        # self.length = self.calcLength(self.rampSegmentLength, self.numLanding, self.width)
        # self.map = self.createMap(self.mapLength)

    def adapt_to_slope(self, slope: float) -> bool:
        for option in self.limits.get_options():
            if slope <= option[0]:
                if self.limits.max_landing != option[1] or self.limits.max_segments != option[2]:
                    self.limits = Limits.set_by_value(option)
                return True
        return False

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

    def calcLength(self, rampSegmentLength, numLanding, width):
        return rampSegmentLength + (numLanding * width)

    def validateMapLength(self, mapLength, numLanding, max_segments):
        if max_segments == 0:
            return True
        elif (mapLength - numLanding - 2) > max_segments:
            return False
        else:
            return True

    def createMap(self, mapLength):
        map = []
        for i in range(mapLength):
            map.append("none")
        lastIndex = mapLength - 1
        for i in range(mapLength):
            if i == 0:
                map[0] = "start"
            elif i == lastIndex:
                map[lastIndex] = "end"
            elif i % 2 == 0:
                map[i] = "landing"
            else:
                map[i] = "ramp"
        return map

    def calcMapLength(self, numLanding):
        if numLanding == 0:
            return 3
        else:
            return 2 + (numLanding + (numLanding * 2))

    def calcNumLanding(self, height, max_landing):
        return floor(height / max_landing)

    def calcDistance(self, height, slope):
        return height / (slope / 100)
    
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

    @length.setter
    def length(self, n: int | float | str) -> None:
        self.__length = self.validate_number(n, "Length")