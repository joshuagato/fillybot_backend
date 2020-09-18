def close_modal(driver):
  close_button = ''
  error = True
  while error:
    try:
      close_button = driver.find_element_by_xpath("//div[@class='ReactModal__Overlay ReactModal__Overlay--after-open']")
      print('close_button', close_button)
      if close_stylish_modal:
        error = False
      else:
        print('ELSE No modal')
    except:
      if not close_button:
        error = False

      print('No modal')


def close_stylish_modal(driver):
  close_stylish_modal_button = ''
  error = True
  while error:
    try:
      close_stylish_modal_button = driver.find_element_by_xpath("//div[@class='bluecoreOverlay']")
      print('close_stylish_modal_button', close_stylish_modal_button)
      if close_stylish_modal:
        error = False
      else:
        print('ELSE No Stylish modal')
    except:
      if not close_stylish_modal_button:
        error = False

      print('No Stylish modal')


def close_stylish_modal2(driver):
  error = True
  while error:
    try:
      close_stylish_modal_button2 = driver.find_element_by_xpath("//div[@class='preScreenElement bluecoreCloseButton']")
      print('close_stylish_modal_button2', close_stylish_modal_button2)
      if close_stylish_modal2:
        error = False
    except:
      print('No Stylish modal2')
      # error = False


def get_page_running_despite(driver):
  error = True
  error_message = ''
  while error:
    try:
      error_message = driver.find_element_by_xpath("//h1[text()='Access Denied']")
      print('error_message', error_message)
      if error_message:
        error_message = ''
        driver.refresh()
      else:
        error = False
        print('ELSE get page running despite...')
    except:
      if not error_message:
        error = False

      error_message = ''
      print('Continue get page running despite...')


def get_page_running(driver):
  error = True
  error_message = ''
  while error:
    try:
      error_message = driver.find_element_by_xpath("//h1[text()='429 Too Many Requests']")
      print('error_message', error_message)
      if error_message:
        error_message = ''
        driver.refresh()
      else:
        error = False
        print('ELSE get page running...')
    except:
      if not error_message:
        error = False

      error_message = ''
      print('Continue get page running...')