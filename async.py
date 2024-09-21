import asyncio
import time

async def say_after(duration, message):
    """
    Args:
        duration (float): waiting time([s]) with sleep func
        message (string): print message after waiting
    """
    await asyncio.sleep(duration)
    print(message)

async def demo1_sequence():
    print(f"started at {time.strftime('%X')}")
    
    await say_after(1, "hello")
    await say_after(2, "wow")
    
    print(f"ended at {time.strftime('%X')}")

async def demo1_parallel():
    task1 = asyncio.create_task(
        say_after(1, "hello")
    )
    task2 = asyncio.create_task(
        say_after(2, "wow")
    )

    print(f"started at {time.strftime('%X')}")
    
    await task1
    await task2

    print(f"ended at {time.strftime('%X')}")

async def demo1_parallel_tg():
    """
    This function isn't runnable under ver3.11
    """
    print(f"started at {time.strftime('%X')}")
    
    async with asyncio.TaskGroup() as tg:
        print(f"recorded point1: {time.strftime('%X')}")
        task1 = tg.create_task(
            say_after(1, "hello")
        )
        print(f"recorded point2: {time.strftime('%X')}")
        task2 = tg.create_task(
            say_after(2, "wow")
        )
        print(f"recorded point3: {time.strftime('%X')}")

    print(f"ended at {time.strftime('%X')}")

if __name__=="__main__":
    asyncio.run(demo1_sequence())
    print("================================")
    asyncio.run(demo1_parallel())
    print("================================")
    asyncio.run(demo1_parallel_tg())
