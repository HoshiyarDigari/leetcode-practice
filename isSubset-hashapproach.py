def wordSubsets():
    word1 = "ab"
    word2 = "pqr"
    index=0
    # we will loop for total length of the two string combined
    merged_string_length = len(word1) + len(word2)
    merged_string=[]
    for index in range(merged_string_length):
        # put character from word1 followed by word2 character into the merged string
        print(index, merged_string)
        # only add if all the characters of word1 are not already placed into the list
        if index < len(word1):
            merged_string.append(word1[index]) 
        # same check for word2
        if index < len(word2):
            merged_string.append(word2[index]) 
    print('merged', merged_string)
    return str(merged_string)   
            


if __name__ == "__main__":
    wordSubsets()