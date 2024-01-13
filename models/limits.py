from dataclasses import dataclass

@dataclass
class Limits:

    # Ramp limits
    slope: float
    max_landing: float
    max_segments: int | None

    # Common context
    common_a: tuple = (5, 1.5, None)
    common_b: tuple = (6.25, 1, None)
    common_c: tuple = (8.33, 0.8, 15)  # the normal values to use

    # Exception context
    except_a: tuple = (10, 0.2, 4)
    except_b: tuple = (12.5, 0.075, 1)

    def get_slopes(self) -> list:
        return [self.common_a[0], self.common_b[0], self.common_c[0], self.except_a[0], self.except_b[0]]

    def get_options(self) -> tuple:
        return (self.common_a, self.common_b, self.common_c, self.except_a, self.except_b)

    @classmethod
    def set_by_value(cls, t: tuple):
        return cls(*t)

    @classmethod
    def set_by_option(cls, option: str):
        match option:
            case "COM-A":
                return cls(*cls.common_a)
            case "COM-B":
                return cls(*cls.common_b)
            case "COM-C":
                return cls(*cls.common_c)
            case "EXP-A":
                return cls(*cls.except_a)
            case "EXP-B":
                return cls(*cls.except_b)
            case _:
                raise ValueError("Invalid Option. Available options: COM-A, COM-B, COM-C, EXP-A, EXP-B")