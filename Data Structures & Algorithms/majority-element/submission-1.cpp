class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> frequency;
        int size = nums.size();
        for (int num: nums) {
            frequency[num] = frequency[num] + 1;
            if(frequency[num] > size/2) {
                return num;
            }
        }
    }
};