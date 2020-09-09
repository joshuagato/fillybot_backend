from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from flask import jsonify
import threading
import multiprocessing
from multiprocessing.dummy import Pool
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.keys import Keys

pool = Pool(10)

# header = randomheaders.LoadHeader()

proxies = {
  'http': '37.48.118.98:13012',
  'https': '37.48.118.98:13012',
}

# options = Options()
# options.add_argument("--headless")

# option = webdriver.ChromeOptions()
# option.add_argument('headless')

# options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=1400,1500")
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("start-maximized")
# options.add_argument("enable-automation")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-dev-shm-usage")


class Champssports:
  """docstring for Champssports."""

  def generate_url(self, product_details, user_details):
    product_name = product_details.get('product_name').lower().replace("'", '').replace(' ', '-').replace('_', '-')

    derived_url = 'https://www.champssports.com/product/' + product_name + '/' + product_details['product_number'] + '.html'
    product_size = product_details.get('product_size')
    product_quantity = product_details.get('product_quantity')

    product_summary = {
      'url': derived_url, 'size': product_size, 'quantity': product_quantity
    }

    # return self.get_product_page(product_summary, user_details)
    self.get_product_page(product_summary, user_details)

    # purchase = pool.apply_async(self.get_product_page, args=(product_summary, user_details))
    # return multiprocessing.cpu_count()


  def get_product_page(self, product_summary, user_details):
    # return_message = ''
    url = product_summary.get('url')
    size = product_summary.get('size')
    quantity = product_summary.get('quantity')
    state_name = user_details['state']

    # driver = webdriver.Chrome('./chromedriver.exe', options=options)

    # driver = webdriver.Chrome('./chromedriver.exe', options=option)
    # print('Chrome Initialized with options')

    driver = webdriver.Firefox()
    # driver = webdriver.Chrome('./chromedriver.exe')
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    print('Chrome Initialized')
    
    driver.get(url)
    print('Got Url')
    wait = WebDriverWait(driver, 40)
    print('Wait Initialized')

    def close_modal():
      try:
        close_button = driver.find_element_by_xpath("//div[@class='ReactModal__Overlay ReactModal__Overlay--after-open']")
        #close_button = driver.find_element_by_xpath("//button[@class='IconButton c-modal__close']")
        #close_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='IconButton c-modal__close']")))
        print('close_button', close_button)
      except:
        print('No modal')


    def close_stylish_modal():
      try:
        close_stylish_modal_button = driver.find_element_by_xpath("//div[@class='bluecoreOverlay']")
        #close_stylish_modal_button = driver.find_element_by_xpath("//button[@class='closeButtonGrey lastFocusableElement']")
        #close_stylish_modal_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='closeButtonGrey lastFocusableElement']")))
        print('close_stylish_modal_button', close_stylish_modal_button)
      except:
        print('No Stylish modal')



    def close_stylish_modal2():
      try:
        close_stylish_modal_button2 = driver.find_element_by_xpath("//div[@class='preScreenElement bluecoreCloseButton']")
        #close_stylish_modal_button2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='preScreenElement bluecoreCloseButton']")))
        print('close_stylish_modal_button2', close_stylish_modal_button2)
      except:
        print('No Stylish modal2')



    def get_page_running():
      try:
        error_message = driver.find_element_by_xpath("//h1[text()='429 Too Many Requests']")
        print('error_message', error_message)
        if error_message:
          driver.refresh()
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.XPATH, "//h2[text()='429 Too Many Requests']"))
      except:
        error_message = ''
        print('Continue...')

    def close_all_modals():
      for null in range(10):
        close_modal()
        close_stylish_modal()


    for null in range(10):
      get_page_running()


    # time.sleep(50)


    #driver.switch_to.default_content()
    #all_frames = driver.find_elements_by_tag_name('iframe')
    #print('Frames @ (Audio) Length', len(all_frames))


    close_all_modals()

    # size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='09.5']")))
    size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))))
    size.click()
    print('Size Selected')

    # qty = wait.until(EC.presence_of_element_located((By.ID, "input_tel_quantity")))
    # qty.send_keys(Keys.BACKSPACE)
    # qty.send_keys(quantity)
    # print('Quntity Typed')

    # close_all_modals()

    # try:
    #     size_again = driver.find_element_by_xpath.click("//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))
    #     size_again.click()
    #     print('Size Selected Again')
    # except:
    #     print('NO: Size Selected Again')


    close_all_modals()


    addtocart = driver.find_element_by_xpath("//button[@class='Button ProductDetails-form__action']")
    addtocart.click()
    print('Added to Cart')


    close_all_modals()


    view_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-cart-added__cta']")))
    view_cart.click()
    print('Cart Viewed')

    #time.sleep(5)


    close_all_modals()


    # checkout = driver.find_element_by_xpath("//div/a[text()='Guest Checkout']")
    checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div/a[text()='Guest Checkout']")))
    checkout.click()
    print('Checked Out')





    # user_details = {'first_name': 'Zerubabel', 'last_name': 'Baah', 'address': '2046 Nicklaus circle',
    # 'city': 'Roseville', 'state': 'California', 'zipcode': '95678', 'phone': '+16145564480',
    # 'email': 'lemuelzerubbabelbaah@gmail.com'
    # }

    # state_name = user_details['state']


    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).send_keys(user_details['first_name'])
    time.sleep(0.3)
    wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).send_keys(user_details['last_name'])
    time.sleep(0.3)
    driver.find_element_by_name('line1').send_keys(user_details['address_1'])
    time.sleep(0.3)
    driver.find_element_by_name('line2').send_keys(user_details['address_2'])
    time.sleep(0.3)
    driver.find_element_by_name('postalCode').send_keys(user_details['zipcode'])
    time.sleep(0.3)
    driver.find_element_by_name('town').send_keys(user_details['city'])
    time.sleep(0.3)
    state = driver.find_element_by_xpath("//select/option[(text()='{}')]".format(state_name))
    # state = driver.find_element_by_xpath("//select/option[contains(text(), '{}')]".format(state_name))
    state.click()
    time.sleep(0.3)
    driver.find_element_by_name('phone').send_keys(user_details['phone'])
    time.sleep(0.3)
    driver.find_element_by_name('email').send_keys(user_details['email'])
    time.sleep(0.3)
    print('Address Details Provided')

    close_all_modals()

    save_and_continue = driver.find_element_by_xpath("//div/button[(text()='Save & Continue')]")
    save_and_continue.click()
    print('Save and Continue Clicked')

    close_all_modals()

    # time.sleep(1)
    wait.until(EC.presence_of_element_located((By.ID, "encryptedExpiryMonth"))).send_keys(user_details['card_expiry'].split(' / ', 0))
    time.sleep(0.3)
    wait.until(EC.presence_of_element_located((By.ID, "encryptedCardNumber"))).send_keys(user_details['card_number'])
    time.sleep(0.3)
    driver.find_element_by_id('encryptedExpiryYear').send_keys(user_details['card_expiry'].split(' / ', 1))
    time.sleep(0.3)
    driver.find_element_by_id('encryptedSecurityCode').send_keys(user_details['card_cvv'])
    time.sleep(0.3)

    print('Review and Pay Clicked')

    place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
    place_order.click()

    print('Place Order Clicked')

    # review_and_pay = driver.find_element_by_xpath("//button/span[(text()='Review and Pay')]")
    # review_and_pay = wait.until(EC.presence_of_element_located((By.XPATH, "//button/span[(text()='Review and Pay')]")))
    # review_and_pay.click()
    time.sleep(3000)

    # time.sleep(0.3)
    # wait.until(EC.presence_of_element_located((By.NAME, 'card.cvv'))).send_keys(user_details['last_name'])
    #
    # addtobag = driver.find_element_by_xpath("//button[@class='gl-cta gl-cta--primary gl-cta--full-width']")
    # addtobag.click()
    # print('Added to Bag')

    # return return_message
    # return 'No Message'
