import pandas as pd
from tkinter import Tk, filedialog
import os
from tkinter import Tk, filedialog

def selecionar_arquivo_csv():
    root = Tk()
    root.withdraw()  
    root.attributes('-topmost', True) 

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=(("CSV files", "*.csv"), ("Todos os arquivos", "*.*"))
    )
    
    root.destroy()  
    return caminho_arquivo


def converter_para_excel():
    try:
        caminho_arquivo = selecionar_arquivo_csv()

        if not caminho_arquivo:
            print("Nenhum arquivo foi selecionado.")
            return

        df = pd.read_csv(caminho_arquivo, delimiter=";", skiprows=4, on_bad_lines='skip')
        print(f"Colunas encontradas no arquivo CSV: {df.columns.tolist()}")

        for coluna in df.columns:
            try:
                df[coluna] = df[coluna].astype(str).str.replace(',', '.', regex=False)
                df[coluna] = pd.to_numeric(df[coluna])
            except ValueError:
                print(f"Coluna '{coluna}' não é numérica e será mantida como está.")

        caminho_saida = os.path.join(
            os.path.expanduser("~"), 
            "Extratos", 
            os.path.basename(os.path.splitext(caminho_arquivo)[0]) + "_extrato_formatado.xlsx"
        )
        os.makedirs(os.path.dirname(caminho_saida), exist_ok=True)

        df.to_excel(caminho_saida, index=False, sheet_name="Extrato")

        print(f"Planilha criada com sucesso em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao converter arquivo: {e}")