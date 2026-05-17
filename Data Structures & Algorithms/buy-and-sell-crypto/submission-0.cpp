class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l=0;
        int r=1;
        int max_diff=0;
        while(r<prices.size()){
            if(prices[r]>prices[l]){
                int diff=prices[r]-prices[l];
                max_diff=max(max_diff,diff);
            }
            else{
                l=r;
            }
            r++;
        }
        return max_diff;
    }
};
