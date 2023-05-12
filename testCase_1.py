from css_library import *
from functions import *

# Tests a wide variety of website functions

try:
    print("Starting browser automation...")
    # Initialize
    fp, driver = initialize_browser(fp_path, ex_path)

    # Opening browser and initializing first location
    open_browser(fp, driver)
    choose_location(fp, driver)

    # Functions to test the navigation bar
    navigate_navbar(fp, driver, about_selector, about_investors_selector)
    navigate_navbar(fp, driver, about_selector, about_reliability_selector)

    # Search functionality
    use_search(fp, driver, search_button_css, entry_button_css, "capital projects")

    # State switching
    switch_states(fp, driver, state_selector, newHampshire_selector)

    # Lower navigation menu
    click_button(fp, driver, accounts_button)
    click_button(fp, driver, outtages_button)
    click_button(fp, driver, saveMoney_button)
    click_button(fp, driver, safety_button)
    click_button(fp, driver, supplierOptions_button)
    click_button(fp, driver, uploadDocuments_button)

    # Exit browser
    close_browser(fp, driver)

    print("Successfully completed browser automation")
except:
    print("Error with browser navigation")
    close_browser(fp, driver)
    print("Successfully exited with error")