'''
Resolução do exercício 2 pelo Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''
#Imports
import re
import matplotlib.pyplot as plt

#Variáveis
num_linha = 0
minIdade, maxIdade = 1000, 0
masc, fem = 0, 0
modsAno = {}
apts, total = {}, {}

er1 = ",(\d+),([MF]),"
er2 = ",(\d{4})-\d{2}-\d{2},.+,[MF],[A-z]+,([A-zãçé]+),"
er3 = ".+,(\d{4})-\d{2}-\d{2},.+,(true|false)$"

#Leitura ficheiro
emd = open("emd.csv", "r")
emd.readline()
for linha in emd:
    num_linha += 1
    
    res1 = re.search(rf'{er1}',linha)
    if res1:
        idade = int(res1.group(1))
        if idade < minIdade:
            minIdade = idade
        if idade > maxIdade:
            maxIdade = idade
        if res1.group(2) == "M":
            masc += 1
        else:
            fem += 1
    
    res2 = re.search(rf'{er2}', linha)
    if res2:
        ano = int(res2.group(1))
        mod = res2.group(2)
        if ano not in modsAno.keys():
            modsAno[ano] = {}
        if mod not in modsAno[ano].keys():
            modsAno[ano][mod] = 0
        modsAno[ano][mod] += 1

    res3 = re.match(rf'{er3}', linha)
    if res3:
        ano = int(res3.group(1))
        if ano not in apts.keys():
            apts[ano] = 0
        if ano not in total.keys():
            total[ano] = 0
        total[ano] += 1
        if res3.group(2) == 'true':
            apts[ano] += 1
emd.close()

#Cálculos auxiliares e Matplotlib
pMasc = (masc/num_linha)*100
pFem = (fem/num_linha)*100

plt.pie([masc,fem], startangle=90)
plt.legend(["Homens","Mulheres"])
plt.savefig("imagem1.png")
plt.close()

mods = {}
for a in sorted(modsAno.keys()):
    x, y = [], []
    for m in sorted(modsAno[a].keys()):
        x.append(m)
        y.append(modsAno[a][m])
        if m not in mods.keys():
            mods[m] = 0
        mods[m]+=modsAno[a][m]
    plt.barh(x,y) ##
    plt.title(f"{a}")
    plt.savefig(f"imagem2-{a}.png")
    plt.close()
xmod = [i[0] for i in sorted(mods.items())]
ymod = [i[1] for i in sorted(mods.items())]
plt.barh(xmod,ymod) ##
plt.title("Total")
plt.savefig("imagem2-total.png")

for k in apts.keys():
    print(f"{k}: {apts[k]}/{total[k]}") ##

#Ficheiro HTML
conteudo_html = f"""<!DOCTYPE html>
<html lang="eng">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ex3</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        h2 {{
            color: #007BFF;
        }}
        .section {{
            margin-bottom: 30px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>Processador de registos de Doenças Cardíacas</h1>
    <div class="section">
        <h2>Idades Extremas do Dataset</h2>
        <p>Neste dataset, a idade mínima é {minIdade} e a idade máxima é {maxIdade}.</p>
    </div>
    <div class="section">
        <h2>Distribuição dos atletas por género</h2>
        <p>Dentre os {num_linha} atletas, {masc} são homens e {fem} são mulheres.</p>
        <img src="imagem1.png" alt="Pie Chart">
        <p>Isso representa {pMasc}% e {pFem}% respetivamente<\p>
    </div>
    <div class="section">
        <h2>Distribuição das modalidades desportivas</h2>
        <p>Texto.</p>
        <img src="imagem2.png" alt="mods">
    </div>
    <div class="section">
        <h2>Aptos</h2>
        <p>Texto.</p>
        <img>
    </div>
</body>
</html>
"""
ficheiro = open("index.html", "w", encoding="utf-8")
ficheiro.write(conteudo_html)
ficheiro.close()