from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:16981/multielements.html")
    clowns = driver.find_element_by_class_name("clown")
    time.sleep(3)
    clowns.send_keys("haha")
    time.sleep(3)
    driver.close()
