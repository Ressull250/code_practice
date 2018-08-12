class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur = 0
        sum = 0
        pos = 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if cur<0:
                cur=0
                pos=i+1

        return pos if sum >= 0 else -1