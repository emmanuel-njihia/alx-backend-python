#!/usr/bin/env python3
"""
Module with an asynchronous generator coroutine.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields a random number between 0 and 10 after each
    asynchronous wait of 1 second. This process is repeated 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example usage (in 0-main.py):
