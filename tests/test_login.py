from pages.home_page import HomePage
from multiprocessing.connection import wait
import time
from selenium.webdriver.common.by import By
from pages.home_page import HomePage

def test_login(driver):
    home_page = HomePage (driver)
    home_page.go_to("https://www.saucedemo.com/")
    home_page.login("standard_user", "secret_sauce")
    assert home_page.get_products_text() == "PRODUCTS"
    home_page.add_to_cart()
    assert home_page.your_cart_text() == "YOUR CART"
    assert home_page.item_name_text("//div[text()='Sauce Labs Bolt T-Shirt']") == "Sauce Labs Bolt T-Shirt"
    assert home_page.item_name_text("//div[text()='Test.allTheThings() T-Shirt (Red)']") == "Test.allTheThings() T-Shirt (Red)"
    home_page.checkout_page()
    assert home_page.checkout_page_text() == "CHECKOUT: YOUR INFORMATION"
    home_page.checkout_information("Azra", "Rizvanovic", "71000")
    assert home_page.overview_page() == "CHECKOUT: OVERVIEW"
    assert home_page.product1_check("//div[text()='Sauce Labs Bolt T-Shirt']") == "Sauce Labs Bolt T-Shirt"
    assert home_page.product2_check("//div[text()='Test.allTheThings() T-Shirt (Red)']") == "Test.allTheThings() T-Shirt (Red)"
    home_page.get_finish()
    assert home_page.checkout_complete_page() == "CHECKOUT: COMPLETE!"
    home_page.get_menu()
    home_page.logout_page()
    time.sleep(5)
    