import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever um texto

# Definir um tempo de delay a cada acao
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 2 segundos para carregar a pagina
time.sleep(2)

# Passo 2: Fazer login
# Digitar o email
pyautogui.click(x=764, y=374)
pyautogui.write("murilo.braggio@gmail.com")
pyautogui.press("tab")

# Digitar a senha
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados

# Esperar 2 segundos para carregar a pagina
time.sleep(2)

# pandas - biblioteca para importacao de base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastramento de Produtos
for linha in tabela.index: # Para cada linha da tabela

    # Codigo
    pyautogui.click(x=765, y=259)
    codigo = tabela.loc[linha, "codigo"] # Localizar a linha na tabela
    pyautogui.write(codigo)

    # Marca
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    # Tipo
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    # Categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    # Preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    # Custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    # Observacao
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    # Enviar e voltar ao inicio da pagina
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# pyautogui -> fazer automacoes em python