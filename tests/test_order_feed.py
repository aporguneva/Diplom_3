import allure

from pages.order_feed_page import OrderFeedPage
from helper.helper import generate_user_data


class TestOrderPage:

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_all_time_orders_counter_increased_after_create_order(self, driver):
        order_page = OrderFeedPage(driver)

        user_data = generate_user_data()
        order_page.create_and_login_user(user_data)


        order_page.click_order_feed_link()

        old_all_time_counter = order_page.get_all_time_orders_counter()
        old_today_counter = order_page.get_today_orders_counter()

        order_page.click_constructor_link()
        
        order_page.create_order()

        order_page.wait_order_number_loaded()
        order_number = order_page.get_order_number_from_modal()

        order_page.click_close_button_in_modal()

        order_page.wait_modal_closed()
        order_page.wait_modal_overlay_closed()
        
        order_page.click_order_feed_link()

        assert order_page.is_all_time_counter_increased(old_all_time_counter)
    


    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increased_after_create_order(self, driver):
        order_page = OrderFeedPage(driver)

        user_data = generate_user_data()
        order_page.create_and_login_user(user_data)


        order_page.click_order_feed_link()

        old_all_time_counter = order_page.get_all_time_orders_counter()
        old_today_counter = order_page.get_today_orders_counter()

        order_page.click_constructor_link()
            
        order_page.create_order()

        
        order_page.wait_order_number_loaded()   
        order_number = order_page.get_order_number_from_modal()

        order_page.click_close_button_in_modal()

        order_page.wait_modal_closed()
        order_page.wait_modal_overlay_closed()
            
        order_page.click_order_feed_link()

        assert order_page.is_today_counter_increased(old_today_counter)


  
    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_after_create_order(self, driver):
        order_page = OrderFeedPage(driver)

        user_data = generate_user_data()
        order_page.create_and_login_user(user_data)


        order_page.click_order_feed_link()

        old_all_time_counter = order_page.get_all_time_orders_counter()
        old_today_counter = order_page.get_today_orders_counter()

        order_page.click_constructor_link()
        
        order_page.create_order()

    
        order_page.wait_order_number_loaded()
        order_number = order_page.get_order_number_from_modal()

        order_page.click_close_button_in_modal()

        order_page.wait_modal_closed()
        order_page.wait_modal_overlay_closed()
        
        order_page.click_order_feed_link()

        assert order_page.is_order_in_progress_visible(order_number)
     