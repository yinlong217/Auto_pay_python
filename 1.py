from pchome_autobuy import login 
from selenium import webdriver
driver = webdriver.Chrome("./chromedriver")
driver.get("https://p-bandai.com/hk/login")

login()
