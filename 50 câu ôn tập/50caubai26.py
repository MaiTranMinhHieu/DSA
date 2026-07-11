class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.head = self.tail = self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.k: return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0: return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

cq = MyCircularQueue(3)
print(cq.enQueue(1), cq.enQueue(2), cq.enQueue(3))
print(cq.enQueue(4))
print(cq.deQueue())
print(cq.enQueue(4))