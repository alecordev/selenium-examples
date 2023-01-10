import time
from selenium import webdriver
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

driver = webdriver.Ie(service=IEService(IEDriverManager().install()))
time.sleep(10)
driver.quit()
