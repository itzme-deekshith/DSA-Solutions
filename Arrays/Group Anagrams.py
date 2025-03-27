class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        srt = {"".join(sorted(strs[0])):[strs[0]]}
        for i in strs[1:]:
            x = ''.join(sorted(i))
            if x in srt:
                srt[x].append(i)
            else:
                srt[x] = [i]
        return list(srt.values())
    
Obj = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
res = Obj.groupAnagrams(strs)
print(strs, "--> ", res)

strs = ["a"]
res = Obj.groupAnagrams(strs)
print(strs, "--> ", res)
