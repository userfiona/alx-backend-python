#!/usr/bin/env python3

"""asynchronous coroutine"""
import asyncio
import random

asyc def wait_random(max_delay: int = 10) -> float:

    """waits random delay between 0 and max delay"""
    random_number = random.uniform(0,max_delay)

    await asyncio.sleep(random_number)
    return random_number
