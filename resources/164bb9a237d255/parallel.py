import os
from multiprocessing import Pool
from typing import List


class Task:
    def run(self):
        print(f"DummyAsyncTask: Hello from process(id={os.getpid()})")


class ParallelTaskExecuter:
    def __init__(self, num_processes: int):
        self.num_processes = num_processes

    def execute_tasks(self, tasks: List[Task]):
        with Pool(processes=self.num_processes) as process:
            for task in tasks:
                process.apply(task.run)


if __name__ == "__main__":
    executor = ParallelTaskExecuter(2)
    executor.execute_tasks([Task() for _ in range(2)])
