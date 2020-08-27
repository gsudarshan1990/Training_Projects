#This python program is about context manager


class ContextManager(object):
    def _init_(self):
        self.entered = False

    def _enter_(self):
        self.entered = True
        return self

    def _exit_(self, exc_type, exc_instance, traceback):
        self.entered = False

'''
c= ContextManagerAnotherExample()
print(c.entered)
'''

with ContextManager() as cm:
    print('hello')
    print(cm.entered)