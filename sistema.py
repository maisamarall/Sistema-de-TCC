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
    print("\n------------------------------------------\nAlunos por orientador:")
    
    while True:
        nomeOrientador = input("Digite o nome do Orientador: ")
        encontrado = False

        for orientador, lista_alunos in orientadores.items():
            if orientador.lower() == nomeOrientador.lower():
                print(f"orientador: {orientador}")
                for aluno in lista_alunos:
                    print(f" - {aluno}")
                encontrado = True
                break
            
        if not encontrado:
            print(f"Aluno {nomeOrientador} não encontrado.\n")
            
        resposta = str(input("\nDeseja continuar? (S/N)"))
        if resposta.upper() != "S":
            break

def listar_entregas_por_aluno(alunos):
    print("\n------------------------------------------\nVersões entregues por aluno:")

    while True:
        nomeAluno = input("Digite o nome do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno["nome"].lower() == nomeAluno.lower():
                print(f"\nAluno: {aluno['nome']}")
                for entrega in aluno['entregas']:
                    versao, data, _ = entrega
                    print(f" - Versão: {versao}\n - Data de entrega: {data}")
                encontrado = True
                break
        if not encontrado:
            print(f"Aluno {nomeAluno} não encontrado.\n")
        
        resposta = str(input("\nDeseja continuar? (S/N)"))
        if resposta.upper() != "S":
            break

def listar_pendencias_avaliacao(alunos):
    print("\n------------------------------------------\nAlunos com entregas não avaliadas:")

    while True:
        nomeAluno = input("Digite o nome do aluno: ")
        encontrado = False
        pendente = False

        for aluno in alunos:
            if aluno["nome"].lower() == nomeAluno.lower():
                encontrado = True
                for entrega in aluno['entregas']:
                    _, _, nota = entrega
                    if nota is None:
                        pendente = True
                        break

                if pendente:
                    print(f" - {aluno['nome']} possui entregas pendentes.")
                else:
                    print(f" - {aluno['nome']} não possui entregas pendentes.")
                break 

        if not encontrado:
            print(f"Aluno {nomeAluno} não encontrado.\n")

        resposta = str(input("\nDeseja continuar? (S/N)"))
        if resposta.upper() != "S":
            break


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

# Registrar nota
def registrar_nota(alunos):
    while True:
        print("--------------------------------------------------")
        nome_aluno = input("Nome do aluno: ")
        versao = input("Número da versão do TCC: ")
        nota = float(input("Nota a ser atribuída (0 a 10): "))

        aluno_encontrado = None
        for aluno in alunos:
            if aluno["nome"].lower() == nome_aluno.lower():
                aluno_encontrado = aluno
                break

        if aluno_encontrado:
            encontrou_versao = False
            for i, (versao_num, data, nota_atual) in enumerate(aluno_encontrado["entregas"]):
                if versao_num.lower() == versao.lower():
                    aluno_encontrado["entregas"][i] = (versao_num, data, nota)
                    encontrou_versao = True
                    print(f"\nNota atribuída com sucesso á versão {versao} de {nome_aluno}.\n")
                    print(aluno_encontrado["entregas"])
                    break

            if not encontrou_versao:
              print(f"Versão {versao} não encontrada para o aluno {nome_aluno}.\n")
        else:
            print(f"Aluno {nome_aluno} não encontrado.\n")

        print("--------------------------------------------------")
        continuar = input("Deseja continuar atribuindo nota? (S/N): ").upper()
        if continuar != "S":
            print("--------------------------------------------------")
            print("Saindo do sistema de atribuição de notas.")
            print("--------------------------------------------------")
            break

def relatorio_orientador(alunos):
  while True:
    print("--------------------------------------------------")
    nome_orientador = input("Nome do orientador: ")
    opcao_funcionalidade = int(input("""\n
--------------------------------------------------
Escolha uma das funcionalidades:

1 - Média das notas por aluno.
2 - Média geral.
    
--------------------------------------------------
"""))

    orientador_encontrado = False
    for aluno in alunos:
      if aluno["orientador"].lower() == nome_orientador.lower():
        orientador_encontrado = True
        break

    if orientador_encontrado:
      if opcao_funcionalidade == 1:
        print("Média das notas por aluno\n")
        
        for aluno in alunos:
          if aluno["orientador"].lower() == nome_orientador.lower():
            entregas = aluno["entregas"]
            notas_validas = [nota for versao, data, nota in entregas if nota is not None]
            
            if notas_validas:
              media = sum(notas_validas) / len(notas_validas)
              print(f"Aluno: {aluno['nome']} - Média das notas: {media:.2f}")
            
            else:
              print(f"Aluno: {aluno['nome']} - Nenhuma nota avaliada.")

      elif opcao_funcionalidade == 2:
        print("Média geral.\n")
        todas_notas = []
        for aluno in alunos:
          if aluno["orientador"].lower() == nome_orientador.lower():
              entregas = aluno["entregas"]
              notas_validas = [nota for versao, data, nota in entregas if nota is not None]

              if notas_validas:
                  todas_notas.append(notas_validas[-1])

        if todas_notas:
          media_geral = sum(todas_notas) / len(todas_notas)  
          print(f"Média geral dos alunos orientados por {nome_orientador}: {media_geral:.2f}")

        else:
          print("Nenhuma nota encontrada")        

      else:
        print("\nFuncionalidade inválida.")

    else:
      print(f"\nOrientador {nome_orientador} não encontrado.\n")

    print("-----------------------------------------------")
    continuar = input("\nDeseja continuar o processo? (S/N): ").upper()
    if continuar != "S":
        print("--------------------------------------------------")
        print("Saindo do sistema de relatório do orientador.")
        print("--------------------------------------------------")

        break


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
            opcao_funcionalidades = input("""\n
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
""")
            
            if str (opcao_funcionalidades).lower() == "q":
                print("Encerrando o programa...\n")
                break
            elif opcao_funcionalidades == "1":
                print("Registrar nova entrega.")
                alunos = registrar_entregas(alunos)
            elif opcao_funcionalidades == "2":
                print("Registrar nota.")
                registrar_nota(alunos)
            elif opcao_funcionalidades == "3":
                print("Listar alunos por orientador.")
                listar_aluno_por_orientador(orientadores)
            elif opcao_funcionalidades == "4":
                print("Listar versões entregues por aluno.")
                listar_entregas_por_aluno(alunos)
            elif opcao_funcionalidades == "5":
                print("Listar pendências de avaliação.")
                listar_pendencias_avaliacao(alunos)
            elif opcao_funcionalidades == "6":
                print("Gerar relatório do orientador.")
                relatorio_orientador(alunos)
            elif opcao_funcionalidades == "7":
                print("Voltar ao menu principal.")
                break
            else: 
                print("Digite uma opção válida...")

        else:
            print("Digite uma opção válida\n")

