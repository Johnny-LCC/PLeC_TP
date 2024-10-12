'''
Grupo 15 
Ex 2? 3? 
Acho q o ex5 vai ser meio complicado...
'''

#Imports
import re
import sys

#Ex 3:
myHeart = open("myheart.csv", "r")
myHeart.readline()

num_linhas = 0
doentes = 0
masc, fem = 0, 0
idades, escalao = [], {}

exp = "(\d+),([MF]),(\d+),(\d+),(\d+),([01])$"
#([0-9][1-9]),(M|F),([0-9]{1,3}),([0-9]{1,3}),([0-9]{2,3}),(0|1)
for linha in myHeart:
    res = re.match(rf'{exp}', linha)

    num_linhas += 1 #if res:
    if int(res.group(6)) == 1:
        doentes += 1
        idades.append(int(res.group(1)))
        if res.group(2) == "M":
            masc += 1
        else: 
            fem += 1

for i in idades:
    e = (i//5)-6
    if e not in escalao.keys():
        escalao[e] = 1
    else:
        escalao[e] += 1

print(f"{num_linhas} linhas lidas\n{doentes} doentes - {masc} homens e {fem} mulheres") #HTML
escalao = sorted(list(escalao.items()))
for (e,n) in escalao:
    i = (e+6)*5
    f  = i+4
    print(f"[{i},{f}]: {n} doentes")

myHeart.close()

'''
839 linhas lidas
468 doentes - 428 homens e 40 mulheres
'''