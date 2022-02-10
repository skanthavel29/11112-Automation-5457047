import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = webdriver.Chrome ("/Users/sanushanak/Downloads/chromedriver-1")
chromedriver.get("https://www.google.com")

def results(search_query, num_results=10):
    driver = chromedriver()

    driver.get(url)
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    search_results = driver.find_elements_by_class_name("g")
    assert len(search_results) >= 10, "Search results are less than 10"
    driver.close()