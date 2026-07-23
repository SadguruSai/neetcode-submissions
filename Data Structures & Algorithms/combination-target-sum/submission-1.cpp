class Solution {
private:
    void dfs(vector<vector<int>>& ans,vector<int>& nums,vector<int>& cur,int i,int cur_sum,int target){
        if(cur_sum == target){
            ans.push_back(cur);
            return;
        }
        if(cur_sum>target || i>=nums.size()){
            return;
        }
        cur.push_back(nums[i]);
        dfs(ans,nums,cur,i,cur_sum+nums[i],target);
        cur.pop_back();
        dfs(ans,nums,cur,i+1,cur_sum,target);
}

public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        vector<int> cur;
        dfs(ans,nums,cur,0,0,target);
        return ans;
    }
};
