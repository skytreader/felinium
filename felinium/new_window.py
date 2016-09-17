from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https:/www.kalibrr.com/job-board")
    driver.find_element_by_class_name("link-dotted").click()
    print driver.window_handles
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
    time.sleep(3)
    driver.close()
