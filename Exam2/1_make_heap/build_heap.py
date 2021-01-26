# python3


class HeapSort(object):

    def __init__(self, A):
        self.size = len(A)
        self.A = A
        self.swaps = []
        self.BuildHeap(A)

    def BuildHeap(self, A):

        for i in range(self.size//2 - 1, -1, -1):
            self.SiftDown(i)


    def SiftDown(self, i):
        maxIndex = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left <= self.size - 1 and self.A[maxIndex] >= self.A[left]:
            maxIndex = left

        if right <= self.size - 1 and self.A[maxIndex] >= self.A[right]:
            maxIndex = right

        if maxIndex != i:
            self.swaps.append((i, maxIndex))
            self.A[i], self.A[maxIndex] = self.A[maxIndex], self.A[i]
            self.SiftDown(maxIndex)



def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    heap = HeapSort(data)

    return heap.swaps



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
