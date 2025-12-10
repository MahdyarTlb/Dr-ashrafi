# approach:
# we have a main queue and a temp one.
# push approach is easy, enqueue to the queue
# for pop, dequeue all of data in the main queue to temp queue except the last one,
# then return the last one, (like stack(FILO))


from collections import deque

class StackWithTwoQueues:
    def __init__(self):
        self.main = deque()
        self.temp = deque()

    def push(self, x):
        self.main.append(x)
        print(f" added to stack: {x} {list(self.main)}")

    def pop(self):
        if not self.main:
            print("empty stack!")
            return None

        while len(self.main) > 1:
            self.temp.append(self.main.popleft())

        top = self.main.popleft()
        print(f"deleted last item {top} ")

        while self.temp:
            self.main.append(self.temp.popleft())

        return top

    def top(self):
        if not self.main:
            return None
        return self.main[-1]

    def is_empty(self):
        return len(self.main) == 0

    def size(self):
        return len(self.main)

    def __str__(self):
        return f"پشته: {list(self.main)} (ته ← بالا)"