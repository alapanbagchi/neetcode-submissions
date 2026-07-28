class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority_element = 0, count = 0;

        for (int num: nums) {
            if (count == 0) {
                majority_element = num;
            }
            if (majority_element == num) {
                count++;
            } else {
                count--;
            }
        }
        return majority_element;
    }
};