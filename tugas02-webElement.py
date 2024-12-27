from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    url = "https://demoqa.com/alerts"

    driver.get(url)

    # Alert box
    driver.find_element(By.ID, "alertButton").click()
    Wait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("We just accepted an alert!")

    # Delayed Alert Box
    driver.find_element(By.ID, "timerAlertButton").click()
    Wait(driver, 6).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("We just accepted a delayed alert!")

    # Confirm Box - Accept
    buttons = driver.find_element(By.ID, "confirmButton").click()
    Wait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    confirmResult = driver.find_element(By.ID, "confirmResult").text
    print(f"We just accepted a confirm box! The website said: {confirmResult}")

    # Confirm Box - Dismiss
    buttons = driver.find_element(By.ID, "confirmButton").click()
    Wait(driver, 5).until(EC.alert_is_present())
    driver.switch_to.alert.dismiss()
    confirmResult = driver.find_element(By.ID, "confirmResult").text
    print(f"We just dismissed a confirm box! The website said: {confirmResult}")

    # Prompt Box
    driver.find_element(By.ID, "promtButton").click()
    Wait(driver, 5).until(EC.alert_is_present())
    prompt = driver.switch_to.alert
    name = "Robert"
    prompt.send_keys(name)
    prompt.accept()
    promptResult = driver.find_element(By.ID, "promptResult").text
    print(f"We just entered {name} in a prompt box! The website said: {promptResult}")

    if (promptResult.endswith(name)):
        print("It matches with the name we typed!")
    else:
        print("It doesn't match with the name we typed!")
except TimeoutException:
    print("Oh no! We cannot play with the alert prompts!")
finally:
    driver.quit()