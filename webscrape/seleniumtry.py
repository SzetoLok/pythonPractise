from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://szetolok.github.io/")

title = driver.title

driver.implicitly_wait(1.5)

text_box = driver.find_elements(by=By.XPATH, value="/html/body/section[1]/div[1]/h1")

print(text_box[0].text)
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text

# driver.quit()