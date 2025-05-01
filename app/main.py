import converterEmPlanilha
import somarColunas
import organizar

"""Esse programa tem como objetivo converter extratos bancários em planilhas do Excel, 
somar gastos por intervalo de linhas e por histórico, 
e criar planilhas mensais a partir dos dados extraídos."""

def opcao_1():
    converterEmPlanilha.converter_para_excel()
    print("Planilha criada com sucesso!")

def opcao_2():
    arquivo = somarColunas.selecionar_arquivo()
    if arquivo:
        linha_inicio = int(input("Digite a linha inicial (começa em 0): "))
        linha_fim = int(input("Digite a linha final: "))
        somarColunas.somar_gastos_por_intervalo(arquivo, linha_inicio, linha_fim)
    else:
        print("Nenhum arquivo selecionado.")

def opcao_3():
    arquivo = somarColunas.selecionar_arquivo()
    if arquivo:
        somarColunas.somar_gastos_por_historico(arquivo)
    else:
        print("Nenhum arquivo selecionado.")

def opcao_4():
    arquivo = organizar.selecionar_arquivo()
    if arquivo:
        organizar.criar_planilha_por_mes(arquivo)
    else:
        print("Nenhum arquivo selecionado.")

def opcao_5():
    print("Saindo do programa. Até mais!")
    return False  

def menu():
    while True:
        print("Todas as pastas criadas são salvas na pasta 'Extratos' na pasta do usuário.")
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Converter extrato para planilha")
        print("2 - Somar gastos por intervalo de linhas")
        print("3 - Somar gastos por histórico")
        print("4 - Criar planilha por mês")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        opcoes = {
            "1": opcao_1,
            "2": opcao_2,
            "3": opcao_3,
            "4": opcao_4,
            "5": opcao_5,
        }

        funcao = opcoes.get(escolha)
        if funcao:
            if escolha == "5":
                if not funcao():
                    break
            else:
                funcao()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
