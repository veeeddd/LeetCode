class Solution {
public:
    static int findLHS(vector<int>& nums) {
        const int n=nums.size();
        sort(nums.begin(), nums.end());
        int maxLen=0;
        for(int l=0, r=0; l<n; l++){
            const int x=nums[l];
            r=upper_bound(nums.begin()+l+1, nums.end(), x+1)-nums.begin()-1;
            if (nums[r]==x+1){
                maxLen=max(maxLen, r-l+1);
                l=upper_bound(nums.begin()+l+1, nums.end(), x)-nums.begin()-1;
            }
        }
        return maxLen;
    }
};