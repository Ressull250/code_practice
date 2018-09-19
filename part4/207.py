class Node:
    def __init__(self, id):
        self.id = id
        self.outs = []
        self.ins = []

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True
        dict = {}
        for pairs in prerequisites:
            if pairs[0] not in dict: dict[pairs[0]] = Node(pairs[0])
            if pairs[1] not in dict: dict[pairs[1]] = Node(pairs[1])
            dict[pairs[0]].outs.append(dict[pairs[1]])
            dict[pairs[1]].ins.append(dict[pairs[0]])

        def judge(node, visited):
            for i in node.ins:
                if i not in visited:
                    return
            visited.add(node)
            for i in node.outs:
                if i not in visited:
                    judge(i, visited)

        visited = set()
        noson = 0
        for i in range(numCourses):
            if i not in dict:
                noson += 1
                continue
            n = dict[i]
            if len(n.ins) == 0:
                judge(n, visited)
        

        return len(visited)+noson == numCourses


print(Solution().canFinish(3,
[]))


