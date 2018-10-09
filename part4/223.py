# encoding=utf8
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        left = max(A, E)
        right = max(min(C, G), left)
        bottom = max(B, F)
        up = max(min(D, H), bottom)

        total = (D - B) * (C - A) + (H - F) * (G - E) - (right-left)*(up-bottom)

        return total
