import pytest
import allure
import time


from pages.main_page import MainPage
from data.data import DataIngredients

class TestMainPage:

    @allure.title("Проверка перехода в раздел «Лента заказов» по клику на кнопку Лента заказов в шапке")
    def test_open_order_feed(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажимаем на кнопку «Лента заказов»"):
            main_page.click_order_feed_link()
        
        with allure.step("Проверяем, что перешли на страницу Лента заказов"):
            assert main_page.chek_order_feed_title()



    @allure.title("Проверка перехода в раздел «Конструктор» по клику на кнопку «Конструктор» в шапке")
    def test_open_constructor (self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажимаем на Лента заказов"):
            main_page.click_order_feed_link()
        
        with allure.step("Нажимаем на Конструктор"):
            main_page.click_constructor_link()
        
        with allure.step("Проверяем, что перешли на страницу Конструктора"):
            assert main_page.chek_constructor_title()




    @pytest.mark.parametrize("ingredient_type, ingredient_locator", DataIngredients.INGREDIENT_MODAL_CASES)
    @allure.title("Проверка открытия модального окна ингредиента кликом по ингредиенту")
    def test_open_ingredient_details_modal(self, driver, ingredient_type, ingredient_locator):
        main_page = MainPage(driver)

        main_page.open_ingredient_details(ingredient_type)

        assert main_page.is_ingredient_details_modal_visible()
        assert main_page.is_ingredient_name_in_modal_visible(ingredient_locator)
    

    @allure.title("Проверка закрытия всплывающего окна по клику на крестик")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.open_sauce_details()
        main_page.click_close_button_in_modal()

        assert main_page.is_ingredient_modal_closed()



    @allure.title("Проверка увеличения счетчика ингредиента после добавления в заказ")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        old_counter = main_page.get_sauce_counter_value()

        main_page.drag_sauce_to_basket()
        assert main_page.is_sauce_counter_increased(old_counter)










    
