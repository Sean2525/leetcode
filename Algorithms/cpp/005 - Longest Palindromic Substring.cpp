class Solution {
public:
    string longestPalindrome(string s0) {
        int size = s0.size();
        int n = 2 * size +2;
        int *p = new int[n];
        string s = "@#";
        for(int i=0; i < size; ++i){
            s += s0[i];
            s += '#';
        }
        int mx = 0, id = 0;
        int ans_value = 0, ans_i = 0;
        for(int i=0; i<n; i++){
            p[i] = mx > i ? min(p[2*id-i], mx-i) : 1;
            while(i - p[i] >=0 && i + p[i] < n && s[i+p[i]] == s[i-p[i]]){
                p[i]++;
            }
            if (p[i] + i -1 > mx) {
                mx = p[i] + i - 1;
                id = i;
            }
            if (p[i] > ans_value){
                ans_value = p[i];
                ans_i = i;
            }
        }


        int start = (ans_i - ans_value)/2;
        return s0.substr(start, ans_value-1);
    }
};