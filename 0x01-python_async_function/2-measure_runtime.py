#!/usr/bin/env python3
"""Measure the runtime of coroutines"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

async def measure_time_coroutine(n: int, max_delay: int) -> float:
    """Async function to measure the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of times wait_n should be called.
        max_delay (int): delay period

    Returns:
        float: total execution time / n
    """
    start_time = time.perf_counter_ns()
    await asyncio.gather(*[wait_n(1, max_delay) for _ in range(n)])
    total_time = time.perf_counter_ns() - start_time

    return total_time / (n * 1e9)  # Convert nanoseconds to seconds

def measure_time(n: int, max_delay: int) -> float:
    """Function to measure the total execution time for wait_n(n, max_delay)

    Args:
        n (int): number of times wait_n should be called.
        max_delay (int): delay period

    Returns:
        float: total execution time / n
    """
    asyncio.run(measure_time_coroutine(n, max_delay))

if __name__ == "__main__":
    n_value = 5  # Replace with your desired value
    max_delay_value = 3  # Replace with your desired value

    measure_time(n_value, max_delay_value)
