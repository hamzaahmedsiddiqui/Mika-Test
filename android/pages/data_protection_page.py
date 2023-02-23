#Importing necessary modules
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from android.config import xpaths
import time
from android.utilities import functions


class DataProtectionPage:
    # Define the locators
    NEXT_BUTTON = (MobileBy.XPATH, xpaths.data_protection_next)
    DATA_PROTECTION_FIRST = (MobileBy.XPATH, xpaths.data_protection_first)

    def __init__(self, driver: WebDriver):
        # Store the driver and create a WebDriverWait object
        self.driver = driver

    def accept_data_protection(self):
        functions.click_by_bounds(176, 828, 992, 1156, self.driver)
        time.sleep(2)

    def click_next_button(self):
        functions.click_by_bounds(28, 1967, 1045, 2163, self.driver)
        time.sleep(5)

