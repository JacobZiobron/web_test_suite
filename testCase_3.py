from css_library import *
from functions import *

# Opens, navigates, then closes browser




try:
    print("Starting browser automation...")
    #Initialize
    fp, driver = initialize_browser(fp_path, ex_path)
    open_browser(fp, driver)
    choose_location(fp, driver)

    # Use nav bar
    navigate_navbar(fp, driver, about_selector, about_investors_selector)

    # Exit browser
    close_browser(fp, driver)
    print("Successfully completed browser automation")
except:
    print("Error with browser navigation")
    close_browser(fp, driver)
    print("Successfully exited with error")