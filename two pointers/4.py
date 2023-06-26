import math
def maxArea(height):
    
    # Write your code here.
    i = 0
    j = len(height) - 1
    
    max_area = 0

    while i < j:
        if height[i] < height[j]:
            area = min(height[i], height[j]) * (j-i)
            i+=1
        elif height[i] > height[j]:
            area = min(height[i], height[j]) * (j-i)
            j-=1
        else:
            area = height[i] * (j-i)
            i+=1
            j-=1
        
        max_area = max(max_area, area)
    return(max_area)
