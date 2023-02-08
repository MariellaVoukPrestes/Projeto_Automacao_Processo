import pandas as pd
import pyautogui as pag
import pyperclip
import time


#abrindo o arquivo
df = pd.read_excel(r"C:/Users/desktop/Downloads/Intensivão de Python/Aula 1/Exportar/Vendas - Dez.xlsx")

#calculando os dados
faturamento = df["Valor Final"].sum()
qtd_produtos = df["Quantidade"].sum()

# ABRIR o gmail;
pag.PAUSE = 5
pag.press("winleft")
pag.write("chrome")
pag.press("enter")

# Clicar em ESCREVER( novo e-mail);
pyperclip.copy("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
pag.hotkey("ctrl", "v")
pag.press("enter")
time.sleep(30)

# Escrever o DESTINATÁRIO;
pag.write("test.dev.mari@gmail.com")
time.sleep(15)
pag.press("tab")
pag.press("tab")

# Selecionar o campo ASSUNTO;
assunto = "test"
pag.write(assunto)
time.sleep(5)

# Selecionar o campo CORPO DO E-MAIL e escrever o e-mail usando os indicadores calculados;
pag.press("tab")
pag.write(f"testando, o faturamento foi de R${faturamento:,.2f}\nE a quantidade foi de {qtd_produtos:,}")

# ENVIAR E-mail;
pag.hotkey("ctrl","enter")
