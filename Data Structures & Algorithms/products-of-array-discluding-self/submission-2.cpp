class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix(nums.size(), 1);
        vector<int> postfix(nums.size(), 1);
        vector<int> res(nums.size(), 1);
        prefix[0] = nums[0];
        postfix[nums.size() - 1] = nums[nums.size() - 1]; 
        for(int i = 1; i < nums.size(); i++) {
            prefix[i] = prefix[i-1] * nums[i];
        }
        for(int i = nums.size() - 2; i >= 0; i--) {
            postfix[i] = postfix[i+1] * nums[i];
        }

        res[0] = postfix[1];
        res[res.size() - 1] = prefix[prefix.size() - 2]; 

        for(int i = 0; i < res.size(); i++) {
            cout << prefix[i] << " " << postfix[i] << '\n';
        }
        for(int i = 1; i < res.size() - 1; i++) {
            res[i] = prefix[i-1] * postfix[i+1];
        }
        return res;
    }
};
