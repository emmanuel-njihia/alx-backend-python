#!/usr/bin/env python3
"""
Module with an asynchronous coroutine.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Args:
        max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
        float: Random delay between 0 and max_delay seconds.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))

