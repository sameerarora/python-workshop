colors = ['black', 'white']
sizes = ['S', 'M', 'L']
sleeves = ['long', 'short']
# #black in Large size with short sleeves

dic = {"S": "Small", "M": "Medium", "L": "Large"}

options = [f"{color} in {dic[size]} size with {sleeve} sleeves"
           for color in colors
           for size in sizes
           for sleeve in sleeves]


print("\n".join(options))



# map(lambda x: x ** 2, l)

# TODO l[0:5:-1]
