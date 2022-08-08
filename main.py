from selenium import webdriver
from selenium.webdriver.common.by import By


# click accept cookies button
def accept_cookies():
    cookie_window = driver.find_element(by=By.ID, value="ensCloseBanner")
    cookie_window.click()
    driver.implicitly_wait(3)


driver = webdriver.Safari()
driver.get("https://www.vueling.com/en")

accept_cookies()

driver.implicitly_wait(3)

driver.quit()
