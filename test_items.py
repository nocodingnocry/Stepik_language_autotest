import time   

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_is_displayed(browser):
   browser.get(link)
   element = browser.find_elements_by_css_selector('button.btn-add-to-basket') #Поиск кнопки по селектору
   assert element, 'button is missing'  #Проверяем нашлась ли кнопка
    
   time.sleep(3)
