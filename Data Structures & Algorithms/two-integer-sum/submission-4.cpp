class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diff;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            if (diff.find(target-nums[i]) != diff.end()) {
                ans = {min({i, diff[target-nums[i]]}), max({i, diff[target-nums[i]]})};
            }
            diff[nums[i]] = i;
        }
        return ans;
    }
};
