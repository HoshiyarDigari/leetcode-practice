def isSubsequence(s, t):
     """
     :type s: str
     :type t: str
     :rtype: bool
     """
     # pointers to keep track of location in the two strings
     s_index = 0
     t_index = 0
     print(s,t)
     # start with first element of s 
     if not s:
         return True
     while s_index <= len(s) -1 and t_index < len(t):
        print('checking for ', s[s_index])
        # compare with elements in t to find this character of s
        while t_index < len(t):
            print('comparing t element ', t[t_index], 'against s element', s[s_index])
            if t[t_index] == s[s_index]:
                s_index+=1
            t_index+=1
        if s_index== len(s):
            print(True)
            return True
     return False
        
        

          
          

if __name__ == "__main__":
    t = "ahbgdc"
    s = ""
    isSubsequence(s,t)