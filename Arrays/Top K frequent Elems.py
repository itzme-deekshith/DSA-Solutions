class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        freq = [[] for _ in range(len(nums)+1)]
        
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in freq[::-1]:
            for n in i:
                res.append(n)
                if len(res) == k:
                    return res
                
Obj = Solution()
nums = [1,1,1,2,2,3]
k = 2
res = Obj.topKFrequent(nums, k)
print(nums, k, " --> ", res)


nums = [1]
k = 1
res = Obj.topKFrequent(nums, k)
print(nums, k, " --> ", res)