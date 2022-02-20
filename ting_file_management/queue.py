class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return None
        return self.data.pop(0)

    def search(self, index):
        if index < 0 or index > len(self.data):
            raise IndexError
        return self.data[index]
