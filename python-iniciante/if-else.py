"""
Estruturas condicionais
if, else, elif

'elif' significa a junção de 'else if', do java, por exemplo

- Se usar o elif, sempre terminar com else
"""

idade = 17

if idade < 18:
    print('Menor de idade!')
elif idade == 18:
    print('Tem 18 anos!')
else:
    print('Maior de idade!')

""""""

pessoas_conhecidas = ['João', 'Maria', 'Pedro', 'Ana']

pessoa = input('Digite o nome de uma pessoa: ')

if pessoa in pessoas_conhecidas:
    print("Você conhece "+pessoa+".")
else:
    print("Você não conhecia "+pessoa+".")
    pessoas_conhecidas.append(pessoa)
    print(f"Lista atualizada: {pessoas_conhecidas}")
    print(f'Agora você conhece {pessoa}!')
