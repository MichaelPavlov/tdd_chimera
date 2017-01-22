from pyvirtualdisplay import Display
from selenium import webdriver

# display = Display()
# display.start()

browser = webdriver.Chrome()
browser.implicitly_wait(2)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

browser.quit()
# display.stop()
