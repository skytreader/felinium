from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:16981/plain_select.html")
    pet_select = Select(driver.find_element_by_id("pets"))
    time.sleep(3)
    pet_select.select_by_visible_text("Embrr")
    time.sleep(3)
    driver.close()
