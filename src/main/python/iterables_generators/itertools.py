from itertools import zip_longest

list1 = ['a', 'b', 'c', 'd','e']
list2 = ['apple', 'banana', 'cherry']

print(list(zip_longest(list1, list2, fillvalue='*****')))
