from datetime import datetime

#funções
orientadores = {}
alunos = []

def cadastrar_orientador(orientadores, alunos):
    orientador = input("Informe o nome do orientador do trabalho: ")

    if orientador not in orientadores:
        orientadores[orientador] = []

    aluno = input("Informe o nome do aluno a ser orientado no trabalho: ")

    for estudante in alunos:
        if estudante['nome'].lower() == aluno.lower():
            print("Este aluno já foi cadastrado anteriormente...")
            return orientadores
        
    orientadores[orientador].append(aluno)

    # if orientador in orientadores:
    #     orientadores[orientador].append(aluno)
    # else:
    #     orientadores[orientador] = [aluno]

    return orientadores

def cadastrar_aluno(orientadores):
    nome = input("Informe o nome do aluno: ")
    matricula = input("Informe o número da matrícula: ")
    orientador = input("Informe o nome do orientador: ")

    if orientador not in orientadores:
        print("Orientador não encontrado. Cadastre o orientador primeiro.")
        return None

    entregas = []

    while True:
        versao = input("Informe a versão da entrega (ex: v1, v2): ")

        while True:
            data_entrega = input("Informe a data da entrega (formato YYYY-MM-DD): ")
            try:
                datetime.strptime(data_entrega, "%Y-%m-%d")
                break
            except ValueError:
                print("Data inválida. Use o formato YYYY-MM-DD")
                
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

def listar_aluno_por_orientador(orientadores):
    print("\nAlunos por orientador:")
    for orientador, lista_alunos in orientadores.items():
        print(f"orientador: {orientador}")
        for aluno in lista_alunos:
            print(f" - {aluno}")

def listar_entregas_por_aluno(alunos):
    print("\nVersões entregues por aluno:")
    for aluno in alunos:
        print(f"\nAluno: {aluno['nome']}")
        for entrega in aluno['entregas']:
            versao, data, _ = entrega
            print(f" - Versão: {versao}, Data de entrega: {data}")

def listar_pendencias_avaliacao(alunos):
    print("\nAlunos com entregas não avaliadas:")
    for aluno in alunos:
        pendente = False
        for entrega in aluno['entregas']:
            _, _, nota = entrega
            if nota is None:
                pendente = True
                break
        if pendente:
            print(f" - {aluno['nome']}")

#Menu
while True:
    opcao = input("""
---------------------------------------------------------
Escolha uma opção ou digite 'q' para encerrar o programa:

1 - Cadastrar orientadores.
2 - Cadastrar alunos.
3 - Realizar operações.
---------------------------------------------------------

""")
    if opcao.lower() == "q":
        print("Encerrando o programa...\n")
        break

    elif opcao == "1":
        print("Cadastrar orientadores.\n")
        cadastrar_orientador(orientadores, alunos)
    elif opcao == "2":
        print("Cadastrar alunos.\n")
        aluno = cadastrar_aluno(orientadores)
        if aluno:
            alunos.append(aluno)
    elif opcao == "3":
        print("Realizar operações")
        while True: 
            opcao_funcionalidades = int(input("""\n
------------------------------------------
Escolha uma funcionalidade:

1 - Registrar nova entrega.
2 - Registrar nota.
3 - Listar alunos por orientador.
4 - Listar versões entregues por aluno.
5 - Listar pendências de avaliação.
6 - Gerar relatório do orientador.
7 - Voltar ao menu principal.
------------------------------------------
"""))
            
            if opcao_funcionalidades.lower() == "q":
                print("Encerrando o programa...\n")
                break
            elif opcao_funcionalidades == 1:
                print("Registrar nova entrega.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 2:
                print("Registrar nota.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 3:
                print("Listar alunos por orientador.")
                listar_aluno_por_orientador(orientadores)
            elif opcao_funcionalidades == 4:
                print("Listar versões entregues por aluno.")
                listar_entregas_por_aluno(alunos)
            elif opcao_funcionalidades == 5:
                print("Listar pendências de avaliação.")
                listar_pendencias_avaliacao(alunos)
            elif opcao_funcionalidades == 6:
                print("Gerar relatório do orientador.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 7:
                print("Voltar ao menu principal.")
                break
            else: 
                print("Digite uma opção válida...")

    else:
        print("Digite uma opção válida\n")


