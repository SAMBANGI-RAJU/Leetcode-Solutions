class Solution:
    def findMinArrowShots(self, pts: List[List[int]]) -> int:
        # Sort the points (balloons) by their right end
        pts.sort(key=lambda p:p[1])

        # Initialize the number of arrows needed to 0, and the rightmost point that has been covered to 0
        ans,arr=0,0

        # Iterate through the points
        for [st,end] in pts:
          # If this is the first point, or if the left end of the point is to the right of the rightmost point that has been covered,
          # increment the number of arrows needed and update the rightmost point that has been covered to the right end of the point
            if ans==0 or st>arr:
                ans,arr=ans+1,end

        # Return the number of arrows needed
        return ans