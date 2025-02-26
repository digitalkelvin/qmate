import time
import asyncio
import sys
sys.path.append('../qmate')
from qmate import Queue, Task  # noqa: E402


async def DoRoutine(number, text):
    await asyncio.sleep(number)
    print(text)


async def DoLater(number, text):
    await asyncio.sleep(number)
    print(text)


queue = Queue(True)
queue.schedule([
    Task(
        func=DoLater,
        name='Do Later',
        at=["00", "30"],
        args=[3, "Doing Later"]
    ),
    Task(
        func=DoRoutine,
        name='Do Routine',
        every=["15"],
        args=[3, "Doing Routine"]
    )
])

while True:
    time.sleep(0.001)
