from selenium import webdriver
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chromeOptions)
driver.minimize_window()

# driver2 = webdriver.Firefox()
# driver2.get("https://google.com")

driver.get("https://idejongkok.com")
print(driver.title)

driver.get("https://kelasotomesyen.com")
print(driver.title)

driver.maximize_window()

driver.back()
print(driver.title)

sleep(5)

driver.quit()