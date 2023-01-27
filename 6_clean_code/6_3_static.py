from typing import Union, List, Optional

sample_int: int = 3
sample_str: str = "Hello, World"

sample_int_float: Union[int, float]
sample_str_none: Optional[str]

sample_str_list: List[str] = ["a", "b", "c"]
sample_mult_list: List[Union[int, str]] = [1, "b", "c"]

def sample_func(a: int, b: int) -> int:
    y = a + b
    return y

class SampleClass:
    def __init__(self):
        pass

sample_instance: SampleClass = SampleClass()

sample_str_error: str = 5