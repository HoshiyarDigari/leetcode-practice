def maxArea( height):
        """
        :type height: List[int]
        :rtype: int
        algo:
         check area betweeen first and last line
         this area has the largest width and limited by only the shorter line
         move inwards from the shorter line , to find a taller one. 
         stop when left meets right
        optimizations:
        exit early  - if the area possible with current taller line and width , is less than the existing maxArea, we can exit
        if the next line after moving isn't taller than the current one, we skip forward
        """
        left = 0
        right = len(height)-1
        max_area = 0
        max_area_possible = 0
        while left < right:
            current_area = min(height[left],height[right]) * (right -left)
            current_max_area_possible = max(height[left],height[right]) * (right -left)
            if max_area_possible > current_max_area_possible:
                 break
            if current_area> max_area:
                max_area = current_area
            if height[left] == min(height[left], height[right]):
                left+=1
                print(left, 'is left index and its values is ', height[left])
                while (height[left] <= height[left-1]) and left < right:
                    left+=1
                
            else:
                right-=1
                while height[right+1 ] >= height[right]:
                    right-=1
                
        print(max_area)
          

if __name__ == "__main__":
    height = [1, 1]
    maxArea(height)