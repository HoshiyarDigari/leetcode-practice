class Solution:
    def minDistance(word1: str, word2: str) -> int:
        """
        Algo:
        we use a matrix distance[word1length+1][word2length+1], where distance[i][j] equals the number of moves to convert word1[0...i-1] to word2[0...j-1]
        we count for empty strings so the distance matrix is longer by 1
        if word1[i]== word2[j], then distance[i+1][j+1] is same as distance[i][j]
        if word1[i]!=word2[j], then we have 3 possiblities
         - deletion: represented by dp[i-1][j]
        - insertion: representd by dp[i][j-1]
         - replacement: represented by dp[i-1][j-1]
         we take minimum of these 3 and add one for that operation itself for dp[i][j]
        """
        rows= len(word1)
        cols = len(word2)
        distance=[[0 for x in range(cols+1)] for y in range(rows+1)]
        # fill matrix for first row and column , that are for when one of the string is empty
        for i in range(rows+1):# iterating on rows
            distance[i][0] = i
        for j in range(cols+1):#iterating on columns
            distance[0][j]= j
        #now lets fill the rest of the matrix as per recurrence
        for i in range(1,rows+1):
            for j in range(1, cols+1):
                print('we are filling ',i,j)
                if word1[i-1]==word2[j-1]:
                    distance[i][j] = distance[i-1][j-1] # both strings increased by length 1 and the incoming character was same
                else:
                    distance[i][j] = 1 + min(distance[i-1][j], distance[i][j-1], distance[i-1][j-1]) 
        return distance[rows][cols]
        




assert Solution.minDistance('horse', 'ros') == 3