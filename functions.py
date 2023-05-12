#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import *
import time
from selenium.webdriver.firefox import firefox_profile
from selenium.webdriver.common.keys import Keys

# initialize web driver
def initialize_browser(fp_path, ex_path):
    """
    Function: 
    * to initialize the browser with indicated profile and driver

    Input Variables:
    * fp_path - path to the firefox profile used for the automation
    * ex_path - path to the gecko driver
    """
    fp = webdriver.FirefoxProfile(fp_path)
    driver = webdriver.Firefox(executable_path=ex_path, firefox_profile=fp)
    return fp, driver

def open_browser(fp, driver):
    """
    Function: 
    * to open the browser with indicated profile and driver

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    """
    print("Opening browser...")
    # open browser
    driver.get("https://www.eversource.com/content/residential")
    print("Browser successfully opened")

def choose_location(fp, driver):
    """
    Function: 
    * choose the location - start with CT

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    """
    print("Choosing location...")
    # enter CT section
    driver.find_element("css selector", ".region-selector__funnel-card:nth-child(1) > .region-selector__img-text").click()
    print("Location successfully chosen")


def click_button(fp, driver, button_css):
    """
    Function: 
    * click an indicated button via it's CSS selector

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    * button_css - the css property of the selector
    """
    print("Navigating to button...")
    button_selection = driver.find_element("css selector", button_css)
    driver.execute_script("arguments[0].scrollIntoView();", button_selection)
    time.sleep(3)
    button_selection.click()
    print("Button successfully clicked")


def close_browser(fp, driver):
    """
    Function: 
    * to exit the browser with indicated profile and driver

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    """
    print("Browser safely exited")
    driver.quit()

def use_search(fp, driver, search_selector, entry_selector, search_query):
    """
    Function: 
    * use the search bar

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    * search_selector - navigate to the search bar
    * entry_selector - selector to input the search_query
    * search_query - string to be searched
    """
    click_button(fp, driver, search_selector)
    search_bar = driver.find_element("css selector", entry_selector)
    search_bar.send_keys(search_query)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)

def switch_states(fp, driver, state_selector, state):
    """
    Function: 
    * change the current state (top right corner menu)

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    * state_selector - selector for state choice
    * state - selector for specific state in the dropdown
    """
    print("Switching states...")
    click_button(fp, driver, state_selector)
    click_button(fp, driver, state)
    print("State successfully switched")

def navigate_navbar(fp, driver, first_field, second_field):
    """
    Function: 
    * use the navigation bar

    Input Variables:
    * fp - firefox profile
    * driver - specific driver used
    * first_field - first dropdown location
    * second_field - second dropdown location
    """
    print("Using navigation bar...")
    time.sleep(2)
    click_button(fp, driver, first_field)
    time.sleep(2)
    click_button(fp, driver, second_field)
    print("Navbar successfully navigated")