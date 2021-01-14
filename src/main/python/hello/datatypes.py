word = 'applesarefreshfromthefarm'
from collections import defaultdict

dictionary = defaultdict(int)

for letter in word:
    if letter not in 'aeiou':
        dictionary[letter] += 1

print(dictionary)

from collections import Counter

print(Counter(word))