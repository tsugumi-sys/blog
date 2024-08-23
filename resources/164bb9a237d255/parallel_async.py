import asyncio
import os
import sys
from multiprocessing import Pool
from typing import List


class AsyncTask:
    def run(self):
        asyncio.run(self.__run())

    async def __run(self):
        print(f"DummyAsyncTask: Hello from process(id={os.getpid()})")
        await asyncio.sleep(0.1)
        sys.stdout.flush()


class ParallelAsyncTaskExecutor:
    def __init__(self, num_processes: int):
        self.num_processes = num_processes

    def execute_tasks(self, tasks: List[AsyncTask]):
        with Pool(processes=self.num_processes) as process:
            res = [
                process.apply_async(
                    task.run,
                )
                for task in tasks
            ]
            for r in res:
                r.wait()


if __name__ == "__main__":
    execturor = ParallelAsyncTaskExecutor(2)
    execturor.execute_tasks([AsyncTask() for _ in range(2)])
