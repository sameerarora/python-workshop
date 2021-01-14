from collections import defaultdict
msg = "John told me I will see you tomorrow"

dic = {}

for letter in msg.lower():
    dic[letter] = dic.get(letter, 0) + 1

print(dic)

def_d = defaultdict(int)

for letter in msg.lower():
    def_d[letter] += 1

print(def_d.keys())
