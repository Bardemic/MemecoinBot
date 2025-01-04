from coin import Coin
from trade import Trade
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")


driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
wait = ui.WebDriverWait(driver,20)

driver.get("https://pump.fun/advanced")
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/button')))
driver.find_element(By.XPATH, '/html/body/div/button').click()

driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/button[1]').click()

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
    #print(coin.link)
    #print(coin.volume)
    #print(coin.market_cap)
    time.sleep(2.5)

    driver.get(coin.link)

    time.sleep(2.5)

    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[1]/div[3]/div[2]')))
    driver.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[1]/div[3]/div[2]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tradesBySize"]')))
    driver.find_element(By.XPATH, '//*[@id="tradesBySize"]').click()

    time.sleep(1)
    pages_of_trades = ((driver.find_element(By.XPATH, '//div[5]/div/div/span')).text).split(' ')
    print(pages_of_trades)
    if len(pages_of_trades) == 3:
        if int(pages_of_trades[2]) <= 5: go_to_page = int(pages_of_trades[2])
        else: go_to_page = 5
    else:
        go_to_page = 1
    current_page = 1
    while current_page <= go_to_page:
        current_page_trades = []
        while current_page_trades == []:
            print(f'checking page {current_page}')
            try:
                time.sleep(0.5)
                trade_type = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[1]/div[4]/div[4]/table/tbody/tr/td[2]')
                trade_amount = driver.find_elements(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div[1]/div[4]/div[4]/table/tbody/tr/td[4]')
                for index in range(len(trade_type)): #loops through trades
                    new_trade = Trade()
                    new_trade.trade_type = trade_type[index].text
                    new_trade.sol_amount = trade_amount[index].text
                    current_page_trades.append(new_trade)

                    #print(new_trade.trade_type)
                    #print(new_trade.sol_amount)

                    
            except Exception:
                current_page_trades = []
                print("Exception, trying again")
                time.sleep(2)
            if current_page != go_to_page: driver.find_element(By.XPATH, '//div[5]/div/div/button[3]').click() #click next page button
            print(f'done checking page {current_page}, final page is {go_to_page}')
            current_page += 1



driver.quit