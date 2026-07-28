class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res;
        
        for(int i = 0; i < temperatures.size(); i++) {
            int count = 1;
            int flag = false;
            for(int j = i+1; j < temperatures.size(); j++) {
                cout << temperatures[i] << " " << temperatures[j] << '\n';
                if (temperatures[j] > temperatures[i]) {
                    res.push_back(count);
                    flag = true;
                    break;
                } else {
                    count++;
                }
            }
            if(!flag) {
                res.push_back(0);
            }
        }
        return res;
    }
};
