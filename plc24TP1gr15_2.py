'''
Resolução do exercício 3 pelo Grupo 15
João Fonseca - A102512
Alexis Correia - A102495
'''
#Imports
import re
import matplotlib.pyplot as plt

#Variáveis
num_linhas = 0
doentes, masc, fem = 0, 0, 0
idades = {}
col = []
tensao, bpm = {}, {}

#Leitura ficheiro
myHeart = open("myheart.csv", "r")
myHeart.readline()
for linha in myHeart:
    num_linhas += 1
    res = re.match(r'(\d+),([MF]),(\d+),(\d+),(\d+),1$', linha) #ER
    if  res:
        doentes += 1
        
        i = int(res.group(1))
        e = (i//5)-6
        if e not in idades.keys():
            idades[e] = 1
        else:
            idades[e] += 1
        
        if res.group(2) == "M":
            masc += 1
        else: 
            fem += 1

        col.append(int(res.group(4)))

        t, b = int(res.group(3)), int(res.group(5))
        if t not in tensao.keys():
            tensao[t] = 1
        else:
            tensao[t] += 1
        if b not in bpm.keys():
            bpm[b] = 1
        else:
            bpm[b] += 1
myHeart.close()

#Cálculos auxiliares
p_doentes = (doentes/num_linhas)*100
p_masc = (masc/doentes)*100
p_fem = (fem/doentes)*100

xidades, yidades = [],[]
for x,y in sorted(idades.items()):
    i = (x+6)*5
    f = i+4
    xidades.append(f"{i}-{f}")
    yidades.append(y)

dCol = {}
for c in col:
    if c>0:
        c = (c//10)*10
    if c not in dCol.keys():
        dCol[c] = 1
    else:
        dCol[c] += 1
xcol, ycol = [], []
for x,y in sorted(dCol.items()):
    if c >= 10:
        xcol.append(f"{x}-{x+9}")
    else:
        xcol.append("ND")
    ycol.append(y)

xtensao, ytensao = [], []
for x,y in sorted(tensao.items()):
    xtensao.append(x)
    ytensao.append(y)

xbpm, ybpm = [], []
for x,y in sorted(bpm.items()):
    xbpm.append(x)
    ybpm.append(y)

#Matplotlib
plt.pie([doentes,num_linhas-doentes], startangle=90)
plt.legend(["Doentes", "Saudáveis"], title="Pacientes: ")
plt.savefig("imagem.png")
plt.close()

plt.pie([masc, fem], startangle=90)
plt.legend(["Masculino", "Feminino"], title = "Doentes por género: ")
plt.savefig("imagem1.png")
plt.close()

plt.bar(xidades,yidades)
plt.ylabel("Número doentes")
plt.xlabel("Escalões Etários")
plt.savefig("imagem2.png")
plt.close()

plt.figure(figsize=(10,8))
plt.barh(xcol,ycol)
plt.ylabel("Nível colesterol")
plt.xlabel("Número doentes")
plt.savefig("imagem3.png")
plt.close()

plt.subplot(1,2,1)
plt.plot(xtensao,ytensao) ###
plt.title("Tensão")
plt.subplot(1,2,2)
plt.plot(xbpm, ybpm) ###
plt.title("Batimentos")
plt.savefig("imagem4.png")
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
            color: #385ea1;
        }}
        .section {{
            margin-bottom: 30px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
        .img-container {{
            text-align: center;
        }}
        img {{
            text-align: center;
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <h1>Processador de registos de Doenças Cardíacas</h1>
    <div class="section">
        <h2>Doentes Totais e por Género</h2>
        <p>Dentre os {num_linhas} pacientes, {doentes} encontram-se doentes. Isso representa {p_doentes:.2f}% do total de pacientes.</p>
        <div class="img-container">
            <img src="imagem.png" alt="Porcentagem doentes">
        </div>
        <p>Dos {doentes} pacientes doentes, {masc} são homens e {fem} são mulheres. Isso representa, respetivamente, {p_masc:.2f}% e {p_fem:.2f}% dos pacientes doentes.</p>
        <div class="img-container">
            <img src="imagem1.png" alt="Porcentagem homem/mulher">
        </div>
    </div>
    <div class="section">
        <h2>Distribuição por Escalões Etários</h2>
        <p>Abaixo podemos ver o gráfico em barras que representa a distribuição dos doentes de acordo com seu Escalão de Idade.</p>
        <div class="img-container">
            <img src="imagem2.png" alt="Barras idades doentes">
        </div>
    </div>
    <div class="section">
        <h2>Distribuição por Níveis de Colesterol</h2>
        <p>Este é o gráfico que apresenta a distribuição de doentes de acordo com os seus níveis de colesterol.</p>
        <div class="img-container">
            <img src="imagem3.png" alt="Barras colesterol doentes">
        </div>
    </div>
    <div class="section">
        <h2>Correlação Tensão/Batimento e Doença</h2>
        <p>Com auxílio de ambos os gráficos abaixo podemos ver a correlação entre a Tensão e Batimentos com a doença.</p>
        <p>No eixo x, podemos ver a tensão/batimentos e, no eixo y, o número de paciente doentes correspondentes.</p>
        <div class="img-container">
            <img src="imagem4.png" alt="Tensão/Batimentos">
        </div>
        <p>Podemos notar, em ambos os gráficos, o intervalo no qual há um pico de pacientes doentes.</p>
    </div>
</body>
</html>
"""
ficheiro = open("index.html", "w", encoding="utf-8")
ficheiro.write(conteudo_html)
ficheiro.close()
print("ficheiro HTML pronto")