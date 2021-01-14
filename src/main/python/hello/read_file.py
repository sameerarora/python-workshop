import re


#
# for line in open('../../resources/poem.txt'):
#     if re.search('the', line):
#         substituted = re.sub('the', 'THE', line)
#         print(substituted, end='')


# * let's write a function which takes a word as an argument and outputs the plural of that word
# * the program should follow these rules:
#   * if the word ends in 's', 'x', or 'z', the plural adds 'es', e.g., ax => axes, loss => losses -> '[sxz]$'
#   * if the word ends in an 'h', which is not preceded by a vowel or 'd', 'g', 'k', 'p', 'r', or 't', the plural adds 'es', e.g., moth => moths, but match => matches
# -> '[^aeioudgkprt]h$'
#   * if the word ends in a 'y' which is not preceded by a vowel, then the plural strips the 'y' and adds 'ies', e.g., baby => babies, but boy => boys
# -> [^aeiou]y$
#   * otherwise just add 's'

# test -> tests
# anomaly -> anomalies
# boy -> boys
# loss -> losses
def pluralize(noun):
    if re.search('[sxz]$', noun):
        return noun + 'es'
    elif re.search('[^aeioudgkprt]h$', noun):
        return noun + 'es'
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

#Object oriented and advanced data types

print(pluralize("test"))
print(pluralize("anomaly"))
print(pluralize("loss"))
