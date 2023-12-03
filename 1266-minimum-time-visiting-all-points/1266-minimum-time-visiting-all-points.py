class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time=0 
        if len(points)==1:
            return total_time 
        for i in range(1,len(points)):
            x_diff=abs(points[i][0]-points[i-1][0])
            y_diff=abs(points[i][1]-points[i-1][1])
            time=max(x_diff,y_diff)
            total_time+=time 
        return total_time