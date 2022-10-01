class Solution:
    # Example1:
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
    #     lp = 0
    #     rp = len(numbers)-1
    #     while lp < rp:
    #         added = numbers[lp]+numbers[rp]
    #         if added == target:
    #             return [lp+1, rp+1]
    #         elif added < target:
    #             lp += 1
    #         else:
    #             rp -= 1

    # Example2:
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
    #     i, j = 0, len(numbers) - 1
    #     while (True):
    #         if numbers[i] + numbers[j] < target:
    #             i += 1
    #         elif numbers[i] + numbers[j] > target:
    #             j -= 1
    #         else:
    #             return [i + 1, j + 1]

    # 我的垃圾代码
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            left = numbers[i]
            right = numbers[j]
            two_sum=left + right
            if two_sum == target:
                return [i + 1, j + 1]
            elif two_sum < target:
                i += 1
            else:
                j -= 1

b=Solution()
print(b.twoSum([2,7,11,15],9))