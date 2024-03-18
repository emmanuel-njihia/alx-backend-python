#!/usr/bin/env python3
'''make_multiplier that takes a float\
        multiplier as argument and returns a function \
        that multiplies a float by multiplier
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple of the key and
    the square of its value.
    '''
    return (k, float(v**2))
