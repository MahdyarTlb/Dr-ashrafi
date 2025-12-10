## approach:
# if the exit stack is empty, multi pop the first stack
# and push it into the exit stack
# now pop can be like dequeue

class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def add(self, x):
        self.in_stack.append(x)

    def remove(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1] if self.out_stack else "خالیه!"

    def is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0

    def __str__(self):
        temp = self.out_stack[::-1] + self.in_stack
        return f"صف: {' ← '.join(map(str, temp)) if temp else 'خالی'} (اول ← آخر)"