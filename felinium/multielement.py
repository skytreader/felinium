from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.kalibrr.com/employers/signup")
    driver.find_element_by_class_name("navbar-footer-nav").click()
    time.sleep(3)
    driver.close()
