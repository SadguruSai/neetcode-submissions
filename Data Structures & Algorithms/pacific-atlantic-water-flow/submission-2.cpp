class Solution {
private:
    void dfs(vector<vector<int>>& heights,int r,int c,set<pair<int,int>>& visited,int prevHeight){
        int rows=heights.size();
        int cols=heights[0].size();
        if(r<0 || c<0 || r==rows || c==cols || heights[r][c]<prevHeight || visited.find({r,c})!=visited.end()){
            return;
        }
        visited.insert({r,c});
        dfs(heights,r+1,c,visited,heights[r][c]);
        dfs(heights,r-1,c,visited,heights[r][c]);
        dfs(heights,r,c+1,visited,heights[r][c]);
        dfs(heights,r,c-1,visited,heights[r][c]);
    }
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        set<pair<int,int>> pac;
        set<pair<int,int>> atl;
        int rows=heights.size();
        int cols=heights[0].size();
        for(int i=0;i<rows;i++){
            dfs(heights,i,0,pac,heights[i][0]);
            dfs(heights,i,cols-1,atl,heights[i][cols-1]);
        }
        for(int j=0;j<cols;j++){
            dfs(heights,0,j,pac,heights[0][j]);
            dfs(heights,rows-1,j,atl,heights[rows-1][j]);
        }
        vector<vector<int>> ans;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(pac.find({i,j})!=pac.end() && atl.find({i,j})!=atl.end()){
                    ans.push_back({i,j});
                }
            }
        }
        return ans;
    }
};
