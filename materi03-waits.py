from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chromeOptions)

try:
    driver.implicitly_wait(10)
    driver.maximize_window()

    url = "https://saucedemo.com"

    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.ID, 'password').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    driver.find_element(By.ID, 'react-burger-menu-btn').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))

    driver.find_element(By.ID, "logout_sidebar_link").click()

    print("We can log out!")
except TimeoutException:
    print("Oh no! We cannout log out!")
finally:
    driver.quit()