def smallest_missing_positive_integer(nums: list[int]) -> int:
    """
    Implement the function smallest_missing_positive_integer 
    using the provided smallest_missing_positive_integer function 
    to find the smallest missing positive integer in the given list.

    """
    num = ["false"]*(max(nums)+1)
    for i in range(0, max(nums)):
        num[i] = "false"
        
    for i in nums:
        if(i<0):
            continue
        else:
            num[i] = "true"
    for i in range(1,len(num)):
        if(num[i]== "false"):
            return i
        else:
            continue
        
    return len(num)





print(smallest_missing_positive_integer([-1, -3, 4, 2]))



  

