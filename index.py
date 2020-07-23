from appium import webdriver
from capabilities import desiredCapabilities
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from stuff import stuffs


driver = webdriver.Remote("http://localhost:4723/wd/hub", desiredCapabilities)
driver.implicitly_wait(30)


def find_element_by_text(text):
    return driver.find_element_by_xpath("//*[@text='" + text + "']")


driver.get("https://unapec.edu.do")
driver.find_elements_by_class_name("navbar-toggler-icon").__getitem__(0).click()
driver.find_element_by_link_text("Aula virtual").click()
TouchAction(driver).press(x=1255, y=1908).move_to(x=1255, y=1330).release().perform()
driver.find_element_by_link_text("Ingresar aquí").click()
driver.find_element_by_id("i0116").send_keys(stuffs["stuff1"])
driver.find_element_by_id("idSIButton9").click()
sleep(2)
driver.find_element_by_id("i0118").send_keys(stuffs["stuff2"])
sleep(2)
driver.find_element_by_id("idSIButton9").click()
sleep(2)
driver.find_element_by_id("idBtn_Back").click()
driver.find_element_by_link_text("SISTEMAS BASADOS EN EL CONOCIMIENTO - INF328-43111-001").click()
driver.find_element_by_id("module-644979").click()



