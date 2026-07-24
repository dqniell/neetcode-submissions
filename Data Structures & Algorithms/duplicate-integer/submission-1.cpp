class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mapp; 
        for (int i = 0; i < nums.size(); ++i) { 
            if (mapp.find(nums[i]) != mapp.end()) { 
                return true; 
            } else { 
                mapp.insert(nums[i]);
            }
        }
        return false;
    }
};