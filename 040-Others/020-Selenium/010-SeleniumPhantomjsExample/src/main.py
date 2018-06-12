import selenium.webdriver

driver = selenium.webdriver.PhantomJS("../phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.get("https://www.google.com/")
print(driver.current_url)
driver.quit()
