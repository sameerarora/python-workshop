word = "supercaligraphicschallengeaccepted"

print(word[::-1])

print(type(word))
# its a list of characters
vowels = ['a', 'e', 'i', 'o', 'u']
for letter in word:
    if letter not in 'aeoiu':
        print(letter, end='')

numbers = [1, 2, 3, 4, 5]
print("")
for i in range(10):
    if i in numbers:
        print(i, end=' ')
