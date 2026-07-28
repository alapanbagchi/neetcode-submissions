#include <cctype>
class Solution {
public:

    string encode(vector<string>& strs) {
        // 4#neet4#code
        string res = "";
        for (string str : strs) {
            res += to_string(str.size()) + "#" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int word_size = -1;
        int starting_index = 0;
        int ending_index = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '#') {
                word_size = stoi(s.substr(starting_index, i));
                res.push_back(s.substr(i+1, word_size));
                starting_index = i+1+word_size;
                i = starting_index;
            }
        }
        return res;
    }
};
