class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not(len(set(nums)) == len(nums))
    
Obj = Solution()
nums = [1,2,3,1]
result = Obj.containsDuplicate(nums)
print(nums,"-->",result)

nums = [1,2,3,4]
result = Obj.containsDuplicate(nums)
print(nums,"-->",result)
