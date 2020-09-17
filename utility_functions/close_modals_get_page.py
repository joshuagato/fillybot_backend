def close_modal(driver):
  error = True
  while error:
    try:
      close_button = driver.find_element_by_xpath("//div[@class='ReactModal__Overlay ReactModal__Overlay--after-open']")
      print('close_button', close_button)
    except:
      print('No modal')
      error = False


def close_stylish_modal(driver):
  error = True
  while error:
    try:
      close_stylish_modal_button = driver.find_element_by_xpath("//div[@class='bluecoreOverlay']")
      print('close_stylish_modal_button', close_stylish_modal_button)
    except:
      print('No Stylish modal')
      error = False


def close_stylish_modal2(driver):
  error = True
  while error:
    try:
      close_stylish_modal_button2 = driver.find_element_by_xpath("//div[@class='preScreenElement bluecoreCloseButton']")
      print('close_stylish_modal_button2', close_stylish_modal_button2)
    except:
      print('No Stylish modal2')
      error = False


def get_page_running_despite(driver):
  error = True
  while error:
    try:
      error_message = driver.find_element_by_xpath("//h1[text()='Access Denied']")
      print('error_message', error_message)
      if error_message:
        driver.refresh()
      else:
        error = False
        print('ELSE get page running despite...')
    except:
      error_message = ''
      error = False
      print('Continue get page running despite...')


def get_page_running(driver):
  error = True
  while error:
    try:
      error_message = driver.find_element_by_xpath("//h1[text()='429 Too Many Requests']")
      print('error_message', error_message)
      if error_message:
        driver.refresh()
      else:
        error = False
        print('ELSE get page running...')
    except:
      error_message = ''
      error = False
      print('Continue get page running...')