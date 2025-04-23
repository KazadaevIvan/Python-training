from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_ITEM_BUTTON).click()

    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ITEM_NAME), "Success message is presented, but should not be"

    def should_be_item_successfully_added_message(self, item):
        assert item in self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_NAME).text, "Item name is not equal expected"

    def should_be_basket_price(self, price):
        assert price in self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_NAME).text, "Item name is not equal expected"
