class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name}，我今年{self.age}岁了')

per=Person('wyl',22)
print(per)#打印输出per的内存地址

