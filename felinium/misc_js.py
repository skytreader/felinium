from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:18000")
    driver.execute_script("alert('iminurbr0ws3rz')")
    time.sleep(3)
    # driver.switch_to_alert().accept()
    # time.sleep(1)
    driver.close()
