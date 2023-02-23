#Importing necessary modules
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from android.config import xpaths, ids

class LoginPage:
    # Define the locators
    EMAIL_FIELD = (MobileBy.XPATH, xpaths.login_email_textfield)
    PASSWORD_FIELD = (MobileBy.XPATH, xpaths.login_password_textfield)
    LOGIN_BUTTON = (MobileBy.XPATH, xpaths.login_button)
    SETTING_BUTTON = (MobileBy.ID, ids.homepage_setting)
    WELCOME_LOOK_LATER = (MobileBy.ID, ids.welcome_page_look_later)

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()

    # Here using the try and except method in this scenario is to demonstrate an approach that can be used to make testing more descriptive.
    # By using the try and except method, we can capture and handle any exceptions that occur during testing, and provide more meaningful error messages to help with debugging.

    def click_setting(self):
        try:
            setting = self.wait.until(EC.element_to_be_clickable(self.SETTING_BUTTON))
            setting.click()
            return True, "Setting button responsive"
        except:
            return False, "Setting button unresponsive"

    def click_look_later_button(self):
        look_later_button = self.wait.until(EC.visibility_of_element_located(self.WELCOME_LOOK_LATER))
        look_later_button.click()


