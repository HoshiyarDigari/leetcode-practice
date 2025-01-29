def largestAltitude(gain):
    """
    :type gain: List[int]
    :rtype: int

    algo:
    - starting altitude is 0. then we just add the gains to get the altitudes
    """
    max_altitude = 0
    altitudes = [0]
    for i in range(1,len(gain)+1):
        current_altitude = altitudes[i-1] + gain[i-1]
        altitudes.append(current_altitude)
        max_altitude = max(max_altitude, current_altitude)
        print(altitudes, max_altitude)
    
    
if __name__ == "__main__":
    nums = [-5,1,5,0,-7]
    k = 1
    largestAltitude(nums)