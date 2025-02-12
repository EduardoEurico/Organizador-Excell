import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import os

def selecionar_arquivo_csv():
   
    root = Tk()
    root.withdraw()  

    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    return caminho_arquivo

def converter_para_excel():
    try:
        caminho_arquivo = selecionar_arquivo_csv()

        if not caminho_arquivo:
            print("Nenhum arquivo foi selecionado.")
            return

        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo, delimiter=";", skiprows=4, on_bad_lines='skip')
        print(f"Colunas encontradas no arquivo CSV: {df.columns.tolist()}")

        # Converte vírgulas para pontos em colunas numéricas
        for coluna in df.columns:
            try:
                # Substitui vírgulas por pontos e tenta converter a coluna para numérica
                df[coluna] = df[coluna].astype(str).str.replace(',', '.', regex=False)
                df[coluna] = pd.to_numeric(df[coluna])
            except ValueError:
                # Coluna não é numérica, ignorar erro
                print(f"Coluna '{coluna}' não é numérica e será mantida como está.")

        # Define o caminho de saída
        caminho_saida = os.path.join(
            os.path.expanduser("~"), 
            "Extratos", 
            os.path.basename(os.path.splitext(caminho_arquivo)[0]) + "_extrato_formatado.xlsx"
        )
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

        # Salva o DataFrame em um arquivo Excel
        df.to_excel(caminho_saida, index=False, sheet_name="Extrato")

        print(f"Planilha criada com sucesso em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao converter arquivo: {e}")