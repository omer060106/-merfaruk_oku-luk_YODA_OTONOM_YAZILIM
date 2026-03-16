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