def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    string = ""
    maxi = 0
    for i in s:
        if i in string:
            maxi = max(len(string), maxi)
        else : 
            string += i

    return maxi



print(longest_substring("abcabcbb"))