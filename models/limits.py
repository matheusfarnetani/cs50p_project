from dataclasses import dataclass, field


@dataclass
class Limits:
    # Ramp limits
    slope: float
    max_landing: float
    max_segments: int | None

    # Common context
    common_a: tuple = field(default=(5, 1.5, None), repr=False)
    common_b: tuple = field(default=(6.25, 1, None), repr=False)
    common_c: tuple = field(default=(8.33, 0.8, 15), repr=False)
    except_a: tuple = field(default=(10, 0.2, 4), repr=False)
    except_b: tuple = field(default=(12.5, 0.075, 1), repr=False)

    def get_options(self) -> tuple:
        return (
            self.common_a,
            self.common_b,
            self.common_c,
            self.except_a,
            self.except_b,
        )

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
                raise ValueError(
                    "Invalid Option. Available options: COM-A, COM-B, COM-C, EXP-A, EXP-B"
                )
