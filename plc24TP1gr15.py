'''
Grupo 15 
Ex 2? 3? 
Acho q o ex5 vai ser meio complicado...
'''

#Imports
import re
import sys

#Ex 3: r"([0-9][1-9]),(M|F),([0-9]{1,3}),([0-9]{1,3}),([0-9]{2,3}),(0|1)" (???)
myHeart = open("myheart.csv", "r")
myHeart.readline()
linha = myHeart.readline()
print(linha)
''''''
myHeart.close()