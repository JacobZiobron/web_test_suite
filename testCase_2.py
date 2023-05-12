from css_library import *
from functions import *

# Tests a wide variety of functions in a different pattern than the first test case

try:
    print("Starting browser automation...")
    # Initialize
    fp, driver = initialize_browser(fp_path, ex_path)

    # Open browser
    open_browser(fp, driver)
    choose_location(fp, driver)
    
    # Navigation and random combinations
    navigate_navbar(fp, driver, about_selector, about_investors_selector)
    click_button(fp, driver, outtages_button)
    click_button(fp, driver, saveMoney_button)
    navigate_navbar(fp, driver, about_selector, about_reliability_selector)
    click_button(fp, driver, uploadDocuments_button)
    switch_states(fp, driver, state_selector, newHampshire_selector)
    use_search(fp, driver, search_button_css, entry_button_css, "savings")
    
    # Lower navigation menu
    click_button(fp, driver, accounts_button)
    click_button(fp, driver, safety_button)
    click_button(fp, driver, supplierOptions_button)

    # Exit browser
    close_browser(fp, driver)
    print("Successfully completed browser automation")
except:
    print("Error with browser navigation")
    close_browser(fp, driver)
    print("Successfully exited with error")