def maxVowels( s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        algo:
        sliding window of k size , keeping track of number of distinct vowels seen in any of the windows
        we compare the outgoing index at current left - 1 , to see if it was a vowel or not similar for included element at current right. if both are vowels, we move on else, we adjust the vowel count accordingly
        optimizations:
        use ternary operations for adding and subtracting vowel count
        use for loop instead of while loop

        """
        left = 0 
        right = k - 1
        vowels = ('a', 'e', 'i', 'o', 'u')
        max_vowels = 0

        # 1st window
        for i in range(left, right + 1):
            if s[i] in vowels:
                max_vowels += 1

        window_vowels = max_vowels

        # Sliding window with a for loop
        for right in range(k, len(s)):
            window_vowels += (s[right] in vowels) - (s[right - k] in vowels)
            if window_vowels > max_vowels:
                max_vowels = window_vowels
        print(max_vowels)
        return max_vowels
            
              
              






if __name__ == "__main__":
    s="ppuuoibwiogewxvgxvugwatxebstgdciswnkynvsbktfrrzxddzpjzvmqnjigkyviwoniyfkhadnqgihbobjjgcmmmnqzsckkqnfonepbgvzrnwxlrdawkwwbnwfouofdtskznfglbsfdaulxj"
    k = 20
    maxVowels(s, k)