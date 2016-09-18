from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.kalibrr.com")
    driver.execute_script("alert('iminurbr0ws3rz')")
    time.sleep(3)
    # driver.switch_to_alert().accept()
    # time.sleep(1)
    driver.close()
