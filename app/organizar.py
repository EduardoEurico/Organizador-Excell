import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

def selecionar_arquivo():
    """Usa o Tkinter para abrir uma janela e o usuário selecionar um arquivo Excel."""
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    arquivo = askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])  # Filtro para arquivos Excel
    return arquivo


def criar_planilha_por_mes(caminho_excel: str):
    """Cria uma planilha filtrada por mês e ano especificados pelo usuário."""
    try:
        # Lê a planilha original
        df = pd.read_excel(caminho_excel)

        if "Data Lançamento" not in df.columns or "Valor" not in df.columns:
            raise ValueError("A planilha deve conter as colunas 'Data Lançamento' e 'Valor'.")

        # Solicita o mês e o ano para o filtro
        mes = int(input("Digite o mês desejado (1 a 12): "))
        ano = int(input("Digite o ano desejado (ex: 2024): "))

        # Converte a coluna 'Data Lançamento' para datetime
        df["Data Lançamento"] = pd.to_datetime(df["Data Lançamento"], errors='coerce')

        # Filtra os dados para o mês e ano fornecidos
        df_filtrado = df[(df["Data Lançamento"].dt.month == mes) & (df["Data Lançamento"].dt.year == ano)]

        # Verifica se existem dados para o mês e ano selecionados
        if df_filtrado.empty:
            print(f"Nenhum dado encontrado para {mes}/{ano}.")
            return

        pasta_saida = os.path.join(os.path.expanduser("~"), "Extratos")
        os.makedirs(pasta_saida, exist_ok=True)  # Cria a pasta se não existir
        nome_arquivo_saida = os.path.join(pasta_saida, f"extrato_filtrado_{mes:02d}_{ano}.xlsx")

        # Salva o DataFrame filtrado em um novo arquivo Excel
        df_filtrado.to_excel(nome_arquivo_saida, index=False)

        print(f"Planilha filtrada criada com sucesso: {nome_arquivo_saida}")

        return df_filtrado

    except Exception as e:
        print(f"Erro ao criar planilha por mês: {e}")