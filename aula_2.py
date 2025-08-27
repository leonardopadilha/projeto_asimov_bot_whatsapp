from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com/")
driver.implicitly_wait(20)

wait = WebDriverWait(driver, timeout=60)
barra_lateral = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='side']")))
#barra_lateral = driver.find_element(By.XPATH, "//*[@id='side']")

nome_contato = "Cliente 1"
barra_pesquisa = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Search input")]')
barra_pesquisa.send_keys(Keys.CONTROL + "a")
barra_pesquisa.send_keys(Keys.DELETE)
barra_pesquisa.send_keys(nome_contato)

wait = WebDriverWait(driver, timeout=2)
conversa_lateral = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{nome_contato}']")))
conversa_lateral.click()

mensagem = "Olá, tudo bem?"
barra_mensagem = driver.find_element(By.XPATH, '//div[@title="Digite uma mensagem"]')
barra_mensagem.send_keys(mensagem)
barra_mensagem.send_keys(Keys.RETURN) # Enter