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

# Import for formulario.py
from formulario import FormularioContato, FormularioLogin, FormBase

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Functions for bot input forms
def preencher_formulario_base(bot, formulario):
    bot.browse("file:///home/caio/dxzl-academy/bot_test/forms/base.html")
    bot.wait(3000)
    bot.find_element("nome_input", By.ID).send_keys(formulario.nome)
    bot.find_element("sexo_input", By.ID).send_keys(formulario.sexo)
    bot.find_element("idade_input", By.ID).send_keys(formulario.idade)
    base_button = bot.find_element("base_button", By.ID)
    if base_button:
        base_button.click()
        print(f"Formulário Base preenchido com: Nome={formulario.nome}, Sexo={formulario.sexo}, Idade={formulario.idade}")

    else:
        print("Error: Could not find base_button element.")
        print(bot.page_source) 

def preencher_formulario_contato(bot, formulario):
    bot.browse("file:///home/caio/dxzl-academy/bot_test/forms/contato.html")
    bot.wait(3000)
    bot.find_element("email_input", By.ID).send_keys(formulario.email)
    bot.find_element("mensagem_input", By.ID).send_keys(formulario.mensagem)
    contato_button = bot.find_element("contato_button", By.ID)
    if contato_button:
        contato_button.click()
        print(f"Formulário de Contato preenchido com: Email={formulario.email}, Mensagem={formulario.mensagem}")
    else:
        print("Error: Could not find contato_button element.")
        print(bot.page_source)

def preencher_formulario_login(bot, formulario):
    bot.browse("file:///home/caio/dxzl-academy/bot_test/forms/login.html")
    bot.wait(3000)
    bot.find_element("usuario_input", By.ID).send_keys(formulario.usuario)
    bot.find_element("senha_input", By.ID).send_keys(formulario.senha)
    login_button = bot.find_element("login_button", By.ID)
    if login_button:
        login_button.click()
        print(f"Formulário de Login preenchido com: Usuário={formulario.usuario}, Senha={formulario.senha}")
    else:
        print("Error: Could not find login_button element.")
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

    base_form = FormBase("Caio", "M", 30)
    contato_form = FormularioContato("Caio", "M", 30, "caio@example.com", "Mensagem de teste")
    login_form = FormularioLogin("Caio", "M", 30, "caio_user", "senha123")
    preencher_formulario_base(bot, base_form)
    preencher_formulario_contato(bot, contato_form)
    preencher_formulario_login(bot, login_form)


    # Opens the BotCity website.
    # bot.browse("https://www.botcity.dev")

    # Implement here your logic...
    ...

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
