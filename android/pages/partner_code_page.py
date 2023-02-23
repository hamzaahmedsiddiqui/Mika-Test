
#Importing necessary modules
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from android.config import xpaths


class PartnerCodePage:
    # Define the locators
    CODE_TEXTVIEW = (MobileBy.XPATH, xpaths.partner_code)
    GOTO_ACCOUNT_SETUP = (MobileBy.XPATH, xpaths.goto_account_setup)

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)

    def add_partner_code(self, code):
        partner_code_field = self.wait.until(EC.visibility_of_element_located(self.CODE_TEXTVIEW))
        partner_code_field.send_keys(code)

    def tap_goto_account_setup(self):
        goto_account_setup = self.wait.until(EC.element_to_be_clickable(self.GOTO_ACCOUNT_SETUP))
        goto_account_setup.click()
