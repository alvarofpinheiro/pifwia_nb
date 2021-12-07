#NB
import math
import random
import matplotlib.pyplot as plt

DIMENSAO = 4
entrada_testes = [5.1,3.5,1.4,2.0]

# 5.1,3.5,1.4,0.2,Iris-setosa
# 7.0,3.2,4.7,1.4,Iris-versicolor
# 7.9,3.8,6.4,2.0,Iris-virginica

input_list = []

for i in inputs_treinamento:
  if i != '':
    aux = i.split(",")
    item = [float(aux[0]), float(aux[1]), float(aux[2]), float(aux[3]), aux[4]]
    input_list.append(item)

print(input_list)

possiveis_saidas = []
for i in input_list:
  if i[4] not in possiveis_saidas:
    possiveis_saidas.append(i[4])
    
print(possiveis_saidas)

dados_separados_por_classe = []
for i in possiveis_saidas:
  dados_separados_por_classe.append([])

for i in input_list:
  for index, j in enumerate(possiveis_saidas):
    if i[4] == j:
      dados_separados_por_classe[index].append(i[:4])

#Media

def media(entrada):
	return sum(entrada)/len(entrada)
 
#Variancia

def variancia(entrada):
  media_entrada = media(entrada)
  aux = 0
  for i in entrada:
    aux += (i - media_entrada)**2
  aux = aux/(len(entrada)-1)
  return aux

#Calculando a probabilidade de um determinado valor
def probabilidade(valor, media, variancia):
	aux = math.exp(-((valor - media)**2 / (2 * variancia)))
	return (1 / math.sqrt(2 * math.pi * variancia)) * aux

#Calculando as probabilidades da entrada

probabilidades = []
for index, classe in enumerate(possiveis_saidas):
  prob = 1
  for dimensao in range(DIMENSAO):
    aux = []
    for entrada in dados_separados_por_classe[index]:
      aux.append(entrada[dimensao])
    med = media(aux)
    var = variancia(aux)
    prob *= probabilidade(entrada_testes[dimensao], med, var)
  probabilidades.append(prob)

#Verificando qual classe tem maior probabilidade

best_prob = 0
best = -1
for i in range(len(probabilidades)):
  if probabilidades[i] > best_prob:
    best_prob = probabilidades[i]
    best = i

print(possiveis_saidas[best])