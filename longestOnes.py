def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        algo:
        
        """
        left = 0 
        right = k - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
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