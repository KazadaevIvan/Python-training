from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators:
    ITEM_PRICE = (By.XPATH, "//article[@class='product_page']//p[@class='price_color']")
    ITEM_NAME = (By.XPATH, "//article[@class='product_page']//h1")
    ADD_ITEM_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")
    MESSAGE_ITEM_NAME = (By.XPATH, "//div[@id='messages']//strong")
    MESSAGE_ITEM_PRICE = (By.XPATH, "//div[@id='messages']//p/strong")

class BasketPageLocators:
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_TO_BUY_TITLE = (By.CSS_SELECTOR, "#content_inner h2")