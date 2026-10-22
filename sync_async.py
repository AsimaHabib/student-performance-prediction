import time
import asyncio

def task_a():
    print("Task A started")
    time.sleep(3)
    print("Task A completed")

def task_b():
    print("Task B started")
    time.sleep(3)
    print("Task B completed")

task_a()
task_b()


async def task_a():
    print("Task A started")
    await asyncio.sleep(3)
    print("Task A completed")

async def task_b():
    print("Task B started")
    await asyncio.sleep(3)
    print("Task B completed")

async def main():
    await asyncio.gather(task_a(), task_b())

asyncio.run(main())
