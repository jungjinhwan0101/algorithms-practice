class MinHeap:
    """
    최소 힙
    """

    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        if not self.heap:
            return
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            return

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def build_heap(self, arr):
        self.heap = arr

        index = len(self.heap) // 2 - 1

        while index >= 0:
            self._heapify_down(index)
            index -= 1

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return index * 2 + 1

    def _right_child(self, index):
        return index * 2 + 2

    def _heapify_down(self, index):
        n = len(self.heap)

        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )

    def _heapify_up(self, index):
        while index > 0 and self.heap[self._parent(index)] > self.heap[index]:
            self.heap[self._parent(index)], self.heap[index] = (
                self.heap[index],
                self.heap[self._parent(index)],
            )
            index = self._parent(index)


def heap_sort(arr: list) -> list:
    heap = MinHeap()
    heap.build_heap(arr)

    sorted_arr = []

    for _ in range(len(heap)):
        sorted_arr.append(heap.extract_min())

    return sorted_arr


def __main__():
    arr = [4, 10, 3, 5, 1]
    print("정렬 전:", arr)
    sorted_arr = heap_sort(arr)
    print("힙 정렬 후:", sorted_arr)

    arr = [(1, "e"), (3, "c"), (5, "d"), (5, "a"), (10, "b")]
    print("정렬 전:", arr)
    sorted_arr = heap_sort(arr)
    print("힙 정렬 후:", sorted_arr)


if __name__ == "__main__":
    __main__()
