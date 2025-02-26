import time
import sys
sys.path.append('../qmate')
from qmate import Queue, Task  # noqa: E402


def PrintSomething(text):
    print(text)


queue = Queue(True)
queue.schedule(
    Task(
        func=PrintSomething,
        name='Print Something',
        at=["00", "15", "30", "45"],
        on=["Tuesday"],
        args=["Quarterly Print"]
    )
)

scheduled = False
while True:

    # Wait 10 seconds, add a task, then print tasks
    if not scheduled:
        time.sleep(10)
        scheduled = True
        queue.schedule(
            Task(
                func=PrintSomething,
                name='Print on 33',
                at=["33"],
                args=["It's Thirty Three"]
            )
        )
        queue.listTasks()
