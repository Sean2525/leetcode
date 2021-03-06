class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            if (m.find(nums[i]) != m.end()) {
        		result.push_back(m[nums[i]]);
        		result.push_back(i);
        		break;
        	}
        	m[target - nums[i]] = i;
        }
        return result;
    }
};