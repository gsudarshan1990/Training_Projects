#This python program is function on class


class Myclass:
    def printlist1(*args):
        for count, item in enumerate(args):
            print("{0}.{1}".format({count},{item}))

    def printlist2(**kwargs):
        for key, value in kwargs.items():
            print("{} likes {}".format(key,value))

Myclass.printlist1("Red","Green","yellow")
Myclass.printlist2(rahul='green',sonu='red')

