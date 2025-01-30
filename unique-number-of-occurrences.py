def uniqueOccurrences(arr):
    """
    :type arr: List[int]
    :rtype: bool
    algo:
    - create a frequency dictionary, frequency key and number with given frequency as value
     - after completing the scan, check if there is any frequency with more than 1 value.
    learning:
    - when we initialize dictionary using dict.fromkeys like
    dict.fromkeys([(x+1) for x in range(length)], []), the list in value shares same ref for all indexes, so It was updating all the keys when appending as frequencies[frequency].append(number)
    """
    length = len(arr)
    # we need n slots for the n numbers as in worst case , all numbers will be same with nth frequency 

    #frequencies = dict.fromkeys([(x+1) for x in range(length)], [])
    frequencies_dict = {}
    print(frequencies_dict)
    number_frequencies = {}
    for i in range(length):
        if arr[i] not in number_frequencies:
            number_frequencies.update({arr[i]: 1})
        else:
            number_frequencies[arr[i]]+=1
    print(number_frequencies)

# scan the number_frequencies and place them in their frequency slot
    for number, frequency in number_frequencies.items():
        print(number, frequency)
        if frequency in frequencies_dict:
            frequencies_dict[frequency].append(number)
        else:
            frequencies_dict.update({frequency:[number]})
        print(frequencies_dict)

# check if there are multiple values for any frequency in the frequency dictionary , return false if so , else return true

    for frequency, number_list in frequencies_dict.items():
        if len(number_list)>1:
            print(False)
            return False
    print(True)
    return True
    
if __name__ == "__main__":
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
    uniqueOccurrences(arr)