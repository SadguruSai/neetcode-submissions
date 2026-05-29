class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        top=0
        bot=rows-1
        while(top<=bot):
            mid_row=top+(bot-top)//2
            if(target<matrix[mid_row][0]):
                bot=mid_row-1
            elif(target>matrix[mid_row][cols-1]):
                top=mid_row+1
            else:
                break;
        if not (top<=bot):
            return False
        al_row=(top+bot)//2
        l=0
        r=cols-1
        while(l<=r):
            mid=l+(r-l)//2
            if(target>matrix[al_row][mid]):
                l=mid+1
            elif(target<matrix[al_row][mid]):
                r=mid-1
            else:
                return True
        return False
            

        
