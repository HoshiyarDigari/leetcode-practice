

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # counter to track position of current line 
    x_coordinate = 0
    
    area_height =0
    area_width = 0
    # scan the list , calculating area of each line against all other lines to its right
    while x_coordinate < len(height):
        # walk through the list of  lines to the right of current line
        for i in range(x_coordinate +1,len(height)):
            temp_height = min(height[i], height[x_coordinate])
            temp_width = i - x_coordinate
            if (temp_height * temp_width) > (area_height * area_width):
                area_width, area_height = temp_width, temp_height
        x_coordinate+=1
    print( area_height * area_width)
    return area_height * area_width
    

if __name__ == "__main__":
    height = [1,2,4,3]
    maxArea(height)