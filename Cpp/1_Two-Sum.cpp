class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        map<int, int> m1;
        int cnt = nums.size();
        for(int i= 0; i< cnt;i++){
            if(m1.count(nums[i]) == 1){
                ans.push_back(m1[nums[i]]);
                ans.push_back(i);
                return ans;
            }
            m1[target - nums[i]] = i;

        }
        return ans;
    }
};