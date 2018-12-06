import Queue
class MedianFinder(object):

    def __init__(self):
        self.maxq = Queue.PriorityQueue()
        self.minq = Queue.PriorityQueue()

    def addNum(self, num):
        if self.maxq.qsize() == self.minq.qsize():
            self.maxq.put(-num)
        else:
            self.minq.put(num)
        if self.minq.qsize() != 0:
            maxtop = -self.maxq.get()
            mintop = self.minq.get()
            if maxtop < mintop:
                self.maxq.put(-maxtop)
                self.minq.put(mintop)
            else:
                self.maxq.put(-mintop)
                self.minq.put(maxtop)


    def findMedian(self):
        if self.maxq.qsize() > self.minq.qsize():
            ret = -self.maxq.get()
            self.maxq.put(-ret)
            return ret
        else:
            ret1 = -self.maxq.get()
            ret2 = self.minq.get()
            self.maxq.put(-ret1)
            self.minq.put(ret2)
            return float(ret1 + ret2)/2