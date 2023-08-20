import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    worker_heap = [(0, i) for i in range(n_workers)]  # 初始的工人佇列，元組格式為 (空閒時間, 工人編號)
    heapq.heapify(worker_heap)

    for job in jobs:
        next_free_time, worker = heapq.heappop(worker_heap)
        result.append(AssignedJob(worker, next_free_time))
        next_free_time += job
        heapq.heappush(worker_heap, (next_free_time, worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
