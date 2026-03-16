class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, item):
        self.frontier.append(item)

    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("frontier boş")
        return self.frontier.pop()


class QueueFrontier(StackFrontier):
    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("frontier boş")
        return self.frontier.pop(0)


print("STACK TEST")
stack = StackFrontier()
stack.add("A")
stack.add("B")
stack.add("C")

print(stack.remove())   
print(stack.remove())   
print(stack.remove())   

print("\nQUEUE TEST")
queue = QueueFrontier()
queue.add("A")
queue.add("B")
queue.add("C")

print(queue.remove())   
print(queue.remove())   
print(queue.remove())   