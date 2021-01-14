class Demo:
    def __init__(self):
        self.one = 1
        self.two = 2
        # self.readonly = 'do not change'
        super().__setattr__('readonly', 'do not change')
        # super(Demo, self).__setattr__...

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            return 'whoop!'

    def __setattr__(self, attr, value):
        print('setting attribute', attr)
        if attr != 'readonly':
            self.__dict__[attr] = value
        else:
            print('nyah!')

d= Demo()

d.name = "Sameer"
d.age = 40

print(d.name)
print(d.age)
