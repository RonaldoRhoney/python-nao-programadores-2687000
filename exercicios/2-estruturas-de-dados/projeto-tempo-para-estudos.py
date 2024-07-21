# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Qual é o seu nome? ')
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dia = input('Quantos dias  semais você estuda? ')
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Quantas horas por dia vocês estuda ? ')
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual o curso de programação você está estudndo? ')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_dia = int(total_dia)
total_horas = int(total_horas)
print(f'Olá {nome} você estuda {total_dia} por semana e {total_horas} horas por dia, então você estuda em média {total_dia * total_horas} semanais do nosso curso de {curso}, excelente !')
