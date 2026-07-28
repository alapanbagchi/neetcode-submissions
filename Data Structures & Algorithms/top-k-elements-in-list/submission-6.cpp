class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freqList;
        vector<int> res;
        for (int num : nums) {
            freqList[num]++; // { 7 : 2}
        }
        vector<vector<int>> count(nums.size());
        for (const auto &m : freqList ) {
            count[m.second - 1].push_back(m.first);
        }
     
        for (int i = count.size() - 1; i >= 0; i--) {
            if (k == 0) {
                break;
            }
            if (count[i].size() == 0) {
                continue;
            }
            for (int j = 0; j < count[i].size(); j++) {
                res.push_back(count[i][j]);
                k--;
            }
        }
        return res;
    }
};
