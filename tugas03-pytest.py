import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

class LoginPageElements:
    loginError = "//div[@class='orangehrm-login-error']/div[@role='alert']/div/p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    inputUsername = "//input[@name='username']"
    inputPassword = "//input[@name='password']"
    errorSpanUsername = "//input[@name='username']/../../span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    errorSpanPassword = "//input[@name='password']/../../span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    buttonLogin = "//button[@type='submit']"

class NavElements:
    headerUserArea = "//div[@class='oxd-topbar-header-userarea']"
    headerUserName = "//div[@class='oxd-topbar-header-userarea']/ul/li/span/p"

@pytest.fixture
def setup():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options = chromeOptions)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def testLoginPositive(setup : webdriver.Chrome):
    setup.find_element(By.XPATH, LoginPageElements.inputUsername).send_keys("Admin")
    setup.find_element(By.XPATH, LoginPageElements.inputPassword).send_keys("admin123")
    setup.find_element(By.XPATH, LoginPageElements.buttonLogin).click()

    print("Logging in...")

    try:
        WebDriverWait(setup, 20).until(EC.presence_of_element_located((By.XPATH, NavElements.headerUserArea)))

        userName = setup.find_element(By.XPATH, NavElements.headerUserName).text

        print(f"Logged in as {userName}.")
    except Exception as e:
        print("Login failed.")

        print(e)

        assert False

userPassBlank = [
    ("Admin", "", "", "Required"),
    ("", "admin123", "Required", ""),
    ("", "", "Required", "Required")
]

@pytest.mark.parametrize("username, password, expectedUserMessage, expectedPassMessage", userPassBlank)
def testLoginNegativeBlank(setup : webdriver.Chrome, username, password, expectedUserMessage, expectedPassMessage):
    setup.find_element(By.XPATH, LoginPageElements.inputUsername).send_keys(username)
    setup.find_element(By.XPATH, LoginPageElements.inputPassword).send_keys(password)
    setup.find_element(By.XPATH, LoginPageElements.buttonLogin).click()

    try:
        userMessage = setup.find_element(By.XPATH, LoginPageElements.errorSpanUsername).text
    except NoSuchElementException:
        userMessage = ''

    try:
        passMessage = setup.find_element(By.XPATH, LoginPageElements.errorSpanPassword).text
    except NoSuchElementException:
        passMessage = ''

    assert userMessage == expectedUserMessage
    assert passMessage == expectedPassMessage

userPassIncorrect = [
    ("Admin", "Admin123"),
    ("admin", "admin123"),
    ("TheAdmin", "admin123"),
]

@pytest.mark.parametrize("username, password", userPassIncorrect)
def testLoginNegativeIncorrect(setup : webdriver.Chrome, username, password):
    setup.find_element(By.XPATH, LoginPageElements.inputUsername).send_keys(username)
    setup.find_element(By.XPATH, LoginPageElements.inputPassword).send_keys(password)
    setup.find_element(By.XPATH, LoginPageElements.buttonLogin).click()

    WebDriverWait(setup, 5).until(EC.presence_of_element_located((By.XPATH, LoginPageElements.loginError)))

    try:
        message = setup.find_element(By.XPATH, LoginPageElements.loginError).text
    except NoSuchElementException:
        message = ''

    assert message == "Invalid credentials"