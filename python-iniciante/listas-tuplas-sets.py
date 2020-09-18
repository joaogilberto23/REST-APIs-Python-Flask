"""
LISTAS
"""

# Funções da lista

notas = [3, 5, 6, 4, 8]

notas.append(10)  # Adiciona um valor a lista

print(notas)

media = sum(notas) / len(notas)

print(media)

inicial = notas[0]  # Acessa o índice inicial da lista | OBS: Em python a lista começa na posição 0

print(inicial)

final = notas[len(notas) - 1]  # Acessa o último índice | Tamanho da lista menos uma posição

print(final)

"""
TUPLAS 

- Indicadas com parenteses
- Tuplas, em tese, não podem ser modificadas; o que pode ser feito é ela ser recriada
"""

tupla = (3, 5, 6, 4, 8)

tupla += (10,)
# Para refazer a tupla com um novo valor, colocase o valor como primeiro parâmetro
# e o segundo fica em branco, seria o mesmo que: tupla = tupla + (valor)

print(tupla)

"""
SETs

- Indicado entre chaves
- Um Set não pode ter valores repetidos
- Também não é possível acessar índices no Set
"""

set_notas = {3, 5, 6, 4, 8}

set_notas.add(10)  # Função que pode adicionar um valor
print(set_notas)
set_notas.add(10)  # Mas se for outro igual, ele não será adicionado como na lista
print(set_notas)