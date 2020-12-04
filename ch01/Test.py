from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0;
        result = []
        for i in nums:
            sum += i
            result.append(sum)
        return result


a = Solution.runningSum('', [4, 1, 2, 3])

print("a = ", a)