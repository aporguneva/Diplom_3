from selenium.webdriver.common.by import By

class AccountPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")

    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")   