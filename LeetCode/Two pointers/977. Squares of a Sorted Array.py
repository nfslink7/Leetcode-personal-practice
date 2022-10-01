class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        i=0
        n=len(nums)-1
        j=n
        ans=[]
        while i<=j:
            lm=nums[i]**2
            rm=nums[j]**2
            if lm>rm:
                ans.append(lm)
                i +=1
            else:
                ans.append(rm)
                j -=1
        return ans[::-1]