class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
         # Take the first string as our reference point
        first_str = strs[0]
        
        # Loop through every character index of the first string
        for i in range(len(first_str)):
            char = first_str[i]
            
            # Compare this character with the same index in all other strings
            for other_str in strs[1:]:
                # If we reach the end of any string, or find a mismatch
                if i >= len(other_str) or other_str[i] != char:
                    # Return everything we matched up to this point
                    return first_str[:i]
                    
        return first_str