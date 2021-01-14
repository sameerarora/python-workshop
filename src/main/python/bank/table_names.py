import re

for line in open('../../resources/poem.txt'):
    if re.search('the', line):
        substituted = re.sub('the', 'THE', line)
        print(substituted, end='')
