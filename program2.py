def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    string = ""
    for i in s:
        if i in string:
            string = ""
            string += i
        else :
            string += i

    return len(string)
print(longest_substring("abcdefghijklmnopqrstuvwxyz"))