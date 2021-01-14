class Word(str):
    def __init__(self, string):
        self.string = string

    def __gt__(self, other):
        return len(self.string) > len(other.string)


a = Word('apple')

b = Word('fig')

print(a > b)

print(type(Word))

fruits = [Word("Apple"), Word("Fig"), Word("Banana"), Word("Pineapple")]
print(sorted(fruits, key=len))
