import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def setup():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options = chromeOptions)
    driver.minimize_window()
    driver.get("https://saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def testLoginPositive(setup : webdriver.Chrome):
    setup.find_element(By.ID, "user-name").send_keys("standard_user")
    setup.find_element(By.ID, "password").send_keys("secret_sauce")
    setup.find_element(By.ID, "login-button").click()

    print("Logging in...")

    try:
        WebDriverWait(setup, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))

        assert setup.find_element(By.XPATH, "//div[@class='app_logo']").text == "Swag Labs"
        
        assert setup.find_element(By.XPATH, "//span[@class='title']").text == "Products"

        print("Login successful.")
    except Exception as e:
        print("Login failed.")

        print(e)

        assert False

userPass = [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("StandardUser", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "secretSauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("", "secret_sauce", "Epic sadface: Username is required"),
]

@pytest.mark.parametrize("username, password, expectedMessage", userPass)
def testLoginNegative(setup : webdriver.Chrome, username, password, expectedMessage):
    setup.find_element(By.ID, "user-name").send_keys(username)
    setup.find_element(By.ID, "password").send_keys(password)
    setup.find_element(By.ID, "login-button").click()

    errorMessage = setup.find_element(By.XPATH, "//h3[@data-test='error']").text

    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Expected message: {expectedMessage}")
    print(f"Message shown: {errorMessage}")

    assert errorMessage == expectedMessage