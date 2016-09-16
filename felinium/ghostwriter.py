from selenium import webdriver
import time

def fancy_ghostwriter(field):
    for c in "ghostwriter":
        field.send_keys(c)
        time.sleep(0.5)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.kalibrr.com")
    job_board_search_field = driver.find_element_by_class_name("jb-search-field")
    job_board_search_field.send_keys("ghostwriter")
    #fancy_ghostwriter(job_board_search_field)
    time.sleep(3)
    driver.close()
