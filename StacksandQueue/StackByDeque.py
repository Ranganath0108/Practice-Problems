from collections import deque


class MyStack2:
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)

    def pop(self):
        for _ in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def is_empty(self):
        return len(self.q) == 0

    def push_list(self, lst):
        for i in lst:
            self.push(i)

    def display(self):
        return self.q


if __name__ == "__main__":
    a = MyStack2()
    print(a.is_empty())
    a.push(1)
    a.push(2)
    a.push(3)
    a.push_list([4, 5, 6])
    print(a.display())
    a.pop()
    print(a.display())
