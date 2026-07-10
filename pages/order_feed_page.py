import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Создаём и авторизуем пользователя")
    def create_and_login_user(self, user_data):

        self.click(AccountPageLocators.LOGIN_ACCOUNT_BUTTON)

        self.click(AccountPageLocators.REGISTER_LINK)

        self.type(AccountPageLocators.NAME_INPUT, user_data["name"])
        self.type(AccountPageLocators.EMAIL_INPUT, user_data["email"])
        self.type(AccountPageLocators.PASSWORD_INPUT, user_data["password"])
        self.click(AccountPageLocators.REGISTER_BUTTON)

        self.find_element(AccountPageLocators.LOGIN_BUTTON)

        self.type(AccountPageLocators.EMAIL_INPUT, user_data["email"])
        self.type(AccountPageLocators.PASSWORD_INPUT, user_data["password"])
        self.click(AccountPageLocators.LOGIN_BUTTON)

        self.find_element(MainPageLocators.CREATE_ORDER_BUTTON)


    @allure.step("Кликаем Лента заказов")
    def click_order_feed_link(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Кликаем Конструктор")
    def click_constructor_link(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
        
    @allure.step("Получаем счетчик заказов за все время")
    def get_all_time_orders_counter(self):
        return int(self.get_text(MainPageLocators.ALL_TIME_ORDERS_COUNTER))

    @allure.step("Получаем счетчик заказов за сегодня")
    def get_today_orders_counter(self):
        return int(self.get_text(MainPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Перетаскиваем булку в корзину")
    def drag_bun_to_basket(self):
        self.scroll_to(MainPageLocators.BUN_ELEMENT)
        self.drag_and_drop(
            MainPageLocators.BUN_ELEMENT,
            MainPageLocators.CONSTRUCTOR_BASKET
        )
        
    @allure.step("Перетаскиваем соус в корзину")
    def drag_sauce_to_basket(self):
        self.scroll_to(MainPageLocators.SAUCE_ELEMENT)
        self.drag_and_drop(
            MainPageLocators.SAUCE_ELEMENT,
            MainPageLocators.CONSTRUCTOR_BASKET
        )

    @allure.step("Нажимаем кнопку Оформить заказ")
    def click_create_order_button(self):
        self.click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Создаём заказ")
    def create_order(self):
        self.drag_bun_to_basket()
        self.drag_sauce_to_basket()
        self.click_create_order_button()
        
    
    @allure.step("Ждём загрузки номера заказа")
    def wait_order_number_loaded(self):
        old_number = self.get_text(OrderFeedPageLocators.ORDER_NUMBER_MODAL)
        self.wait_for_text_to_change(
            OrderFeedPageLocators.ORDER_NUMBER_MODAL,
            old_number
        )

    @allure.step("Получаем номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(OrderFeedPageLocators.ORDER_NUMBER_MODAL)
    
    @allure.step("Клик по крестику в всплывающем окне")
    def click_close_button_in_modal(self):
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)


    @allure.step("Ждём закрытия модального окна")
    def wait_modal_closed(self):
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_WINDOW)

    @allure.step("Ждём исчезновения overlay модального окна")
    def wait_modal_overlay_closed(self):
        return self.wait_for_element_to_disappear(
            MainPageLocators.MODAL_OVERLAY
        )

    @allure.step("Проверяем, что заказ появился в списке В работе")
    def is_order_in_progress_visible(self, order_number):
        return self.check_element_is_visible(
            OrderFeedPageLocators.order_number_in_progress(order_number)
        )

    @allure.step("Проверяем, что счетчик за все время увеличился")
    def is_all_time_counter_increased(self, old_counter):
        return self.get_all_time_orders_counter() > old_counter

    @allure.step("Проверяем, что счетчик за сегодня увеличился")
    def is_today_counter_increased(self, old_counter):
        return self.get_today_orders_counter() > old_counter