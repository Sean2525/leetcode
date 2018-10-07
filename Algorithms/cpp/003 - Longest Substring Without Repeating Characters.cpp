class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int index[128] = {0};
        int ans=0, i=0, j=0;
        for(i,j ;j < s.length(); j++){
            i = max(index[s[j]], i);
            ans = max(ans, j - i + 1);
            index[s[j]] = j + 1;
        }
        return ans;
    }
};