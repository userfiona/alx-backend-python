#!/usr/bin/env python3

"""basics of async"""
import asyncio
import random
import time

async def wait_random(max_delay: int = 10) -> float:
    """waits random delay between 0 and max delay"""
    random_number = random.uniform(0, max_delay)

    await asyncio.sleep(random_number)
    return random_number
