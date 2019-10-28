import asyncio
# gather 는 동시에 aws 시퀀스에 있는 awaitable object 를 동시에 실행합니다.
import os

import aiohttp
import uvloop


async def factorial(name, number):
    f = 1
    pid = os.getpid()
    name = f'{pid}:{name}'

    if number == 2:
        raise Exception(f'Too small number {number}.')

    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f


async def req(name, url):
    pid = os.getpid()
    name = f'{pid}:{name}'
    print(f"Task {name}: Request {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            print(f"Task {name}: Response of Request {text}")


async def main():
    print(asyncio.get_event_loop_policy())

    results = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        return_exceptions=False
    )
    print(f"Results={results}")
    await asyncio.sleep(5)

    # await asyncio.gather(
    #     req("A", 'https://httpbin.org/delay/2'),
    #     req("B", 'https://httpbin.org/delay/3'),
    #     req("C", 'https://httpbin.org/delay/4'),
    # )


uvloop.install() # Change _UnixSelectorEventLoop to EventLoop based on Cython
asyncio.run(main())
