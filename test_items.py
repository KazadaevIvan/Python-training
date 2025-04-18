from selenium.webdriver.common.by import By

URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
ADD_ITEM_BUTTON_LOCATOR = (By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")

class TestClass:

    def test_item_page_should_contain_add_item_button(self, browser):
        browser.get(URL)

        assert browser.find_element(*ADD_ITEM_BUTTON_LOCATOR).is_displayed() == True, "Add Item button is not displayed"