class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> mapp; 
        for (auto i = 0; i < nums.size(); ++i) { 
            if (mapp.find(nums[i]) == mapp.end()) { 
                mapp.insert(nums[i]); 
            }
            else { 
                return true; 
            }
        }
        return false; 
    }
};