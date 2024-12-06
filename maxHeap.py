# Python MaxHeap
# Public Functions: push, peek, pop
# private functions: __swap, __floatUp, __bubbleDown

class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) -1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) -1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) -1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        idx_parent = index // 2
        if idx_parent > 0 and self.heap[idx_parent] < self.heap[index]:
            self.__swap(idx_parent, index)
            self.__floatUp(idx_parent)

    def __bubbleDown(self, idx):
        left = 2*idx
        right = left+1
        tmp = idx

        if self.heap[left] and self.heap[left] > self.heap[idx]:
            tmp = left
        if self.heap[right] and self.heap[right] > self.heap[idx]:
            tmp = right

        if tmp != idx:
            self.__swap(tmp,idx)
            self.__bubbleDown(tmp)

    def HeapSort(self):
        pass

m = MaxHeap([95,3,21])
print(m.heap)
m.push(10)
print(m.heap)
print(m.heap.pop())
print(m.peek())
