import asyncio
import datetime
import random
 

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

 
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        a = yield from fib(40)
        print(a)
        yield from asyncio.sleep(random.randint(0, 5))
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()
