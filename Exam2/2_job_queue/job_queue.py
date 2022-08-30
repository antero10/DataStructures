# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Job:
    def __init__(self, id, started_at):
        self.id = id
        self.started_at = started_at

    def __lt__(self, other):
        return self.started_at < other.started_at or self.id <= other.id

    def __le__(self, other):
        return self.started_at <= other.started_at or self.id < other.id

    def __gt__(self, other):
        return self.started_at > other.started_at or self.id > other.id

    def __ge__(self, other):
        return self.started_at >= other.started_at or self.id >= other.id

    def __str__(self):
        return 'Job(id=%s, started_at=%s)' % (self.id, self.started_at)


class PriorityQueue:
    def __init__(self, A):
        self.size = len(A)
        self.A = A
        self.BuildHeap()

    def BuildHeap(self):
        for i in range(self.size // 2, 0, -1):
            self.SiftDown(i)

    def Insert(self, p):
        self.size += 1
        self.A.append(p)
        self.SiftUp(self.size - 1)

    def ExtractMax(self):
        result = self.A.pop(0)
        self.size -= 1
        self.A[0], self.A[self.size - 1] = self.A[self.size - 1], self.A[0]
        self.SiftDown(0)
        return result

    def SiftUp(self, i):
        index = i
        parent = i // 2
        while index > 0 and self.A[parent] > self.A[index]:
            self.A[index], self.A[parent] = self.A[parent], self.A[index]
            index = parent

    def SiftDown(self, i):
        max_index = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= self.size - 1 and self.A[max_index] > self.A[left]:
            max_index = left

        if right <= self.size - 1 and self.A[max_index] > self.A[right]:
            max_index = right

        if max_index != i:
            self.A[i], self.A[max_index] = self.A[max_index], self.A[i]
            self.SiftDown(max_index)


def assign_jobs(n_workers, jobs):
    result = []
    workers = [Job(n, 0) for n in range(0, n_workers)]
    priority_queue = PriorityQueue(workers)
    for job in jobs:
        worker = priority_queue.ExtractMax()
        result.append(AssignedJob(worker.id, worker.started_at))
        worker.started_at += job
        priority_queue.Insert(worker)
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
