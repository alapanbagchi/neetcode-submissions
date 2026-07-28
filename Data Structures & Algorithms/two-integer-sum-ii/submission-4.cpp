class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int right = numbers.size() - 1;
        int left = 0;
        vector<int> res = {0, 0};
        while (left < right) {
            if (numbers[right] + numbers[left] > target) {
                right--;
            } else if (numbers[right] + numbers[left] < target) {
                left++;
            } else {
                res[0] = ++left;
                res[1] = ++right;
                return res;
            }
        }
        return res;
    }
};
