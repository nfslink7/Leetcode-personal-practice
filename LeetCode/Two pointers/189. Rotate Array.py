class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, start, end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        k=k%len(nums)
        swap(nums,0,len(nums)-1)
        swap(nums,0,k-1)
        swap(nums,k,len(nums)-1)