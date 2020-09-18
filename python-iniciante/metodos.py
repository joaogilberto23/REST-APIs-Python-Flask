"""
Em Python, para se criar um  método basta usar a seguinte estrutura:

def meu_metodo():
    instrução

Para executar este método, basta chamá-lo.

meu_metodo()

OBS: lembrar de identar corretamente as instruções dentro do método
"""


def imprimir():
    print('Olá')


imprimir()


# método com parâmetros


def soma_valores(a, b):
    soma = a + b
    print(soma)


soma_valores(3, 5)

# Algumas funções Built-In - Embutidas

print() # Imprime algo
int() # Retorna um inteiro
float() # Retorna um decimal
len() # Retorna o tamanho de uma string
abs() # Retorna um módulo | Valor absoluto
sum() # Retorna uma soma de valores
min() # Retorna o valor mínimo
max() # Retorna o maior valor
round() # Arredonda um valor
round('valor', 'número de casas decimais') # Arredonda um valor com o número de casas decimais especificadas