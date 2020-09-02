#This python program

from abc import ABC, abstractmethod

class Hominidae(ABC):

    @abstractmethod
    def diet(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class Humans(Hominidae):

    def diet(self):
        print('Humans are corinivores')

cathy = Humans()