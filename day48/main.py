from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException

script_dir = os.path.dirname(__file__)

with open(script_dir + "/amazon_urls.txt") as urls_file:
    urls = urls_file.readlines()
    
with open(script_dir + "/amazon_prices.txt") as urls_file:
    prices = urls_file.readlines()
    
def check_exists_by_id(id):
    try:
        driver.find_element(by=By.CLASS_NAME, value=id)
    except NoSuchElementException:
        return False
    return True

chrome_opts = webdriver.ChromeOptions()

chrome_opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_opts)

for i in range(0, len(urls)):
    _url = urls[i]
    if len(prices) > i:
        _price = int(prices[i])
    if len(prices) < i:
        # more expensive product? wtf
        print(f"{_url} is more expensive than before, refusing to write the price")
    else:
        _price = 999999
    driver.get(url=_url)
    
    # cookies terms button in case of present
    if check_exists_by_id("sp-cc-accept"):
        driver.find_element(by=By.ID, value="sp-cc-accept").click()
        
    current_price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole").text
    
    if int(current_price) < _price:
        prices.append(f"{current_price}\n")
        # maybe send msg to alert of price change or something
    print(current_price)
    driver.implicitly_wait(5) # seconds

driver.quit()

with open(script_dir + "/amazon_prices.txt", mode="w") as new_prices_file:
    new_prices_file.writelines([f"{str(price)}" for price in prices])