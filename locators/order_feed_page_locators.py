from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

   #Локатор номера заказа в всплывающем окне
   ORDER_NUMBER_MODAL = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
   
   
   ORDER_LOADING = (By.XPATH, "//img[@alt='loading animation']")
   

   # Локатор счетчика заказов за всё время
   ALL_TIME_ORDERS_COUNTER = (By.XPATH,"//p[text()='Выполнено за все время:']/following-sibling::p")

   # Локатор счетчика заказов за сегодня
   TODAY_ORDERS_COUNTER = (By.XPATH,"//p[text()='Выполнено за сегодня:']/following-sibling::p")


   @staticmethod
   def order_number_in_progress(order_number):
      return (By.XPATH,
      f"//p[text()='В работе:']/following::li[text()='{order_number}']")
   

   