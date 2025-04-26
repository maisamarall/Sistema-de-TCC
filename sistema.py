# Função cadastrar orientador

def cadastrar_orientador(orientadores):
    orientador = input("Informe o nome do orientador do trabalho: ")
    aluno = input("Informe o nome do aluno a ser orientado no trabalho: ")

    if orientador in orientadores:
        orientadores[orientador].append(aluno)
    else:
        orientadores[orientador] = [aluno]

    return orientadores

# Função cadastrar aluno
def cadastrar_aluno():
    nome = input("Informe o nome do aluno: ")
    matricula = input("Informe o número da matrícula: ")
    orientador = input("Informe o nome do orientador: ")

    entregas = []
    while True:
        versao = input("Informe a versão da entrega (ex: v1, v2): ")
        data_entrega = input("Informe a data da entrega (formato YYYY-MM-DD): ")
        nota_input = input("Informe a nota (ou pressione Enter se ainda não foi avaliado): ")

        nota = float(nota_input) if nota_input else None
        entregas.append((versao, data_entrega, nota))

        mais_entregas = input("Deseja adicionar outra entrega? (s/n): ")
        if mais_entregas.lower() != 's':
            break

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": entregas
    }

    return aluno

# Dicionarios
orientadores = {}
alunos = []

# Cadastrar orientadores
print("\nCadastro de orientadores")
while True:
    cadastrar_orientador(orientadores)

    continuar = input("Deseja cadastrar outro orientador? (s/n): ")
    if continuar.lower() != 's':
        break

# Parte 2: Cadastrar alunos
print("\nCadastro de alunos")
while True:
    aluno = cadastrar_aluno()
    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar resultados
print("\nOrientadores e seus alunos:")
for orientador, lista_alunos in orientadores.items():
    print({'nome': orientador, 'alunos': lista_alunos})

print("\nAlunos cadastrados:")
for aluno in alunos:
    print(aluno)
