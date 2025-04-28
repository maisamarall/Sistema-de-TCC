#funções
orientadores = {}
alunos = []

def cadastrar_orientador(orientadores):
    orientador = input("Informe o nome do orientador do trabalho: ")
    aluno = input("Informe o nome do aluno a ser orientado no trabalho: ")

    if orientador in orientadores:
        orientadores[orientador].append(aluno)
    else:
        orientadores[orientador] = [aluno]

    return orientadores

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

   #registrar versões
def registrar_entregas(alunos):
    matricula_aluno = input("Informe o num da matrícula do aluno: ")
    aluno_encontrado = None
    for aluno in alunos:
        if aluno["matricula"] == matricula_aluno:
            aluno_encontrado = aluno
            break

    if not aluno_encontrado:
        print(f"Aluno com matrícula {matricula_aluno} não encontrado.")
        return alunos

    if aluno_encontrado["entregas"] and aluno_encontrado["entregas"][-1][2] is None:
        print("Não é possível registrar nova entrega. A versão anterior ainda não foi avaliada.")
        return alunos

    num_versao = len(aluno_encontrado["entregas"]) + 1
    data_entrega = input("Informe a data da entrega (formato YYYY-MM-DD): ")
    nova_entrega = (f"v{num_versao}", data_entrega, None)
    aluno_encontrado["entregas"].append(nova_entrega)
    print(f"Versão v{num_versao} registrada com sucesso para o aluno {aluno_encontrado['nome']} em {data_entrega}.")
    return alunos

orientadores = {}
alunos = []

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
        cadastrar_orientador(orientadores)
    elif opcao == "2":
        print("Cadastrar alunos.\n")
        aluno = cadastrar_aluno()
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
            
            if str (opcao_funcionalidades).lower() == "q": #corrigindo.. Comparar com a entrada do menu inicial
                print("Encerrando o programa...\n")
                break
            elif opcao_funcionalidades == 1:
                print("Registrar nova entrega.")
                alunos = registrar_entregas(alunos)
            elif opcao_funcionalidades == 2:
                print("Registrar nota.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 3:
                print("Listar alunos por orientador.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 4:
                print("Listar versões entregues por aluno.")
                # colocar a funcao aqui
            elif opcao_funcionalidades == 5:
                print("Listar pendências de avaliação.")
                # colocar a funcao aqui
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

