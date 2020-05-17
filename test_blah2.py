from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        lastStonePos = stones[-1]

        def jump(k, currPos, stones, memo):
            if currPos == lastStonePos:
                return True
            nextPos = currPos + k
            if nextPos in memo:
                return memo[nextPos]
            elif nextPos > currPos and nextPos in stones:
                k_plus_1 =  jump(k + 1, nextPos, stones, memo)
                k_ =  jump(k, nextPos, stones, memo)
                k_minus_1 =  jump(k -1, nextPos, stones, memo)
                memo[currPos] =  k_plus_1 or k_ or k_minus_1
                return memo[currPos]
            else:
                return False

        return jump(1, 0, stones, {})


def test_lbah():
    assert True == Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17])


def test_lbah2():
    assert False == Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])
