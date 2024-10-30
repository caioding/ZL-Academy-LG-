"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/web/
"""

# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Add
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin

# Add Import for formulario.py
from produto_poo import Produto
# Add for path OS
import os

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Relative path for each OS
caminho_arquivo = os.path.join(os.path.dirname(__file__), "forms", "produto.html")

# Add Function for bot input forms
def preencher_formulario_produto(bot, produto):
    # bot.browse("file:///home/caio/dxzl-academy/bot_produto/forms/produto.html")
    # bot.browse(" file:///C:/Users/noturno/dxzl-academy/bot_produto/forms/produto.html")
    bot.browse("file://" + caminho_arquivo)
    bot.wait(3000)
    bot.find_element("nome", By.ID).send_keys(produto.nome)
    bot.find_element("preco", By.ID).send_keys(produto.preco)
    bot.find_element("quantidade", By.ID).send_keys(produto.quantidade)
    produto_button = bot.find_element("produto_button", By.ID)
    if produto_button:
        produto_button.click()
        print(f"Formulário de Produto preenchido com: Nome={produto.nome}, Preço={produto.preco}, Qauntidade={produto.quantidade}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source) 
# End funcionts for bot input forms

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    # bot.browser = Browser.FIREFOX

    ## Add
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path
    # bot.driver_path = "<path to your WebDriver binary>"

    # Add
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    # bot.browse("https://www.botcity.dev")

    # Implement here your logic...
    ...

    # Add Call function
    produto_form = Produto("Produto Teste", 100, 10)
    print("Informações do produto antes de atualizar:")
    produto_form.exibir()
    preencher_formulario_produto(bot, produto_form)
    bot.wait(3000)
    produto_form.atualizar("Produto Atualizado", 150, 20)
    print("Informações do produto após atualizar:")
    produto_form.exibir()
    preencher_formulario_produto(bot, produto_form)

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
