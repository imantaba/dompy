
# Given an array of birth and death years, return a year that has the highest number of alive people.
# Assume no one dies before they're one aka death year > birth year
# Ex :
# [[2000,2005],[1990,2005],[2005,2010],[1980,1995]]   return -> 2005

list = [[2000,2005],[1990,2005],[2005,2010],[1980,1995]]
dic = {}
complete_list = []
for items in list:
    for i in range(items[0], items[1]+1):
        complete_list.append(i)

for year in complete_list:
    if year in dic:
        dic[year] += 1
    else:
        dic[year] = 1

value_list = []
print(max(dic, key=dic.get))   