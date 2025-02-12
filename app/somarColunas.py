import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

def selecionar_arquivo():
    """Usa o Tkinter para abrir uma janela e o usuário selecionar um arquivo Excel."""
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])  # Filtro para arquivos Excel
    return arquivo

def somar_gastos_por_intervalo(caminho_excel: str, linha_inicio: int, linha_fim: int):
    """Soma os gastos no intervalo de linhas especificado."""
    try:
        df = pd.read_excel(caminho_excel)

        if "Valor" not in df.columns:
            raise ValueError("A planilha deve conter uma coluna chamada 'Valor'.")

        df_intervalo = df.iloc[linha_inicio:linha_fim + 1]
        soma_gastos = df_intervalo[df_intervalo["Valor"] < 0]["Valor"].sum()

        print(f"Total dos gastos no intervalo ({linha_inicio} a {linha_fim}): R$ {soma_gastos:.2f}")
        return soma_gastos

    except Exception as e:
        print(f"Erro ao calcular soma dos gastos: {e}")

def somar_gastos_por_historico(caminho_excel: str, max_linhas: int = 1):
    """Soma os gastos agrupados por 'Histórico' e cria um arquivo Excel com os resultados, limitando o número de linhas das colunas 'Histórico{historico}'."""
    try:
        df = pd.read_excel(caminho_excel)

        if "Valor" not in df.columns or "Histórico" not in df.columns:
            raise ValueError("A planilha deve conter as colunas 'Valor' e 'Histórico'.")

        # Filtra os gastos (valores negativos) e receitas (valores positivos)
        df_gastos = df[df["Valor"] < 0]
        df_receitas = df[df["Valor"] > 0]

        # Cria um dicionário para armazenar as somas por histórico
        colunas_novas = {}
        
        # Para cada tipo único de "Histórico", cria uma nova coluna e soma os valores
        for historico in df["Histórico"].unique():
            # Filtra os dados de acordo com o tipo de histórico
            valores_historico = df[df["Histórico"] == historico]["Valor"].sum()
            # Cria a coluna correspondente e adiciona a soma dos valores
            colunas_novas[f"Histórico{historico}"] = valores_historico

        # Adiciona as novas colunas ao dataframe
        for coluna, valor in colunas_novas.items():
            df[coluna] = valor

        # Limitar o número de linhas nas colunas 'Histórico{historico}'
        for coluna in colunas_novas.keys():
            if coluna in df.columns:
                df[coluna] = df[coluna].head(max_linhas)

        # Soma geral dos valores positivos e negativos
        soma_receitas = df_receitas["Valor"].sum()
        soma_gastos = df_gastos["Valor"].sum()

        # Cria um ExcelWriter para salvar múltiplos DataFrames em diferentes planilhas
        nome_arquivo_saida = os.path.join(os.path.expanduser("~"), "Extratos", "gastos_por_historico_com_tipos.xlsx")

        with pd.ExcelWriter(nome_arquivo_saida, engine='xlsxwriter') as writer:
            # Clona o arquivo original com as colunas limitadas
            df.to_excel(writer, sheet_name='Original', index=False)

            # Adiciona a tabela com a soma geral das receitas
            df_soma_receitas = pd.DataFrame({'Total Receitas': [soma_receitas]})
            df_soma_receitas.to_excel(writer, sheet_name='Soma Geral Receitas', index=False)

            # Adiciona a tabela com a soma geral dos gastos
            df_soma_gastos = pd.DataFrame({'Total Gastos': [soma_gastos]})
            df_soma_gastos.to_excel(writer, sheet_name='Soma Geral Gastos', index=False)

        # Exibe o resumo
        print("\nResumo por Histórico com colunas 'Histórico{historico}' limitadas:")
        print(df)
        print(f"\nSoma Geral das Receitas: R$ {soma_receitas:.2f}")
        print(f"Soma Geral dos Gastos: R$ {soma_gastos:.2f}")
        print(f"\nArquivo Excel gerado: {nome_arquivo_saida}")

        return df, soma_receitas, soma_gastos

    except Exception as e:
        print(f"Erro ao calcular soma por histórico: {e}")

