from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def fill_mailing_address_form(driver, user_details, state_name, print_message):
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
  print(print_message)


def save_form_and_continue(driver, print_message):
  save_and_continue = driver.find_element_by_xpath("//div/button[(text()='Save & Continue')]")
  save_and_continue.click()
  print(print_message)

def fake_wait(wait):
  try:
    elements = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Field col Adyen-cardNumber")))
    print(elements)
  except:
    print('Not found')


def fill_card_details(driver, identity, value, all_frames):
  for x in range(len(all_frames)):
    driver.switch_to.default_content()
    driver.switch_to.frame(all_frames[x])
    try:
      driver.find_element_by_id(identity).send_keys(value)
    except:
      print('Inner')


def place_order(print_message):
  place_order = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
  place_order.click()
  print(print_message)