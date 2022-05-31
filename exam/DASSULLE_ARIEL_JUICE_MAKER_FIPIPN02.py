from ctypes import sizeof
from itertools import count
from enum import Enum


class TypeSize(Enum):
    Small = 0
    Medium = 0.5
    Large = 1



count = float
class ChoixJus:
    def __init__(self, name, price,size=TypeSize.Small):
        self.name = name
        self.price = price
        self.size= size

    def info(self):
        return self.name + ': $' + str(self.price)

    def get_total_price(self):
        
        if self.size == TypeSize.Small :
            return self.price

        if self.size == TypeSize.Medium :
            return self.price+0.5

        if self.size == TypeSize.Large :
            return self.price+1
  
    def setSize (self,size) :
        self.size=size
        


class Juice(ChoixJus):
    # Define the __init__ method
    def __init__(self, name, price):
        super().__init__(name, price)

Juice1 = Juice('The Boost', 5)
Juice2 = Juice('The Fresh', 4)
Juice3 = Juice('The Fusion', 5)
Juice4 = Juice('The Detox', 3.5)

Juices = [Juice1, Juice2, Juice3,Juice4]



print('Juices')
index = 0
for Juice in Juices:
    print(str(index) + '. ' + Juice.info())
    index += 1

print('--------------------')


Juice_order = int(input('Enter Juice item number: '))
inputSize= input('Enter Size wanted (S for small, M for Medium, L for Large): ')


   
if inputSize in ["S", "s"]:
    SizeWanted= TypeSize.Small

if inputSize in ["M", "m"]:
    SizeWanted=TypeSize.Medium

if inputSize in ["L", "l"]:
    SizeWanted=TypeSize.Large



selected_Juice = Juices[Juice_order]
# Call the get_total_price method from selected_food and from selected_Juice
selected_Juice.setSize(SizeWanted)
prix =selected_Juice.get_total_price()


# Output 'Your total is $____'
print('Your total is $', prix)