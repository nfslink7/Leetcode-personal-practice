class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)
        while(left<right):
            middle = (left+right)//2
            if nums[middle]>target:
                right = middle
            elif nums[middle]<target:
                left = middle + 1
            else:
                return middle
        return -1
num =[-1,0,3,5,9,12]
target = 9
test = Solution().search(num,target)
print(test)