from selenium import webdriver
import time

def alternate_approach(driver):
    link = driver.find_element_by_class_name("link-dotted")
    linky = link.get_attribute("href")
    driver.get(linky)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https:/www.kalibrr.com/job-board")
    alternate_approach(driver)
    #driver.find_element_by_class_name("link-dotted").click()
    #print driver.window_handles
    #for handle in driver.window_handles:
    #    driver.switch_to_window(handle)
    time.sleep(3)
    driver.close()
