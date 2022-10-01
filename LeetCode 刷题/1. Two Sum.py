class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, e in enumerate(nums):
            diff = target - e
            if diff in d:
                return [d[diff], i]
            d[e] = i

number = [2,7,11,5]
target = 9
a = Solution()
print(a.twoSum(number,target))