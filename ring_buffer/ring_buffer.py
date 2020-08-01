from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque([], maxlen=capacity)
        self.index = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.index += 1

        else:
            self.storage[self.index] = item
            self.index += 1

        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return list(self.storage)

ring = RingBuffer(5)

ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')
ring.append('e')
ring.append('f')
ring.append('g')
ring.append('h')
ring.append('i')

ring.get()
