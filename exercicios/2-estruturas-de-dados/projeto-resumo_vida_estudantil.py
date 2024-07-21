# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.
estudante = {}
estudante['nome'] = input('Qual o seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Quando você entrou no LinkedIn? '))
estudante['ano_atual'] = int(input('Qual o anos atual? '))
cursos = input('Quais os cursos você já fez aqji no LinkedIn? ')
estudante['cursos'] = cursos.split(', ')
# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']
total_cursos = len(estudante['cursos'])
print(f"Olá {estudante['nome']}, desde {estudante['ano_conheceu_linkedin']} você conhece o LinkdIn nesses {total_anos} anos, anos realizou {total_cursos} cursos, sendo o primeiro curso {estudante['cursos'][0]} e o ultimo curso {estudante['cursos'][-1]}.")
