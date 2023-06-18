# Given an integer array and number k, output all unique pairs that sum up to k

# sum_arry = [1,3,5,9,8,4,8]

# for x in sum_arry:
#     a = sum_arry
#     a.remove(x)
#     for i in a:
#         print(sum_arry)
#         print(f"x is : {x} and i is : {i}")
#         print(x+i)

def findPairs(arr, k): 
    seen = set() 
    output = set() 
  
    for num in arr: 
        target = k - num 
        if target not in seen: 
            seen.add(num) 
        else: 
            output.add((min(num,target), max(num,target))) 

    return output  

  
arr = [1,3,5,9,8,4,8] 
k = 8
print(findPairs(arr, k))