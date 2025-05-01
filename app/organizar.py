import pandas as pd
from tkinter import Tk
import os
from tkinter.filedialog import askopenfilename


"""Usa o Tkinter para abrir uma janela e o usuário selecionar um arquivo Excel."""
def selecionar_arquivo():
    root = Tk()
    root.withdraw()  
    root.attributes('-topmost', True)  
    arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    root.destroy()  
    return arquivo 


"""Cria uma planilha filtrada por mês e ano especificados pelo usuário."""
def criar_planilha_por_mes(caminho_excel: str):
    try:
        df = pd.read_excel(caminho_excel)

        if "Data Lançamento" not in df.columns or "Valor" not in df.columns:
            raise ValueError("A planilha deve conter as colunas 'Data Lançamento' e 'Valor'.")

        mes = int(input("Digite o mês desejado (1 a 12): "))
        ano = int(input("Digite o ano desejado (ex: 2024): "))

        df["Data Lançamento"] = pd.to_datetime(df["Data Lançamento"], errors='coerce')

        df_filtrado = df[(df["Data Lançamento"].dt.month == mes) & (df["Data Lançamento"].dt.year == ano)]

        if df_filtrado.empty:
            print(f"Nenhum dado encontrado para {mes}/{ano}.")
            return

        pasta_saida = os.path.join(os.path.expanduser("~"), "Extratos")
        os.makedirs(pasta_saida, exist_ok=True)  
        nome_arquivo_saida = os.path.join(pasta_saida, f"extrato_filtrado_{mes:02d}_{ano}.xlsx")

        df_filtrado.to_excel(nome_arquivo_saida, index=False)

        print(f"Planilha filtrada criada com sucesso: {nome_arquivo_saida}")

        return df_filtrado

    except Exception as e:
        print(f"Erro ao criar planilha por mês: {e}")