class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        vector<int> ans;
        for(int i:nums){
            freq[i]++;
        }
        vector<vector<int>> bucket(nums.size()+1);

        for(auto j:freq){
            bucket[j.second].push_back(j.first);
        }

        for(int i=bucket.size()-1;i>=0;i--){
            for(int nums:bucket[i]){
                ans.push_back(nums);
                if(ans.size()==k){
                    return ans;
                }
            }
        }
        return nums;
    }
};
