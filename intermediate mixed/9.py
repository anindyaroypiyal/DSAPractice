def largestRectangle(arr):

 

        arr.append(0)

        maxArea=0

        stack=[]

 

        for i,h in enumerate(arr):

                start=i #the starting range of the element. 

                while stack and stack[-1][1]>h: 

                        index,height=stack.pop() #because we found a smaller elemnt than stack top.

                        maxArea=max(maxArea,height*(i-index)) #calculate the max area as it can't be extended further.

                        start=index #the smaller element will be extended to the back.

                stack.append((start,h)) #the element is not smaller than stack top.

        for i,h in stack:
                maxArea = max(maxArea, h * (len(arr)-i)) #for the remaining items in the stack that were not popped.

        return maxArea