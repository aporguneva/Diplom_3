from data.urls import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):

    @allure.step("Клик по кнопке Конструктор» в шапке")
    def click_constructor_link(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step("Проверка перехода в Конструктор по заголовку Соберите бургер")
    def chek_constructor_title(self):
        return self.check_element_is_visible(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Клик по кнопке Лента заказов» в шапке")
    def click_order_feed_link(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Проверка перехода в Ленту заказов по заголовку Лента заказов")
    def chek_order_feed_title(self):
        return self.check_element_is_visible(MainPageLocators.ORDER_FEED_TITLE)




    @allure.step("Клик по булке «Флюоресцентная булка R2-D3» и кликаем")
    def open_bun_details(self):
        self.click(MainPageLocators.BUN_ELEMENT)

    @allure.step("Скроллим к соусу «Spicy-X» и кликаем")
    def open_sauce_details(self):
        self.scroll_to(MainPageLocators.SAUCE_ELEMENT)
        self.click(MainPageLocators.SAUCE_ELEMENT)

    @allure.step("Скроллим к начинке «Мини-салат Экзо-Плантаго» и кликаем")
    def open_fillings_details(self):
        self.scroll_to(MainPageLocators.FILLINGS_ELEMENT)
        self.click(MainPageLocators.FILLINGS_ELEMENT)

    @allure.step("Открываем детали ингредиента")
    def open_ingredient_details(self, kind: str):
        actions = {
            "bun": self.open_bun_details,
            "sauce": self.open_sauce_details,
            "filling": self.open_fillings_details,
        }
        actions[kind]()

    @allure.step("Проверяем отображение модального окна")
    def is_ingredient_details_modal_visible(self):
        return (self.check_element_is_visible(MainPageLocators.MODAL_WINDOW)
            and
            self.check_element_is_visible(MainPageLocators.MODAL_TITLE))

    @allure.step("Проверяем название ингредиента в модальном окне")
    def is_ingredient_name_in_modal_visible(self, ingredient_locator):
        return self.check_element_is_visible(ingredient_locator)
    

    @allure.step("Клик по крестику в всплывающем окне")
    def click_close_button_in_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверяем что всплывающее окно закрылось")
    def is_ingredient_modal_closed(self):
        return self.wait_for_element_to_disappear(MainPageLocators.MODAL_WINDOW)
    



    @allure.step("Перетаскиваем соус «Spicy-X» в корзину заказа")
    def drag_sauce_to_basket(self):
        self.scroll_to(MainPageLocators.SAUCE_ELEMENT)
        self.drag_and_drop(
            MainPageLocators.SAUCE_ELEMENT,
            MainPageLocators.CONSTRUCTOR_BASKET
        )


    @allure.step("Получаем значение счетчика соуса «Spicy-X»")
    def get_sauce_counter_value(self):
        return int(self.get_text(MainPageLocators.ELEMENT_COUNTER))


    @allure.step("Проверяем, что счетчик соуса увеличился")
    def is_sauce_counter_increased(self, old_counter):
        new_counter = self.get_sauce_counter_value()
        return new_counter > old_counter





