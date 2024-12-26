from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chromeOptions)

driver.get("https://saucedemo.com")
driver.maximize_window()

driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("secret_sauce")
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

elements = driver.find_elements(By.XPATH, "//div[@class='pricebar']/child::button")

for i in range(3):
    elements[i].click()

sleep(3)

driver.quit()