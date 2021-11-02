from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    basket_page = ProductPage(browser, link)
    basket_page.open()
    basket_page.add_to_basket_page()
    basket_page.solve_quiz_and_get_code()
    basket_page.compare_name()
    basket_page.compare_price()


