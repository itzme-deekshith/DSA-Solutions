class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target-n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
            
Obj = Solution()
nums = [2,7,11,15]
target = 9
res = Obj.twoSum(nums, target)
print(nums, target, " --> ", res)


nums = [3,3]
target = 6
res = Obj.twoSum(nums, target)
print(nums, target, " --> ", res)