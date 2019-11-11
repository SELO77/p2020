import asyncio as aio


class AsyncQueueLoop:
    def __init__(self):
        self.queue = aio.Queue()
        self.tasks = []


async def q_worker(name, queue):
    name = f'q_worker-{name}'
    while True:
        queue.qsize()
        task = await queue.get()
        await task()
        queue.task_done()
        print(f'{name} has done')
        await aio.sleep(3)


async def time_keeper(name):
    name = f'time_keeper-{name}'
    return await aio.sleep(3)



QSIZE = 20
q = aio.Queue(QSIZE)


async def enq():
    global q

    i = 0
    while True:
        print(f'Put to Queue {i}')
        # await q.put(time_keeper(i))
        q.put_nowait(time_keeper(i))
        i += 1

async def runq():
    global q

    while True:
        qsize = q.qsize()
        print(f'runq qsize {qsize}')
        if qsize > 0:
            coro = await q.get()
            # coro = aio.ensure_future(coro)
            await coro
        await aio.sleep(1)


async def main():
    # sleep_for = random.uniform(0.05, 1.0)
    tasks = []
    tasks.append(aio.ensure_future(enq()))
    tasks.append(aio.ensure_future(runq()))
    print("==")
    await aio.gather(tasks, return_exceptions=True)
    print("===")


aio.run(main())
