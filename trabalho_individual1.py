# -*- coding: utf-8 -*-
"""Trabalho-individual1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DVt8lkpsaoQF-l-Gb-yI5L263lml9niu

# SEÇÃO 1 TRABALHO INDIVIDUAL - MÓDULO 4

**Uma determinada loja deseja produzir relatórios
semanais com ganhos e despesas. O gerente da
loja te contratou para gerar um relatório de uma
semana para mostrar ao dono da loja como a
análise dos dados pode ser útil para eles. Para
isso, ele te enviou uma tabela de exemplo das
despesas de uma semana:
CONTEXTO
Além disso, ele informou que os ganhos não estão nessa planilha, mas que ele
possui a seguinte lista: 2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893
respectivos aos dias da semana. Ele te deixou bem livre para incluir no relatório as
estatísticas que desejar, mas ele deseja que o relatório contenha outros dados que
veremos a seguir.**



|Dia|Limpeza|Comida|Transporte|Outros|
|---|---|---|---|---|
|segunda|100|221.60|150|0|
|terça|0|375.31|100|0
|quarta|100|412.00|125|2310|
|quinta|0|495.20|300|500|
|sexta|100|245.00|525|0|
|sábado|100|245.00|525|0|
|domingo|0|164.00|75|820|

 CONTEXTO Além disso, ele informou que os ganhos não estão nessa planilha, mas que ele possui a seguinte lista: 2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893 respectivos aos dias da semana. Ele te deixou bem livre para incluir no relatório as estatísticas que desejar, mas ele deseja que o relatório contenha outros dados que veremos a seguir.

**DATA FRAME**
---
"""

import pandas as pd
#dícionario para armanezar dados entregues pela loja
dados_semanais = {'Limpeza':[100,0,100,0,100,100,0,400.00,57.14], 'Comida':[221.60, 375.31, 412.00, 495.20, 411.53, 245.00, 164.00, 2324.64, 332.09], 'Transporte':[150,100,125,300,275,525,75,1550.00,221.43], 'Outros':[0,0,2310,500,0,0,820,3630.00,518.57], 'Ganhos':[2200, 2420.50, 3391, 5322, 4898.50, 4200, 3893, 26325, 3760.71]}
df = pd.DataFrame(dados_semanais, index = ['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo','Total','Média'])
df
Limpeza	Comida	Transporte	Outros	Ganhos
Segunda	100.00	221.60	150.00	0.00	2200.00
Terça	0.00	375.31	100.00	0.00	2420.50
Quarta	100.00	412.00	125.00	2310.00	3391.00
Quinta	0.00	495.20	300.00	500.00	5322.00
Sexta	100.00	411.53	275.00	0.00	4898.50
Sábado	100.00	245.00	525.00	0.00	4200.00
Domingo	0.00	164.00	75.00	820.00	3893.00
Total	400.00	2324.64	1550.00	3630.00	26325.00
Média	57.14	332.09	221.43	518.57	3760.71

"""# DIMINUIR 7%

dados de ganhos de cada dia da semana e subtraído o imposto de 7%.
"""

Ganhos_diarios = df[:7]['Ganhos']
Ganhos_diarios * 0.93

Segunda    2046.000
Terça      2251.065
Quarta     3153.630
Quinta     4949.460
Sexta      4555.605
Sábado     3906.000
Domingo    3620.490
Name: Ganhos, dtype: float64

"""**TOTAL DOS GANHOS**
---

foi selecionado o total dos ganhos.
"""

Total_Ganhos = df['Ganhos']['Total']
Total_Ganhos

"""#MÉDIA DOS GANHOS SEMANAIS

foi selecionado na tabela a média do ganho semanal.
"""

Media_Ganhos = df['Ganhos']['Média']
Media_Ganhos

"""#SOMA TOTAL DAS DESPESAS

foram selecionados os valores das despesas: Limpeza, Comida, Transporte e Outros.
"""

Dados_semanais = df[['Limpeza', 'Comida', 'Transporte', 'Outros']]
Dados_semanais.loc['Total']

"""#MÉDIA SEMANAL DAS DESPESAS

selecionados os mesmos valores a cima, porém buscando a média semanal.
"""

Dados_semanais.loc['Média']

"""#LUCRO DIÁRO

cálculo com as despesas por dia e depois efetuado um cálculo com ganhos diários.
"""

df ['Lucro'] = df ['Ganhos'] - (df ['Limpeza'] + df ['Outros'] + df['Comida'] + df ['Transporte'])
df

"""#LUCRO SEMANAL

soma do total das despesas semanais e esse valor foi executado do valor ganhos semanais e revertendo o resultado.
"""

Lucro_semanais = df['Lucro']
Lucro_semanais
Segunda     1728.40
Terça       1945.19
Quarta       444.00
Quinta      4026.80
Sexta       4111.97
Sábado      3330.00
Domingo     2834.00
Total      18420.36
Média       2631.48
Name: Lucro, dtype: float64
