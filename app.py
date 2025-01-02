from coin import Coin
from trade import Trade
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=options)
wait = ui.WebDriverWait(driver,20)

driver.get("https://pump.fun/advanced")
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/button')))
driver.find_element(By.XPATH, '/html/body/div/button').click()

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[1]/main/div/div[1]/div/div/div/a')))

trending_coins_scraped = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/main/div/div[1]/div/div/div/a')


trending_coins = []

for coin in trending_coins_scraped:
    this_coin = Coin()

    link = coin.get_attribute("href")
    this_coin.link = link

    marketcap = coin.find_element(By.XPATH, './/div/div/span[2]').text
    this_coin.market_cap = marketcap

    volume = coin.find_element(By.XPATH, './/div/div[2]/span[2]').text
    this_coin.volume = volume

    trending_coins.append(this_coin)

for coin in trending_coins:
    print(coin.link)
    print(coin.volume)
    print(coin.market_cap)

    continue


driver.quit