
# Comentario
import random


numero1 = 10444
numero2 = 2044444
numero3 = 152222
numero4 = 3333
# maior numero ??????
#operadores LOGICOS 


if (numero1 > numero2):
    print(f"Numero 1 -> {numero1}  é maior")
else:
    print(f"Numero 2 -> {numero2}  é maior")


#  3 numeros 
'''
if (numero1 > numero2) and (numero1 > numero3):
    print(f"Numero 1 -> {numero1}  é maior")
elif (numero2 > numero1) and (numero2 > numero3):
    print(f"Numero 2 -> {numero2}  é maior")
else:
    print(f"Numero 3 -> {numero2}  é maior")
'''    
# 4 numeros
'''
if (numero1 > numero2) and (numero1 > numero3) and (numero1 > numero4):
    print(f"Numero 1 -> {numero1}  é maior")
elif (numero2 > numero1) and (numero2 > numero3) and (numero2 > numero4):
    print(f"Numero 2 -> {numero2}  é maior")
elif (numero3 > numero1) and (numero3 > numero2) and (numero3 > numero4):
    print(f"Numero 3 -> {numero3}  é maior")
else:
    print(f"Numero 4 -> {numero4}  é maior")
'''
# Tabela com 100 numeros 


tabela_numeros = []
numero_de_numeros =100000

for i in range(numero_de_numeros):
    tabela_numeros.append(random.randint(0, numero_de_numeros)) #adiciona 100 numeros  de 0 a 99   
    #print(f"Valor tabela numeros {tabela_numeros}")

# temos de ver o tamanho da tabela
maior_numero = 0
numero_de_numeros =100000
for i in range(numero_de_numeros):
    if tabela_numeros[i] >= maior_numero:
        maior_numero = tabela_numeros[i]
        print(f"Maior numero na pos {i} tabela é {maior_numero}")
print(f"O maior numero  é {maior_numero}")
#print(f"{tabela_numeros}")

