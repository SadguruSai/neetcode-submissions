class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left=0;
        int right=heights.size()-1;
        int max_vol=0;
        while(left<right){
            int vol=(right-left)*(min(heights[right],heights[left]));
            max_vol=max(max_vol,vol);
            if(heights[left]>heights[right]){
                right--;
            }
            else if(heights[left]<=heights[right]){
                left++;
            }
        }
        return max_vol;
    }
};
