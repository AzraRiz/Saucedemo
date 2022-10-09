from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from time import time
from turtle import clear
from xml.dom.minidom import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    # 1. Otvori web stranicu https://www.saucedemo.com/ u maksimiziranom prozoru
    def go_to(self, url):
        self.driver.get(url)
        self.driver.maximize_window() 

    # 2. Popuni "Username" polje korištenjem sljedećih vrijednosti - Korisničko ime: standard_user
    # 2. Popuni "Password" polje korištenjem sljedećih vrijednosti - Password: secret_sauce
    # 3. Klikni "LOGIN" dugme
    def login(self, username, password):
        self.wait 
        username_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
        username_polje.clear()
        username_polje.click()
        username_polje.send_keys(username)
        password_polje = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        password_polje.clear()
        password_polje.click()
        password_polje.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()      

    # 4. Verifikuj da se nalaziš na "PRODUCTS" web stranici
    def get_products_text(self):
        welcome_element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        return welcome_element.text 

    # 5. Klikni "ADD TO CART" dugme za dva različita proizvoda (po ličnom izboru)
    def add_to_cart(self):
        self.wait
        button1 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        button1.click() 
        button2 = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")))
        button2.click() 

    # 6. Klikni ikonu košarice u gornjem desnom uglu
        self.driver.find_element(By.ID, "shopping_cart_container").click()

    # 7. Verifikuj da se nalaziš na "YOUR CART" web stranici
    def your_cart_text(self):
        your_cart_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Your Cart']")))
        return your_cart_page.text

    # 8. Korištenjem imena prethodno dodanih proizvoda verifikuj da se isti nalaze u košarici
    def item_name_text(self, xpath):
        cart_page_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        return cart_page_title.text

    # 9. Klikni "CHECKOUT" dugme
    def checkout_page (self):
        self.driver.find_element(By.ID, "checkout").click()

    # 10. Verifikuj da se nalaziš na "CHECKOUT: YOUR INFORMATION" web stranici
    def checkout_page_text (self):
        checkout_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Checkout: Your Information']")))
        return checkout_text.text 

    # 11. Popuni sva polja na "CHECKOUT: YOUR INFORMATION" web stranici
    def checkout_information (self, name, surname, zipcode):
        self.wait
        first_name = self.driver.find_element(By.ID, "first-name")
        first_name.click()
        first_name.clear()
        first_name.send_keys("Azra") 

        last_name = self.driver.find_element(By.ID, "last-name")
        last_name.click()
        last_name.clear()
        last_name.send_keys("Rizvanovic") 

        postal_code = self.driver.find_element(By.ID, "postal-code")
        postal_code.click()
        postal_code.clear()
        postal_code.send_keys("71000") 
    
    # 12. Klikni "CONTINUE" dugme
        self.driver.find_element(By.ID, "continue").click()

    # 13. Verifikuj da se nalaziš na "CHECKOUT: OVERVIEW" web stranici
    def overview_page (self):
       overview_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Checkout: Overview']")))
       return overview_text.text  

    # 14. Korištenjem imena prethodno dodanih proizvoda verifikuj da se isti nalaze na "CHECKOUT: OVERVIEW" web stranici
    def product1_check (self, xpath):
        product1_checkout = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Sauce Labs Bolt T-Shirt']")))
        return product1_checkout.text  
    def product2_check (self, xpath):
        product2_checkout = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Test.allTheThings() T-Shirt (Red)']")))
        return product2_checkout.text  
    
    # 15. Klikni "FINISH" dugme na "CHECKOUT: OVERVIEW" web stranici
    def get_finish(self):
       self.driver.find_element(By.ID, "finish").click()

    # 16. Verifikuj da se nalaziš na "CHECKOUT: COMPLETE!" web stranici
    def checkout_complete_page (self):
        complete_page = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Checkout: Complete!']")))
        return complete_page.text    

    # 17. Klikni na ikonu izbornika u gornjem lijevom uglu
    def get_menu(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    
    # 18. Kada se izbornik učita, klikni "LOGOUT" link u izborniku
    def logout_page (self):
       logout_button = self.wait.until(EC.element_to_be_clickable ((By.ID, "logout_sidebar_link")))
       logout_button.click() 

    # 19. Verifikuj da se nalaziš na "LOGIN" stranici
       self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    