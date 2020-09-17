from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def select_size(wait, size, print_message):
  size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))))
  size.click()
  print(print_message)


def add_to_cart(wait, print_message):
  addtocart = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='Button ProductDetails-form__action']")))
  addtocart.click()
  print(print_message)


def view_cart(wait, print_message):
  view_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-cart-added__cta']")))
  view_cart.click()
  print(print_message)


def check_out(wait, print_message):
  checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div/a[text()='Guest Checkout']")))
  checkout.click()
  print(print_message)