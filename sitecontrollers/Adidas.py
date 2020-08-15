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

class Adidas:
    """docstring for Adisas."""
    def generate_url(self, product_details, user_details):
        product_name = product_details.get('product_name').lower().replace(' ', '-').replace('_', '-')
        # derived_url = 'https://www.eastbay.com/product/' + model_name + '/' + product_id + '.html'

        derived_url = 'https://www.adidas.com/us/' + product_name + '/' + product_details['product_number'] + '.html'
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

        # driver = webdriver.Chrome('./chromedriver.exe')
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        print('Chrome Initialized')
        driver.get(url)
        print('Got Url')
        wait = WebDriverWait(driver, 60)
        print('Wait Initialized')

        # selected_size = driver.find_element_by_xpath("//button[@class='gl-label size___2Jnft']/span[text()={}]".format(size))
        selected_size = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='gl-label size___2Jnft']/span[text()={}]".format(size))))
        selected_size.click()
        print('Size Selected')

        addtobag = driver.find_element_by_xpath("//button[@class='gl-cta gl-cta--primary gl-cta--full-width']")
        addtobag.click()
        print('Added to Bag')

        viewbag = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='gl-cta gl-cta--primary gl-cta--full-width gl-vspace']")))
        viewbag.click()
        print('Bag Viewed')

        quantity = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='gl-dropdown-custom__select-element']/option[text()={}]".format(quantity))))
        quantity.click()
        print('Quntity Selected')

        checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='checkout-actions__button-wrapper___cUBs-']")))
        checkout.click()
        print('Checked out')

        time.sleep(0.3)
        wait.until(EC.presence_of_element_located((By.NAME, 'firstName'))).send_keys(user_details['first_name'])
        time.sleep(0.3)
        wait.until(EC.presence_of_element_located((By.NAME, 'lastName'))).send_keys(user_details['last_name'])
        time.sleep(0.3)
        driver.find_element_by_name('address1').send_keys(user_details['address'])
        time.sleep(0.3)
        driver.find_element_by_name('city').send_keys(user_details['city'])
        time.sleep(0.3)
        state = driver.find_element_by_xpath("//select/option[(text()='{}')]".format(state_name))
        # state = driver.find_element_by_xpath("//select/option[contains(text(), '{}')]".format(state_name))
        state.click()
        time.sleep(0.3)
        driver.find_element_by_name('zipcode').send_keys(user_details['zipcode'])
        time.sleep(0.3)
        driver.find_element_by_name('phoneNumber').send_keys(user_details['phone'])
        time.sleep(0.3)
        driver.find_element_by_name('emailAddress').send_keys(user_details['email'])
        time.sleep(0.3)
        print('The End')
        review_and_pay = driver.find_element_by_xpath("//button/span[(text()='Review and Pay')]")
        review_and_pay.click()

        time.sleep(300)

        # return return_message
        # return 'No Message'
