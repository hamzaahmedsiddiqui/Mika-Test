#Section1: Importing Modules
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from android.utilities import functions
from android.config import xpaths, config, ids
from android.pages import login_page, data_protection_page, partner_code_page
import pytest
import time

#Section2: Defining Desired capabilities
dcaps = config.android_desire_capability

host = config.android_host
driver = webdriver.Remote(host, dcaps)
driver.implicitly_wait(30)
wait = WebDriverWait(driver, 10)

login_page = login_page.LoginPage(driver)
data_protection_page = data_protection_page.DataProtectionPage(driver)
partner_code_page = partner_code_page.PartnerCodePage(driver)


# Test Case #1
def test_login_success(login_fixture):

    # Wait for the success element to be visible
    success_element = wait.until(EC.visibility_of_element_located((By.ID, ids.login_successfull_page)))
    driver.implicitly_wait(30)

    # Assert that the success element is present
    assert success_element is not None, "Login failed"
    functions.restart_app(driver)

# Test Case #2
def test_click_settings_button(login_fixture):
    # Wait for 5 seconds
    time.sleep(5)

    val, msg = login_page.click_setting()
    # Wait for 5 seconds
    time.sleep(5)
    assert val == True

    # Wait for the success element to be visible
    success_element = driver.find_element(By.XPATH, xpaths.setting)
    driver.implicitly_wait(30)

    # Assert that the success element is present
    text = success_element.text
    assert text == "Settings", "Navigate to setting page failed"

    # Wait for 3 seconds
    time.sleep(3)

    functions.restart_app(driver)

# Test Case #3
def test_entering_code():
    # Wait for 5 seconds
    time.sleep(5)

    # Check if the app opens for the first time
    if functions.check_app_opens_firsttime(driver):

        # Find and click the "I am new here" button
        btn = driver.find_element(By.XPATH, xpaths.i_am_new_here)
        btn.click()

    # Wait for 2 seconds
    time.sleep(2)

    # Accept the data protection terms
    data_protection_page.accept_data_protection()

    # Click the "Next" button
    data_protection_page.click_next_button()

    # Add the partner code
    partner_code_page.add_partner_code(config.partner_code)
    time.sleep(2)

    # Tap the "Go to account setup" button
    partner_code_page.tap_goto_account_setup()

    # Wait for the success element to be visible
    success_element = driver.find_element(By.XPATH, xpaths.code_activated)
    driver.implicitly_wait(30)

    # Assert that the success element is present
    text = success_element.text
    assert text == "Mika has now been activated.", "Code in not activate"


@pytest.fixture
def login_fixture():
    time.sleep(5)

    # Checking if application is open first time
    if functions.check_app_opens_firsttime(driver):
        # Click on "I have a user account"
        btn = driver.find_element(By.XPATH, xpaths.I_have_a_user_account)
        btn.click()

    # Fill login details
    login_page.enter_email(config.login_email)
    login_page.enter_password(config.login_passowrd)
    time.sleep(2)

    # Click on login button
    login_page.click_login_button()
    time.sleep(5)
    login_page.click_look_later_button()





