class Solution(object):
    def productExceptSelf(self, nums):
        x = len(nums)
        res = [1 for i in range(x)]

        pre = nums[0]
        for i in range(1,x):
            res[i] = pre
            pre *= nums[i]

        post = nums[-1]
        for i in range(x-2,-1,-1):
            res[i] = res[i]*post
            post *= nums[i]
        
        return res
    
Obj = Solution()
nums = [1,2,3,4]
res = Obj.productExceptSelf(nums)
print(nums, " --> ", res)

nums = [-1,1,0,-3,3]
res = Obj.productExceptSelf(nums)
print(nums, " --> ", res)