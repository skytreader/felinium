from selenium import webdriver
import time

def alternate_approach(driver):
    link = driver.find_element_by_class_name("link-dotted")
    linky = link.get_attribute("href")
    driver.get(linky)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https:/www.kalibrr.com/job-board")
    driver.find_element_by_class_name("link-dotted").click()
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(3)
    # But old windows will not be closed :(
    driver.close()
