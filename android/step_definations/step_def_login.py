#Section1: Importing Modules
from pytest_bdd import scenario, given, when, then
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from android.utilities import functions
from android.config import xpaths, config, ids
from android.pages import login_page


#Section2: Defining Desired capabilities
dcaps = config.android_desire_capability

host = config.android_host
driver = webdriver.Remote(host, dcaps)
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)
login_page = login_page.LoginPage(driver)

#Section3: First Scenario
@scenario('../features/login.feature','verifying user login')
def test_publish():
    pass

@given("the user install the application and the user is on login page")
def login_to_app():
    if functions.check_app_opens_firsttime(driver):
        # Click on "I have a user account"
        btn = driver.find_element(By.XPATH, xpaths.I_have_a_user_account)
        btn.click()
    print("given working")

@when("the user enter email address")
def enter_email_address():
    login_page.enter_email(config.login_email)
    print("When working")

@when("the user enter password")
def enter_password():
    login_page.enter_password(config.login_passowrd)
    print("When working")

@when("the user tap login button")
def button_tap():
    login_page.click_login_button()
    print("When working")

@then("the user should see login successful")
def success():
    # Wait for the success element to be visible
    success_element = wait.until(EC.visibility_of_element_located((By.ID, ids.login_successfull_page)))

    # Assert that the success element is present
    assert success_element is not None, "Login failed"
    print("success")

