# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Add
from webdriver_manager.chrome import ChromeDriverManager
from botcity.plugins.http import BotHttpPlugin

# For import packages
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Faker data
from faker import Faker

# Classes import
from classes.veiculo import Veiculo
from classes.carro import Carro
from classes.motocicleta import Motocicleta

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def instanciar_carro(nome: str, ano: int, diaria: float, combustivel: str):
    return Carro(nome, ano, diaria, combustivel)

def instanciar_moto(nome: str, ano: int, diaria: float, cilindrada: int):
    return Motocicleta(nome, ano, diaria, cilindrada)

def escrever_linha(nome_arquivo: str, linha: str):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha)

def extrari_dados(form_veiculo: dict):
    nome = form_veiculo['nome']
    ano = form_veiculo['ano']
    diaria = form_veiculo['diaria']

    if 'combustivel' in form_veiculo:
        combustivel = form_veiculo['combustivel']
        carro = instanciar_carro(nome, ano, diaria, combustivel)
        id = Veiculo.quant_veiculos
        linha = f'{id},{carro.nome},{carro.ano},{carro.diaria},{carro.__class__.__name__},{carro.combustivel},\n'
        print(linha)

    elif 'cilindrada' in form_veiculo:
        cilindrada = form_veiculo['cilindrada']
        moto = instanciar_moto(nome, ano, diaria, cilindrada)
        id = Veiculo.quant_veiculos
        linha = f'{id},{moto.nome},{moto.ano},{moto.diaria},{moto.__class__.__name__},,{moto.cilindrada}\n'
        print(linha)

    escrever_linha('veiculos.txt', linha)

def inventar_carros():
    fake = Faker()
    nome = f'{fake.word().capitalize()} {fake.word().capitalize()}'
    ano = fake.year()
    diaria = fake.random_number(digits=3)
    combustivel = fake.random_element(elements=('Gasolina', 'Etanol', 'Diesel', 'GNV', 'Elétrico'))
    
    return nome, ano, diaria, combustivel
    
def inventar_motos():
    fake = Faker()
    nome = f'{fake.word().capitalize()} {fake.word().capitalize()}'
    ano = fake.year()
    diaria = fake.random_number(digits=3)
    cilindrada = fake.random_element(elements=(100, 150, 200, 250))
    
    return nome, ano, diaria, cilindrada
    
def inserir_forms(bot:WebBot, carros: int, motos: int):
    for _ in range(carros):
        bot.browse('http://127.0.0.1:5000')
        bot.wait(500)
        alugar_carros = bot.find_element('/html/body/div/div/div[1]/div/div/div/button', By.XPATH) 
        alugar_carros.click()
        bot.wait(500)
        nome, ano, diaria, combustivel = inventar_carros()
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(nome)
        bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(ano)
        bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(diaria)
        bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(combustivel)
        btn_submit = bot.find_element('/html/body/div/div[1]/form/button', By.XPATH) 
        btn_submit.click()
        bot.wait(500)

    for _ in range(motos):
        bot.browse('http://127.0.0.1:5000')
        bot.wait(500)
        alugar_motos = bot.find_element('/html/body/div/div/div[2]/div/div/div/button', By.XPATH)
        alugar_motos.click()
        bot.wait(500)
        nome, ano, diaria, cilindrada = inventar_motos()
        bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(nome)
        bot.find_element('//*[@id="ano"]', By.XPATH).send_keys(ano)
        bot.find_element('//*[@id="diaria"]', By.XPATH).send_keys(diaria)
        bot.find_element('//*[@id="cilindrada"]', By.XPATH).send_keys(cilindrada)
        btn_submit = bot.find_element('/html/body/div/div[1]/form/button', By.XPATH)
        btn_submit.click()
        bot.wait(500)
        
    return

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
    try:
        print("Automação para aluguel de veículos!")
        carros = int(input('Quantos carros você deseja alugar? '))
        motos = int(input('Quantas motos você deseja alugar? '))
        inserir_forms(bot, carros, motos)
    
    except Exception as ex:
        print(ex)
        
    finally:
        bot.wait(3000)
        bot.stop_browser()

    # Wait 3 seconds before closing
    # bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    # bot.stop_browser()

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
