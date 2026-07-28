class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for(int i = 0; i < s.length(); i++) {
            if (isalnum(s[i])) {
                str += s[i];
            }
        }
        int left = 0;
        int right = str.length()-1;

        while(left < right && right >= 0) {
            if (tolower(str[left]) != tolower(str[right])) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
