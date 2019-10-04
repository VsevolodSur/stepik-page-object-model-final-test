from pages.product_page import ProductPage
import pytest


# link = "http://selenium1py.pythonanywhere.com/"
# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.skip
def test_guest_should_see_add_to_backet_form(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_backet_form()

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_backet_form()
    page.check_name_product()
    page.check_price_product()
