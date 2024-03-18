#!/usr/bin/env python3
'''sum_mixed_list which takes a list\
        mxd_lst of integers and floats\
        and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers and floating-point numbers.
    '''
    return float(sum(mxd_lst))
