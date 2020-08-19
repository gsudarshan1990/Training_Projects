"""
This python program describes about the types of different python objects
"""

print('The type of 1 is :',type(1))
print('The type of [] is:',type([]))
A_Class = type('A_class', (), {})
print('The type of A_Class  is : ',type(A_Class))
an_inst = A_Class()
print('The type of an_inst is :',type(an_inst))
A_type = type('A_type',(),{'start':1 ,'a_method': lambda self:'This is an instance of '+str(self.__class__)})
type_inst = A_type()
print('The type of A_type is :',type(A_type))
print('The type of type_inst is:',type(type_inst))
print('Calling a method returns ',type_inst.a_method())
class Basic():
    start = 1
    def a_method(self):
        return 'This is an instance of '+str(self.__class__)

basic_inst = Basic()
print('type type of Basic is:',type(Basic))
print('type of basic_inst is :',type(basic_inst))
print('Calling a method returns :', basic_inst.a_method())
