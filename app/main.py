import converterEmPlanilha
import somarColunas
import organizar

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

        if escolha == "1":
            converterEmPlanilha.converter_para_excel()
            print("Planilha criada com sucesso!")

        elif escolha == "2":
            arquivo = somarColunas.selecionar_arquivo()

            if arquivo:
                linha_inicio = int(input("Digite a linha inicial (começa em 0): "))
                linha_fim = int(input("Digite a linha final: "))
                somarColunas.somar_gastos_por_intervalo(arquivo, linha_inicio, linha_fim)
            else:
                print("Nenhum arquivo selecionado.")

        elif escolha == "3":
            arquivo = somarColunas.selecionar_arquivo()

            if arquivo:
                somarColunas.somar_gastos_por_historico(arquivo)
            else:
                print("Nenhum arquivo selecionado.")

        elif escolha == "4":
            arquivo = organizar.selecionar_arquivo()

            if arquivo:
                organizar.criar_planilha_por_mes(arquivo)
            else:
                print("Nenhum arquivo selecionado.")
        

        elif escolha == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
