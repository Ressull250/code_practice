class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = dict()
        for s in strs:
            if tuple(sorted(s)) in map:
                map[tuple(sorted(s))].append(s)
            else:
                map[tuple(sorted(s))] = [s]

        return list(map.values())

#排序的时间复杂度为 KlogK，总时间复杂度 N*KlogK
#改进：不排序 tuple（n1,n2,n3,...,n26）作key，nk为字母出现次数，时间复杂度为 NK

print(Solution().groupAnagrams(['bat','tab','sb']))


