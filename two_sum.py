sum_arry = [1,3,5,9,8,4,8]

for x in sum_arry:
    a = sum_arry
    a.remove(x)
    for i in a:
        print(sum_arry)
        print(f"x is : {x} and i is : {i}")
        print(x+i)