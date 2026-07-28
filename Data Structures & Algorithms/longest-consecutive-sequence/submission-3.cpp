class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set(nums.begin(), nums.end());
        vector<int> boundary;
        int max_len = 0;
        for (int i = 0; i < nums.size(); i++) {
            if(num_set.find(nums[i] - 1) == num_set.end()) {
                boundary.push_back(nums[i]);
            }
        }
        for (int x : boundary) {
            int len = 0;
            cout << x << '\n';
            while(num_set.find(x++) != num_set.end()) {
                len++;
            }
            max_len = max(max_len, len);
        }
        return max_len;
    }
};
