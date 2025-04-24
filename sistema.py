# Cadastrar orientadores

orientadores = {}

def cadastrar_orientador(orientadores):
    orientador = input("Informe o nome do orientador do trabalho: ")
    aluno = input("Informe o nome do aluno a ser orientado no trabalho: ")

    if orientador in orientadores:
        orientadores[orientador].append(aluno)
    else:
        orientadores[orientador] = [aluno]

    return orientadores

# Loop para cadastrar vários orientadores e alunos
while True:
    cadastrar_orientador(orientadores)

    continuar = input("Deseja cadastrar outro orientador/aluno? (s/n): ")
    if continuar.lower() != 's':
        break

# Exibe o resultado final
print("\nOrientadores e seus alunos:")
for orientador, alunos in orientadores.items():
    print(f"{orientador}: {alunos}")