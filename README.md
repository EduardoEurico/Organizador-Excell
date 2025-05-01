
# 💰 Extrato Financeiro - Analisador e Organizador de Gastos

Este projeto é uma ferramenta interativa em Python para auxiliar na organização, análise e filtragem de extratos bancários, transformando arquivos CSV em planilhas Excel formatadas e permitindo a extração de informações úteis como somatórios por intervalo, por tipo de gasto e por mês.

## 🧩 Funcionalidades

- Converter extratos CSV em planilhas Excel formatadas
- Somar gastos dentro de um intervalo de linhas
- Agrupar e somar gastos por tipo de "Histórico"
- Filtrar e gerar planilhas por mês/ano específico
- Interface simples por terminal

## 📁 Estrutura do Projeto

```
.
├── main.py                      # Menu principal para interação com o usuário
├── converterEmPlanilha.py      # Converte CSV bancário para Excel formatado
├── somarColunas.py             # Funções para somar valores por intervalo ou histórico
├── organizar.py                # Gera planilhas filtradas por mês
├── gastos_por_historico.xlsx   # Exemplo de planilha Excel (usado para testes)
```

## ⚙️ Requisitos

- Python 3.8 ou superior

### Bibliotecas:

```bash
pip install pandas openpyxl xlsxwriter
```

**Obs:** O script usa Tkinter para seleção de arquivos com janelas gráficas. No Linux, você pode precisar instalar com:

```bash
sudo apt install python3-tk
```

## 🚀 Como Executar

1. Clone este repositório ou baixe os arquivos:

```bash
git clone https://github.com/seu-usuario/extrato-analisador.git
cd extrato-analisador
```

2. Instale as dependências (veja acima).

3. Execute o programa principal:

```bash
python main.py
```

4. Use o menu para selecionar a funcionalidade desejada:

```
===== MENU PRINCIPAL =====
1 - Converter extrato para planilha
2 - Somar gastos por intervalo de linhas
3 - Somar gastos por histórico
4 - Criar planilha por mês
5 - Sair
```

## 📌 Descrição dos Arquivos

- **main.py**: Menu principal que conecta todas as funcionalidades.
- **converterEmPlanilha.py**: Lê um CSV bancário e transforma em Excel formatado, corrigindo números com vírgula.
- **somarColunas.py**:
  - `somar_gastos_por_intervalo`: Soma valores negativos (gastos) entre duas linhas da planilha.
  - `somar_gastos_por_historico`: Agrupa os gastos por "Histórico" e cria novas colunas com a soma.
- **organizar.py**: Permite filtrar a planilha por mês e ano, criando um novo arquivo Excel com os dados filtrados.
- **gastos_por_historico.xlsx**: Exemplo de planilha que pode ser usada para testar os módulos `somarColunas` e `organizar`.

## 🗂 Saída dos Arquivos

Todos os arquivos gerados (planilhas Excel) são salvos automaticamente na pasta:

```bash
~/Extratos/
```

## 🧠 Observações

- As planilhas precisam conter as colunas obrigatórias: "Valor", "Histórico" e "Data Lançamento" dependendo da funcionalidade usada.
- A interface gráfica para seleção de arquivos exige que o Python tenha suporte a Tkinter.
