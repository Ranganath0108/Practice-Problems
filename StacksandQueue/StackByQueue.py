from queue import Queue


class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, data):
        return self.q.put(data)

    def pop(self):
        for _ in range(self.q.qsize()-1):
            self.push(self.q.get())
        return self.q.get()

    def is_empty(self):
        return self.q.empty()
    def push_list(self,lst):
        if len(lst) == 0:
            return
        for i in lst:
            self.push(i)


if __name__ == "__main__":
    a = MyStack()
    print(a.is_empty())
    a.push(1)
    a.push(2)
    a.push(3)
    a.push_list([4,5,6])
    print(a.pop())

    
