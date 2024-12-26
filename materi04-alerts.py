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

    url = "https://demoqa.com/alerts"
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "alertButton")))

    driver.find_element(By.ID, "alertButton").click()

    WebDriverWait(driver, 10).until(EC.alert_is_present)

    driver.switch_to.alert.accept()

    print("There was an alert!")
except TimeoutException:
    print("Something went wrong!")
finally:
    driver.quit()