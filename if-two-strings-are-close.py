def closeStrings(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: bool
    algo:'
    - make frequency dictionaries for both words
    - if the sets of keys and values in both dictionaries is same, return true else false
    - it appears that the two words should have same number of total characters and each type of character to be "close"
    """
    frequencies1 ={}
    for char in word1:
        frequencies1[char]=frequencies1.get(char,0)+1
    
    frequencies2 ={}
    for char in word2:
        frequencies2[char]=frequencies2.get(char,0)+1
    ##print(frequencies1,'\n', frequencies2)

    #compare the dictionaries
    ##print(set(frequencies1.keys()), set(frequencies2.keys()))
    ##print((frequencies1.values()), (frequencies2.values()))
    if frequencies1 == frequencies2:
        #print(True)
        return True
    # compare keys and values
    if set(frequencies1.keys()) == set(frequencies2.keys()):
       return sorted(frequencies1.values()) == sorted(frequencies2.values())
    #print(False)
    return False
if __name__ == "__main__":
    word1 = "cabbba"
    word2 = "aabbss"
    closeStrings(word1, word2)