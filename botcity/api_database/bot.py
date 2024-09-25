# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Added webdriver for chrome
from webdriver_manager.chrome import ChromeDriverManager

# Added http plugin
from botcity.plugins.http import BotHttpPlugin

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def pesquisar_cidade(bot: WebBot, cidade: str):
    bot.browse("https://www.google.com")
    while len(bot.find_elements('//*[@id="APjFqb"]', By.XPATH))<1:
        bot.wait(1000)
        print('carregando')

    bot.find_element('//*[@id="APjFqb"]', By.XPATH).send_keys(cidade)
    bot.wait(1000)
    bot.enter()    

def extrair_dados(bot):
    cont = 0
    while True:
        cont += 1
        dia_semana = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[1]', By.XPATH).text
        temp_max = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[1]', By.XPATH).text
        temp_min = bot.find_element(f'//*[@id="wob_dp"]/div[{cont}]/div[3]/div[2]', By.XPATH).text
        print(f'Dia: { dia_semana} - Max: {temp_max} - Min:{temp_min}')
        if cont == 8:
            break

def obter_dados_api():
    """
    Obtém dados da API e retorna como JSON.
    """
    try:
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/13/regioes-metropolitanas'
        http = BotHttpPlugin(url)
        retorno_json = http.get_as_json()
        return retorno_json
    except Exception as ex:
        print(f"Erro ao obter dados da API: {ex}")
        return []
    
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
    # Changed para chrome
    bot.browser = Browser.CHROME

    # Uncomment to set the WebDriver path 
    # Changed to chrome 
    bot.driver_path = ChromeDriverManager().install()

    # Opens the BotCity website.
    # bot.browse("https://www.google.com")

    # Implement here your logic...

    try:
        dados = obter_dados_api()

        for item in dados:
            # print(item['id'])
            # print(item['nome'])
            # print(item['UF']['id'])
            # print(item['municipios'][1])
            for m in item['municipios']:
                
                #print(m['nome']) 
                cidade = m['nome'] 
                print(f"\n {cidade}") 
                cidade = (" clima ", cidade, " Amazonas")   
                pesquisar_cidade(bot,cidade)
                bot.wait(3000)
                extrair_dados(bot)
    
    except Exception as ex:
        print(ex)
        bot.save_screenshot('erro.png')

    finally:
        bot.wait(3000)

    # Wait 3 seconds before closing
    bot.wait(3000)

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
