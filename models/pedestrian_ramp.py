from math import floor

from .limits import Limits
from .ramp import Ramp
from .landing import Landing


class PedestrianRamp:

    def __init__(self, height: float | int, width: float | int, option: str, slope: float | int = 0):
        self.__height: float | int = 0
        self.__width: float | int = 0
        self.__slope: float | int = 0
        self.__length: float | int = 0

        self.limits = Limits.set_values(option)
        if not self.set_variables(height, width, slope):
            raise ValueError("Unable to set variables")
        self.reload()

    def __str__(self):
        return f"Ramp\nHeight={self.height}, Width={self.width}, Slope={self.slope}, Options={self.limits}"

    def reload(self):
        # Calculates everything
        ...
        # self.rampSegmentLength = self.calcDistance(self.height, self.slope)
        # self.numLanding = self.calcNumLanding(self.height, self.max_landing)
        # self.mapLength = self.calcMapLength(self.numLanding)
        # self.validatedMapLength = self.validateMapLength(self.mapLength, self.numLanding, self.max_segments)
        # self.length = self.calcLength(self.rampSegmentLength, self.numLanding, self.width)
        # self.map = self.createMap(self.mapLength)

    def set_variables(self, height: float | int, width: float | int, slope: float | int) -> bool:
        self.height = height
        self.width = width
        if not slope:
            self.slope = self.limits.slope
        else:
            self.slope = slope
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