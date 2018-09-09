class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []
        self.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # initial
        if not self.list:
            self.min = x
            self.list.append(0)
        else:
            self.list.append(x-self.min)
            self.min = min(self.min, x)

    def pop(self):
        """
        :rtype: void
        """
        t = self.list.pop(-1)
        if t<0 :
            self.min -= t
            return t
        else:
            return self.min + t

    def top(self):
        """
        :rtype: int
        """
        t = self.list[-1]
        if t < 0:
            return self.min
        else:
            return self.min + t

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
