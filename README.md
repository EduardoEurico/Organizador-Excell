# Documentação do Projeto

## Visão Geral

Este projeto é uma aplicação em Python que permite a manipulação de arquivos Excel e CSV para realizar diversas operações, como:

- Conversão de extratos.
- Soma de gastos por intervalo de linhas.
- Soma de gastos por histórico.
- Criação de planilhas filtradas por mês.

## Estrutura do Projeto

### Diretórios e Arquivos

```
app/
   ├── __pycache__/
   ├── addGrafico.py
   ├── converterEmPlanilha.py
   ├── gastos_por_historico.xlsx
   ├── main.py
   ├── organizar.py
   ├── somarColunas.py
```

### Descrição dos Arquivos

#### `main.py`

Arquivo principal que contém o menu da aplicação. Ele permite ao usuário escolher entre diferentes operações.

**Funções principais:**

- `menu()`: Exibe o menu principal e chama as funções apropriadas com base na escolha do usuário.

#### `converterEmPlanilha.py`

Arquivo responsável pela conversão de arquivos CSV para planilhas Excel.

**Funções principais:**

- `selecionar_arquivo_csv()`: Abre uma janela para o usuário selecionar um arquivo CSV.
- `converter_para_excel()`: Converte o arquivo CSV selecionado em uma planilha Excel.

#### `somarColunas.py`

Arquivo responsável por somar gastos em arquivos Excel.

**Funções principais:**

- `selecionar_arquivo()`: Abre uma janela para o usuário selecionar um arquivo Excel.
- `somar_gastos_por_intervalo(caminho_excel: str, linha_inicio: int, linha_fim: int)`: Soma os gastos em um intervalo de linhas especificado.
- `somar_gastos_por_historico(caminho_excel: str, max_linhas: int = 1)`: Soma os gastos agrupados por histórico e cria um arquivo Excel com os resultados.

#### `organizar.py`

Arquivo que permite criar planilhas filtradas por mês e ano.

**Funções principais:**

- `selecionar_arquivo()`: Abre uma janela para o usuário selecionar um arquivo Excel.
- `criar_planilha_por_mes(caminho_excel: str)`: Cria uma planilha filtrada por mês e ano especificados pelo usuário.

#### `addGrafico.py`

Arquivo atualmente vazio, reservado para futuras implementações de funcionalidades relacionadas a gráficos.

---

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python e as bibliotecas necessárias instaladas:

- `pandas`
- `matplotlib`
- `tkinter`
- `xlsxwriter`

### Passos para execução

1. Navegue até o diretório `app`:
   ```bash
   cd app
   ```
2. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

---

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- [pandas](https://pandas.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)

---
