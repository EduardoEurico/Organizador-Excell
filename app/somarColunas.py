import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

def selecionar_arquivo():
    root = Tk()
    root.withdraw()  
    root.attributes('-topmost', True)  
    arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    root.destroy()  
    return arquivo 



"""Soma os gastos no intervalo de linhas especificado."""
def somar_gastos_por_intervalo(caminho_excel: str, linha_inicio: int, linha_fim: int):
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


"""Soma os gastos agrupados por 'Histórico' e cria um arquivo Excel com os resultados, limitando o número de linhas das colunas 'Histórico{historico}'."""
def somar_gastos_por_historico(caminho_excel: str, max_linhas: int = 1):
    try:
        df = pd.read_excel(caminho_excel)

        if "Valor" not in df.columns or "Histórico" not in df.columns:
            raise ValueError("A planilha deve conter as colunas 'Valor' e 'Histórico'.")

        df_gastos = df[df["Valor"] < 0]
        df_receitas = df[df["Valor"] > 0]

        colunas_novas = {}
        
        for historico in df["Histórico"].unique():
            valores_historico = df[df["Histórico"] == historico]["Valor"].sum()
            colunas_novas[f"Histórico{historico}"] = valores_historico

        for coluna, valor in colunas_novas.items():
            df[coluna] = valor

        for coluna in colunas_novas.keys():
            if coluna in df.columns:
                df[coluna] = df[coluna].head(max_linhas)

        soma_receitas = df_receitas["Valor"].sum()
        soma_gastos = df_gastos["Valor"].sum()

        nome_arquivo_saida = os.path.join(os.path.expanduser("~"), "Extratos", "gastos_por_historico_com_tipos.xlsx")

        with pd.ExcelWriter(nome_arquivo_saida, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Original', index=False)

            df_soma_receitas = pd.DataFrame({'Total Receitas': [soma_receitas]})
            df_soma_receitas.to_excel(writer, sheet_name='Soma Geral Receitas', index=False)

            df_soma_gastos = pd.DataFrame({'Total Gastos': [soma_gastos]})
            df_soma_gastos.to_excel(writer, sheet_name='Soma Geral Gastos', index=False)

        print("\nResumo por Histórico com colunas 'Histórico{historico}' limitadas:")
        print(df)
        print(f"\nSoma Geral das Receitas: R$ {soma_receitas:.2f}")
        print(f"Soma Geral dos Gastos: R$ {soma_gastos:.2f}")
        print(f"\nArquivo Excel gerado: {nome_arquivo_saida}")

        return df, soma_receitas, soma_gastos

    except Exception as e:
        print(f"Erro ao calcular soma por histórico: {e}")

