#Importing necessary modules
from selenium.webdriver.common.by import By
from android.config import xpaths

def data_protection_accept(driver):
    try:
        x = driver.find_element(By.XPATH, xpaths.data_protection_first)
        x.click()
        return True, "Data protection click confirmed"
    except:
        return False, "Data protection click unresponsive"

