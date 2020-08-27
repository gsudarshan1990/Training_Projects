#This python program demonstrates the read only property


class ReadOnly:

    @property
    def constant(self):
        return 24

only_read = ReadOnly()
print('%d is the constant value'%(only_read.constant))

try:
    only_read.constant =25
except AttributeError as e:
    print(e)