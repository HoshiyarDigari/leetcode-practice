
def gcdOfStrings( str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        shorter_string = str1 if (len(str1) < len(str2)) else str2
        gcd  = shorter_string
        # check if the candidate divides both str1 and str2 correctly
        while gcd:
            print('in while candidate', gcd)
            # check if the gcd_candidates length divides both strings
            
            if  len(str1)%len(gcd) == 0 and len(str2)%len(gcd)==0:
                # now check if we can reconstruct the strings by repeating the pattern of gcd_candidate
                if str1 == gcd * (len(str1)//len(gcd)) and str2 == gcd* (len(str2)//len(gcd)):
                     print('gcd found', gcd)
            else:
                gcd = gcd[:-1]
                
        print('out of while', gcd)
      
             
        return gcd
