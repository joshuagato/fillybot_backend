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


class Footlocker:
  """docstring for Footlocker."""

  def generate_url(self, product_details, user_details):
    product_name = product_details.get('product_name').lower().replace("'", '').replace(' ', '-').replace('_', '-')

    derived_url = 'https://www.footlocker.com/product/' + product_name + '/' + product_details['product_number'] + '.html'
    product_size = product_details.get('product_size')
    product_quantity = product_details.get('product_quantity')

    product_summary = {
      'url': derived_url, 'size': product_size, 'quantity': product_quantity
    }

    return self.get_product_page(product_summary, user_details)
    # self.get_product_page(product_summary, user_details)
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
    wait = WebDriverWait(driver, 20)
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
    

    def get_page_running_despite():
      try:
        error_message = driver.find_element_by_xpath("//h1[text()='Access Denied']")
        print('error_message', error_message)
        if error_message:
          driver.refresh()
        #WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.XPATH, "//h2[text()='429 Too Many Requests']"))
      except:
        error_message = ''
        print('Continue...')


    def close_all_modals():
      for null in range(30):
        close_modal()
        close_stylish_modal()


    def force_page_to_run():
      for null in range(30):
        get_page_running()
        get_page_running_despite()


    force_page_to_run()
    close_all_modals()


    # size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='09.5']")))
    size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))))
    size.click()
    print('Size Selected')

    close_all_modals()

    # addtocart = driver.find_element_by_xpath("//button[@class='Button ProductDetails-form__action']")
    addtocart = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='Button ProductDetails-form__action']")))
    addtocart.click()
    print('Added to Cart')

    force_page_to_run()
    close_all_modals()


    view_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-cart-added__cta']")))
    view_cart.click()
    print('Cart Viewed')    
    
    close_all_modals()
    
    # checkout = driver.find_element_by_xpath("//div/a[text()='Guest Checkout']")
    checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div/a[text()='Guest Checkout']")))
    checkout.click()
    print('Checked Out')    
    
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
    driver.find_element_by_xpath("//select/option[(text()='{}')]".format(state_name))
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
    
    try:
      elements = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Field col Adyen-cardNumber")))
      print(elements)
    except:
      print('Not found')
      
    driver.switch_to.default_content()
    all_frames = driver.find_elements_by_tag_name('iframe')

    def fill_card_details(identity, value):
      for x in range(len(all_frames)):
        driver.switch_to.default_content()
        driver.switch_to.frame(all_frames[x])
        try:
          driver.find_element_by_id(identity).send_keys(value)
        except:
          print('Inner')

    fill_card_details('encryptedCardNumber', user_details['card_number'])
    fill_card_details('encryptedExpiryMonth', user_details['card_expiry'].split(' / ', 1)[0])
    fill_card_details('encryptedExpiryYear', user_details['card_expiry'].split(' / ', 1)[1])
    fill_card_details('encryptedSecurityCode', user_details['card_cvv'])

    # place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
    # place_order.click()
    # print('Place Order Clicked')
    # time.sleep(3000)
    return {'success': True, 'message': 'Ordered'}
