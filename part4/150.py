import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for char in tokens:
            if char.isdigit() or (char[0] == '-' and char[1:] and char[1:].isdigit):
                stack.append(char)
            else:
                op1 = int(stack.pop(-1))
                op2 = int(stack.pop(-1))
                if char == "-":
                    stack.append(op2-op1)
                elif char == "+":
                    stack.append(op2+op1)
                elif char == "/":
                    if (op2 > 0 and op1 < 0):
                        stack.append(-(op2/(-op1)))
                    elif (op2 < 0 and op1 > 0):
                        stack.append(-((-op2)/op1))
                    else:
                        stack.append(op2/op1)
                elif char == "*":
                    stack.append(op2*op1)

        return int(stack[0])

print Solution().evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"])
print -(6/132)


