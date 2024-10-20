#Imports
import re
import matplotlib.pyplot as plt

#Ex 3:
num_linhas = 0
doentes = 0
masc, fem = 0, 0
idades, escalao = [], {}
#exp = "(\d+),([MF]),\d+,\d+,\d+,1$"

myHeart = open("myheart.csv", "r")
myHeart.readline()

for linha in myHeart:
    num_linhas += 1
    res = re.match(r'(\d+),([MF]),\d+,\d+,\d+,1$', linha)
    if  res:
        doentes += 1
        idades.append(int(res.group(1)))
        if res.group(2) == "M":
            masc += 1
        else: 
            fem += 1

myHeart.close()

p_doentes = (doentes/num_linhas)*100
p_masc = (masc/doentes)*100
p_fem = (fem/doentes)*100

for i in idades:
    e = (i//5)-6
    if e not in escalao.keys():
        escalao[e] = 1
    else:
        escalao[e] += 1

fig, ax = plt.subplots()

ax.pie([doentes,num_linhas-doentes])
plt.legend(["Pacientes doentes", "Pacientes saudáveis"])
plt.savefig("imagem.png")

ax.pie([masc, fem])
plt.legend(["Masculino", "Feminino"])
plt.savefig("imagem1.png")

#HTML
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
        <h2>Doentes Totais e por Género</h2>
        <p>Dentre os {num_linhas} pacientes, {doentes} encontram-se doentes. Isso representa {p_doentes:.2f}%</p>
        <img src="imagem.png" alt="Porcentagem doentes">
        <p>Dos {doentes} pacientes doentes, {masc} são homens e {fem} são mulheres. Isso representa, respetivamente {p_masc:.2f}% e {p_fem:.2f}%</p>
        <img src="imagem1.png" alt="Porcentagem homem/mulher">
    </div>
    <div class="section">
        <h2>Distribuição por Escalões Etários</h2>
        <p>Abaixo podemos ver o gráfico.</p>
        <img src="imagem2.png" alt="Descrição da imagem 2">
    </div>
    <div class="section">
        <h2>Distribuição por Níveis de Colesterol</h2>
        <p>Este é o texto descritivo abaixo do terceiro subtítulo. O conteúdo deve complementar a imagem logo abaixo.</p>
        <img src="imagem3.png" alt="Descrição da imagem 3">
    </div>
    <div class="section">
        <h2>Correlação Tensão/Batimento e Doença</h2>
        <p>Este é o texto descritivo abaixo do quarto subtítulo. Coloque aqui as informações adicionais desejadas.</p>
        <img src="imagem4.png" alt="Descrição da imagem 4">
    </div>
</body>
</html>
"""
ficheiro = open("plc24TP1gr15.html", "w", encoding="utf-8")
ficheiro.write(conteudo_html)
ficheiro.close()