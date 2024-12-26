from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

# chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options = chromeOptions)

driver = webdriver.Firefox()

try:
    driver.implicitly_wait(10)
    driver.maximize_window()

    url = "https://demoqa.com/menu"
    driver.get(url)

    mainItem = driver.find_element(By.XPATH, "//a[contains(text(), 'Main Item 2')]")
    subItem = driver.find_element(By.XPATH, "//a[contains(text(), 'SUB SUB LIST')]")
    subSubItem = driver.find_element(By.XPATH, "//a[contains(text(), 'Sub Sub Item 2')]")

    action = ActionChains(driver)

    action.move_to_element(mainItem)
    action.move_to_element(subItem)
    action.move_to_element(subSubItem)

    action.perform()
except TimeoutException:
    print("Something went wrong!")
finally:
    pass

    driver.quit()