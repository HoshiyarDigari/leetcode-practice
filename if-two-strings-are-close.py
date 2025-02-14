
def closeStrings( word1, word2):
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
    print(frequencies1,'\n', frequencies2)

    #compare the dictionaries
    print(set(frequencies1.keys()), set(frequencies2.keys()))
    print((frequencies1.values()), (frequencies2.values()))
    if frequencies1 == frequencies2:
        print(True)
        return True
    # compare keys and values
    if set(frequencies1.keys()) == set(frequencies2.keys()):
        values2 = tuple(frequencies2.values())
        print('values2', values2)
        for number in frequencies1.values():
            print(number, values2)
            if number not in values2:
                print(False)
                return False
            else:
                index = values2.index(number)
                print('deleting', index, values2, number)
                values2 = values2[:index] + values2[index+1:]
                print('new values2', values2)
            
        print(True)
        return True
    print(False)
    return False


if __name__ == "__main__":
    word1 = "cabbba"
    word2 = "abbccc"
    closeStrings(word1, word2)