class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
      sort(nums.begin(), nums.end());
      vector<vector<int>> res;
      for(int i = 0; i < nums.size(); i++) {
        if (i!=0 && nums[i-1] == nums[i]) {
            continue;
        }
        int left = i + 1;
        int right = nums.size() - 1;
        while (left < right) {
            if(nums[left] + nums[right] + nums[i] > 0 ) {
                right--;
            } else if (nums[left] + nums[right] + nums[i] < 0) {
                left++;
            } else {
                res.push_back({nums[i], nums[left], nums[right]});
                while (left < right && nums[left] == nums[left + 1]) {
                    left++;
                }
                left++;
                right--;
            }
        }        
      }
      return res;
    }
};
