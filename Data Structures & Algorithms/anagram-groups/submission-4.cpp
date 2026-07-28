class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;
        vector<vector<string>> answer;
        for (string word : strs) {
            vector<int> key(26,0);
            string keyS;
            for (char s : word) {
                key[s - 'a']++;
            }
            for (int k : key) {
                keyS += to_string(k) + ',';
            }
            res[keyS].push_back(word);
        }
        for (auto &[key, value] : res) {
            answer.push_back(value);
        }
        return answer;
    }
};
