from .geometry import Geometry


class Filler(Geometry):
    def __init__(self, length: float, width: float, height: float):
        super().__init__(x=length, y=width, z=height)
    
    def __str__(self) -> str:
        return f"Filler Geometry(x={self.x}, y={self.y}, z={self.z}, area={self.area}, volume={self.volume})"
    