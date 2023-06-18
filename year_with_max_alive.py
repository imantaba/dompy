# Question :
# Given an array of birth and death years, return a year that has the highest number of alive people.
# Assume no one dies before they're one aka death year > birth year
# Ex :
# [[2000,2005],[1990,2005],[2005,2010],[1980,1995]]   return -> 2005

list = [[2000,2005],[1990,2005],[2005,2010],[1980,1995]]


class YearWithMaxAlive:
    def __init__(self, list):
        self._year = _FindYear(list)
    def print_year(self):
        result = self._year.year_max_alive()
        print(max(result, key=result.get))

class _FindYear:
    def __init__(self, list):
        self.list = list
    def year_max_alive(self):
        dic = {}
        lst = self._create_complete_list(list)
        for year in lst:
            if year in dic:
                dic[year] += 1
            else:
                dic[year] = 1
        return dic
    def _create_complete_list(self, list):
        complete_list = []
        for items in list:
            for i in range(items[0], items[1]+1):
                complete_list.append(i)
        return complete_list

a = YearWithMaxAlive(list)
a.print_year()