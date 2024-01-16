#!/usr/bin/env python3

""" Tasks """
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def task_wait_random(max_delay: int = 10) -> asyncio.Future:
    """
        Args:
            max_delay: max wait

        Return:
            Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return taski
