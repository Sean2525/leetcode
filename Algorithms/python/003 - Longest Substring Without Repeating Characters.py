class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        index = {}
        i = 0
        
        for j in range(n):
            i = max(index.get(s[j], 0), i)
            ans = max(ans, j - i + 1)
            index[s[j]] = j + 1
    
        return ans 