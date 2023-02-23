from appium import webdriver
from android.config import config
from appium.webdriver.common.touch_action import TouchAction

def restart_app(driver):
    driver.close_app()
    driver.launch_app()

def check_app_opens_firsttime(driver):
    try:
        x = driver.find_element("xpath", "//android.widget.TextView[@text='I have a user account']").text
        return True
    except:
        return False


def click_by_bounds(x1,y1,x2,y2,driver):

    # Find the element using its bounds
    element_bounds = (x1, y1, x2, y2)  # Replace with the actual bounds of the element
    x = (element_bounds[0] + element_bounds[2]) // 2  # Calculate the x coordinate of the center of the element
    y = (element_bounds[1] + element_bounds[3]) // 2  # Calculate the y coordinate of the center of the element

    # Click on the element using its center coordinates
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()