from functools import partial

print_with_tabs = partial(print, end='\t')

sorted_r = partial(sorted, reverse=True)
print(sorted_r([-1, -2, 6, 0, 7, 14]))

sorted_str_r = partial(sorted, key=lambda x: x[::-1])
print(sorted_str_r(['pineapple', 'apple', 'guava', 'fig', 'banana']))
# sorted_r = partial(sorted, key=lambda w: w[::-1])
#
# print_no_nl = partial(print, end=' ')
# print_no_sp = partial(print_no_nl, sep='-')
#
# print_no_sp("01", "01", "2020")
#
# print_no_nl("I am")
# print_no_nl("Loving Python")
#create a __`print_no_nl()`__ function which allows you to print something without a trailing newline, without having to specify __`end=''`__

print_no_nl  = partial(print, sep='-', end='\t')

print_no_nl("abc", "def", "xyz")
print_no_nl("uvw")
print_no_nl("another")