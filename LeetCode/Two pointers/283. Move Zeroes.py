class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i],nums[p] = nums[p],nums[i]
                p+=1