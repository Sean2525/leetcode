class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.manacher(s)
    

    def manacher(self, s0 : str) -> list:
        s = '@#' + '#'.join(s0) + '#'
        l = len(s)
        r = [0] * l
        mx, pos = 0, 0
        ans_i = 0
        ans_value = 0
        for i in range(l):
            if i > mx:
                r[i] = 1
            else:
                r[i] = min(r[2 * pos - i], mx - i)
        
            while i - r[i] >= 0 and i + r[i] < l and s[i+r[i]] == s[i-r[i]]:
                r[i] += 1
            
            if r[i] + i - 1 > mx:
                mx = r[i] + i - 1
                pos = i
            
            if r[i] > ans_value:
                ans_i = i
                ans_value = r[i]
            
        start = int((ans_i - ans_value)/2)
        end = int(start + ans_value - 1) 
        return s0[start:end]
