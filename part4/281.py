# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    tmp = None
    def __init__(self, iterator):
        self.it = iterator

    def peek(self):
        if self.tmp:
            t = self.tmp
            self.tmp = None
            return t
        else:
            self.tmp = self.it.next()
            return self.tmp

    def next(self):
        if self.tmp:
            t = self.tmp
            self.tmp = None
            return t
        else:
            return self.it.next()

    def hasNext(self):
        return True if self.tmp else self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].