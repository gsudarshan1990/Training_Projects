#This is another python program on iterator


class yrange:
    def __init__(self, num):
        self.index = 0
        self.num = num

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == self.num:
            raise StopIteration
        else:
            i = self.index
            self.index+=1
            return i

numbers = yrange(5)
for num in numbers:
    print(num)