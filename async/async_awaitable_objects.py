import asyncio
import time
from functools import partial


# awaitable objects are 3types. coroutine, task, future

async def say_after(delay, what):
    print(f"{delay}.1")
    await asyncio.sleep(delay)
    print("Say ", what)
    print(f"{delay}.2")


# say_after_1s = partial(say_after, 2, 'world')
say_after_2s = partial(say_after, 3, 'kyul')


# tasks = []
# tasks.append(asyncio.create_task(say_after_1s))
# tasks.append(asyncio.create_task(say_after_2s))


async def main():
    # tasks1 = asyncio.create_task(say_after_1s())

    tasks1 = asyncio.create_task(say_after(2, 'world'))
    # tasks3 = asyncio.create_task(say_after(2, 'serim'))
    tasks2 = asyncio.create_task(say_after_2s())


    print(f"started at {time.strftime('%X')}")
    # await say_after(1, 'World')
    # await say_after(2, 'Kyul')

    # print("0")
    # await say_after_1s()
    # print("1")
    # await say_after_2s()
    # print("2")

    # print("0")
    # await tasks1
    # print("1")
    # await tasks2
    # print("2")
    # 0
    # 2.1
    # 3.1
    # 2.2
    # 1
    # 3.2
    # 2

    print("0")
    # await tasks1 # this included initialize loop when first call `````````````````````````~~~~`````````````````````````````````````````````````````````````````````````````````~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`11q

    print("1")
    print(await asyncio.sleep(0.1, "sleep done"))
    # await tasks2
    print("2")

    print(f"finished at {time.strftime('%X')}")

    await tasks1
    await tasks2


asyncio.run(main())
# asyncio.run(main())
