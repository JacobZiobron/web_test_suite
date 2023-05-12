from css_library import *
from functions import *

# Quick function to use the search function, click a button, then close the browser
try:
    print("Starting browser automation...")
    # Initialize browser
    fp, driver = initialize_browser(fp_path, ex_path)
    open_browser(fp, driver)
    choose_location(fp, driver)

    # Search functionality
    use_search(fp, driver, search_button_css, entry_button_css, "energy efficiency")
    click_button(fp, driver, accounts_button)

    # Exit browser
    close_browser(fp, driver)
    print("Successfully completed browser automation")
except:
    print("Error with browser navigation")
    close_browser(fp, driver)
    print("Successfully exited with error")

