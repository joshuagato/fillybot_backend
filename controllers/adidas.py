from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from flask import jsonify
import threading
import multiprocessing
from multiprocessing.dummy import Pool

pool = Pool(10)

# header = randomheaders.LoadHeader()

proxies = {
  'http': '37.48.118.98:13012',
  'https': '37.48.118.98:13012',
}


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

        driver = webdriver.Chrome('./chromedriver.exe')
        driver.get(url)
        wait = WebDriverWait(driver, 30)

        # sizes = driver.find_elements_by_xpath("//button[@class='gl-label size___2Jnft']")
        # sizes_list = []
        # for size in sizes:
        #     sizes_list.append(size.text)
        # print('sizes_list', sizes_list)
        # time.sleep(0.3)

        # if driver.find_element_by_xpath("//div[@class='scarcity-message___XH8G2']"):
        #     scarcity_message = driver.find_element_by_xpath("//div[@class='scarcity-message___XH8G2']")
        #     return_message = 'Scarcity_Message: ' + scarcity_message.text
        # else:
        #     return_message = 'Scarcity_Message: No Message'

        selected_size = driver.find_element_by_xpath("//button[@class='gl-label size___2Jnft']/span[text()={}]".format(size))
        selected_size.click()

        addtobag = driver.find_element_by_xpath("//button[@class='gl-cta gl-cta--primary gl-cta--full-width']")
        addtobag.click()

        viewbag = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='gl-cta gl-cta--primary gl-cta--full-width gl-vspace']")))
        viewbag.click()

        quantity = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='gl-dropdown-custom__select-element']/option[text()={}]".format(quantity))))
        quantity.click()

        checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='checkout-actions__button-wrapper___cUBs-']")))
        checkout.click()

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

        # review_and_pay = driver.find_element_by_xpath("//div[@class='col-m-12 col-s-12 gl-vspace-bpall-medium']")
        # review_and_pay = driver.find_element_by_xpath("//button[@class='gl-cta gl-cta--primary gl-cta--full-width']")
        review_and_pay = driver.find_element_by_xpath("//span[@class='gl-cta__content']")

        review_and_pay.click()
        time.sleep(300)

        # return return_message
        # return 'No Message'


    def checkout(self, driver):
        thread = threading.Thread(target=self.provide_size)
        thread.start

      # thread.join()
        while product_size is None:
            time.sleep(15)

        driver.find_element_by_xpath('//button/span[contains(text(), product_size)]').click()

        if driver.find_element_by_xpath("//div[@class='scarcity-message___XH8G2']"):
            scarcity_message = driver.find_element_by_xpath("//div[@class='scarcity-message___XH8G2']")
            print('Scarcity_Message: ', scarcity_message.text)
        else:
            print('Scarcity_Message: ', 'No Message')


    def provide_size(self, size):
        # self.product_size = size
        global product_size
        product_size = size

        return product_size


    def check_stock(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            'Chrome/83.0.4103.116 Safari/537.36'}
        # res = requests.get(url, headers=header)
        res = requests.get(url, headers=headers)
        # res = requests.get(url, headers=headers, proxies=proxies)
        page = BeautifulSoup(res.text, 'html.parser')
        list_of_sizes_raw = page.find_all('span', class_='c-form-label-content')
        for size in list_of_sizes_raw:
            if size == 'Qty*':
                break
            print(size.text)


    def start(self, model_name, product_id):
        url = generate_url(model_name, product_id)
        check_stock(url)
