from selenium.webdriver.common.by import By

class MainPageLocators:

    #Локатор кнокпки Конструктор
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/' and .//p[text()='Конструктор']]")

    #Локатор заголовка Соберите бургер
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    #Локатор кнокпки Лента заказов
    ORDER_FEED_LINK = (By.XPATH, "//a[@href='/feed' and .//p[text()='Лента Заказов']]")

    #Локатор заголовка Лента заказов 
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    
    #Локатор Флюоресцентная булка R2-D3
    BUN_ELEMENT = (By.XPATH, "//a[.//p[text()='Флюоресцентная булка R2-D3']]")

    #Локатор названия булки в всплывающем окне Детали ингредиента
    BUN_NAME_IN_MODAL = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")

    #Локатор Соус Spicy-X
    SAUCE_ELEMENT = (By.XPATH, "//a[.//p[text()='Соус Spicy-X']]")

    #Локатор названия соуса в всплывающем окне Детали ингредиента
    SAUCE_NAME_IN_MODAL = (By.XPATH, "//p[text()='Соус Spicy-X']")

    #Локатор начинки Мини-салат Экзо-Плантаго
    FILLINGS_ELEMENT = (By.XPATH, "//a[.//p[text()='Мини-салат Экзо-Плантаго']]")

    #Локатор названия начинки в всплывающем окне Детали ингредиента
    FILLINGS_NAME_IN_MODAL = (By.XPATH, "//p[text()='Мини-салат Экзо-Плантаго']")

    #Локатор всплывающего окна Детали ингредиента
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")

    #Локатор заголовка в всплывающем окне Детали ингредиента
    MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']") 

    #Локатор крестика 
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    # Локатор overlay модального окна
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    
    #Локатор счетчика соуса Spicy-X
    ELEMENT_COUNTER = (By.XPATH,
        "//a[.//p[text()='Соус Spicy-X']]//p[contains(@class, 'counter_counter__num')]")
    
    #Локатор корзины заказа
    CONSTRUCTOR_BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    #Локатор кнопки Оформить заказ
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    #Локатор счетчика заказов за все время
    ALL_TIME_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")

    #Локатор счетчика заказов за сегодня
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")





    

