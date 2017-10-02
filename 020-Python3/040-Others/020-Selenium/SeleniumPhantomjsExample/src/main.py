import os, sys

from selenium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


driver = webdriver.PhantomJS()
driver.get("https://www.google.com/")
print(driver.current_url)
driver.quit()
