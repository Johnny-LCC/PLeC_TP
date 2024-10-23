'''
Resolução do exercício 2 pelo Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''
#Imports
import re
#import matplotlib.pyplot as plt

#Variáveis
num_linha = 0
minIdade, maxIdade = 1000, 0
masc, fem = 0, 0
modsAno = {}
er1 = ",(\d+),([MF]),"
er2 = ",(\d{4})-\d{2}-\d{2},.+,[MF],[A-z]+,([A-zãçé]+),"
#"[a-z0-9]+,\d+,\d{4}-\d{2}-\d{2},[A-z]+,[A-z]+,\d+,[MF],[A-z]+,[A-z]+,[A-z]+,[A-zã@\.]+,true|false,true|false"

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
            modsAno[ano][mod] = 1
        else:
            if mod not in modsAno[ano].keys():
                modsAno[ano][mod] = 1
            else:
                modsAno[ano][mod] += 1

emd.close()

print(f"Min: {minIdade}, Max: {maxIdade}")
print(f"Num_Total: {num_linha}, Homens: {masc}, Mulheres: {fem}")
for k in modsAno.keys():
    print(f"{k}: {modsAno[k]}")
'''
#Cálculos auxiliares
pMasc = (masc/num_linha)*100
pFem = (fem/num_linha)*100

#Matplotlib
plt.pie([masc,fem], startangle=90)
plt.legend(["Homens","Mulheres"])
plt.savefig("imagem1.png")
plt.close()

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
        <h2>Distribuição por Níveis de Colesterol</h2>
        <p>Texto.</p>
        <img src="imagem3.png" alt="Barras colesterol doentes">
    </div>
    <div class="section">
        <h2>Correlação Tensão/Batimento e Doença</h2>
        <p>Texto.</p>
        <img src="imagem4.png" alt="Correlação Tensão">
    </div>
</body>
</html>
"""
ficheiro = open("index.html", "w", encoding="utf-8")
ficheiro.write(conteudo_html)
ficheiro.close()
'''