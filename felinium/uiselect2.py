from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:18000/employers/signup")
    mobile_prefix_field = driver.find_element_by_class_name("select")
    mobile_prefix_field.click()
    driver.find_element_by_class_name("ui-select-search").send_keys("8")
    time.sleep(3)
    driver.close()
