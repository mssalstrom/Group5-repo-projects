from WebInteractionModule import WebInteractionModule
from ValidationModule import ValidationModule
if __name__ == "__main__":
    # Create a WebDriver instance (e.g., Chrome)
    web_interaction = WebInteractionModule('chrome')  # Initialize Chrome WebDriver

    web_interaction.navigate_to_url('http://127.0.0.1:5000/')

    # Create an instance of the ValidationModule class
    validation = ValidationModule(web_interaction.driver)
    
    # Define the expected page title
    expected_title = 'Sample Website'

    # Use the validate_page_title method to check the page title
    is_title_valid = validation.validate_page_title(expected_title)

    # Check the result and print a message
    if is_title_valid:
        print(f"Page title matches the expected title: {expected_title}")
    else:
        print(f"Page title does not match the expected title: {expected_title}")

    
    
    
    
    
    
    
    
    
    
     # report = initialize_report()
    
    
    # navigate_to_url('http://127.0.0.1:5000/')
    
    # print(validate_page_title('Hello')+ ' World!')


    # if validate_page_title("Sample Website"):
    #     search_box = find_element("ID", "searchBoxId")
    #     search_box.send_keys("Test")

    #     if validate_element_presence("ID", "resultId"):
    #         log_result("Search Functionality", "Pass", report)
    #     else:
    #         log_result("Search Functionality", "Fail", report)
    #         capture_screenshot("Search_Fail.png")
    # else:
    #     log_result("Navigation to Sample Website", "Fail", report)

    # driver.quit()

    # print(report)
