class Node:
    def __init__(self, id):
        self.id = id
        self.outs = []
        self.ins = []

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dict = {}
        for pairs in prerequisites:
            if pairs[0] not in dict: dict[pairs[0]] = Node(pairs[0])
            if pairs[1] not in dict: dict[pairs[1]] = Node(pairs[1])
            dict[pairs[1]].outs.append(dict[pairs[0]])
            dict[pairs[0]].ins.append(dict[pairs[1]])

        def judge(node, visited, res):
            for i in node.ins:
                if i not in visited:
                    return
            visited.add(node)
            res.append(node.id)
            for i in node.outs:
                if i not in visited:
                    judge(i, visited, res)

        visited = set()
        res = []
        noson = 0
        for i in range(numCourses):
            if i not in dict:
                noson += 1
                res.append(i)
                continue
            n = dict[i]
            if len(n.ins) == 0:
                judge(n, visited, res)

        return res if len(visited) + noson == numCourses else []


print(Solution().findOrder(2,
                           [[0,1]]))


