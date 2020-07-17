from appium import webdriver
from capabilities import desiredCapabilities


driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredCapabilities)
driver.implicitly_wait(30)
