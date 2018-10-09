class MyStack(object):

    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop(-1)

    def top(self):
        return self.l[-1]

    def empty(self):
        return len(self.l) == 0