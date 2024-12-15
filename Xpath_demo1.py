from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.maximize_window()

#driver.get("https://www.amazon.de/")
driver.get("https://www.facebook.com/") #css selector

#Absolute  path
#driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/input[1]").send_keys("perfume women dior")
#driver.find_element(By.XPATH,"/html/body/div[1]/header/div[1]/div[4]/form/div[2]/div/input").click()

#Relative path
#driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("T-shirt")
#driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()

#or operator
#driver.find_element(By.XPATH,"//input[@placeholder='Search Amazon.de' or@id='twotabsearchtextbox']").send_keys("T-shirt")

#and operator
#driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button' and @type='submit']").click()


#unable to execute, not working
#contains() &  start-with()
#driver.find_element(By.XPATH,"//input[contains(@placeholder,'Search')]").send_keys("T-shirt")

#Text()
#driver.find_element(By.XPATH,"//a[text()='Music']").click()
#driver.find_element(By.XPATH,"//span[@class='hm-icon-label']").click()

# CSS Selector
#Tag and ID
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")

#tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("ABD")

#tag Attribute
driver.find_element(By.CSS_SELECTOR,"[Email address or phone number]").send_keys("abc")
