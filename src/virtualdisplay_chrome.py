import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from pyvirtualdisplay import Display

display = Display(visible=0, size=(1920, 1080))
display.start()
driver = webdriver.Chrome(service=ChromeService('/usr/lib/chromium-browser/chromedriver'))
driver.get("http://rugbychampagneweb.com")
driver.save_screenshot("example.png")
driver.quit()
