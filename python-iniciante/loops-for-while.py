"""
Estruturas de repetição

LOOP FOR em Python:

for item in interavel:
    //execução do loop

Loops são utilizados para iterar sobre sequência ou valores iteráveis

Exemplos:

- String
    nome = 'João Gilberto'
- Lista
    lista = [1, 2, 3, 4, 5]
- Range
    range(1, 10)

OBS: No range, o valor final é apenas uma referência, ele não é incluído na "impressão".

Enumerate - Sequencia cada valor da variável em uma túpla especificanto seus índices.
Exemplo:
nome = 'João'

for variavel in enumerate(nome):
    print(variavel)

OBS: Quando não precisamos de um valor, descartamos o mesmo utilizando um underline ( _ ).

nome = 'João Gilberto'
for letra in nome:
    print(letra, end='')

OBS: a terminação END='' no print faz a impressão da variável ser horizontal.

"""

nome = 'Olá mundo!'

for i in nome:
    print(i, end='')

"""
Criação de um range

range(start, stop, step)

- start padrão é 0
- stop precisa ser definido
- step padrão é 1

"""
# A função list(), cria a lista definida no range
# O valor stop é a refência de índice, logo, começando de 0 irá até 9

numeros = list(range(0, 11))
# Imprime valores de 0 a 10
pares = list(range(0, 11, 2))
# Imprime valores pares de 0 a 10
impar = list(range(1, 11, 2))
# Imprime valores ímpares de 0 a 10
invertidos = list(range(10, -1, -1))
# Imprime valores de 10 a 0

print(numeros)
print(pares)
print(impar)
print(invertidos)

"""
LOOP WHILE em Python:

while expressão_booleana:
    //execução do loop

- O bloco do while será repetido enquanto a expressão booleana for verdadeira
- No while, o valor padrão da expressão é verdadeira
- Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso

exemplos:

while numero < 10:
    print(numero)
    numero = numero + 1  // Em um loop while é importante que se trate o critério de parada

resposta = ''
while resposta not in ['SIM', Sim', 'sim', 'S', 's']:
    resposta = input(f'Já acabou Jéssica? ')

Obs: Em Python não existe a expressão DO WHILE.

"""
numero = 0
while numero < 10:
    print(numero)
    numero += 1
