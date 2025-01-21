
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    # Early exit if no flowers need to be planted
    if n == 0:
        return True

    length = len(flowerbed)
    i = 0

    while i < length:
        # If the current plot is empty and the adjacent plots (if any) are also empty
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            # Plant a flower
            flowerbed[i] = 1
            n -= 1
            # Early exit if all flowers are planted
            if n == 0:
                return True
            # Skip the next plot to maintain the no-adjacent-flowers rule
            i += 2
        else:
            # Move to the next plot
            i += 1

    # If we exit the loop and still have flowers to plant, it's not possible
    return n == 0

    

if __name__ == "__main__":
    flowerbed = [0]
    canPlaceFlowers(flowerbed, 1)