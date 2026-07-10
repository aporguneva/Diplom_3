from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step("Кликаем на элемент")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Клик через JavaScript")
    def js_click(self, locator):
        self.driver.execute_script("arguments[0].click();", self.find_element(locator))


    @allure.step("Находим элемент")
    def find_element(self, locator):
        return self.wait.until(
        EC.visibility_of_element_located(locator))

    
    @allure.step("Проверяем, что элемент отображается")
    def check_element_is_visible(self, locator):
        return self.find_element(locator).is_displayed()
    
    
    @allure.step("Скроллим к элементу")
    def scroll_to(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            self.find_element(locator)
        )
    

    @allure.step("Вводим текст")
    def type (self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Получаем текст")
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step("Ждём, что текст элемента изменится")
    def wait_for_text_to_change(self, locator, old_text):
        self.wait.until(
            lambda driver: self.get_text(locator) != old_text
        )
        
    def wait_for_element_to_disappear(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def drag_and_drop(self, source_locator, target_locator):
        
        #Перетаскивает элемент из source_locator в target_locator с использованием JavaScript.
        #:param source_locator: Локатор элемента, который нужно перетащить.
        #:param target_locator: Локатор элемента, куда нужно перетащить.
            
        self.find_element(source_locator)
        self.find_element(target_locator)

        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    
        

    
    
