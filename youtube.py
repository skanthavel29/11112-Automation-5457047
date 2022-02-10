import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = webdriver.Chrome ("/Users/sanushanak/Downloads/chromedriver-1")
chromedriver.get("https://www.youtube.com/")

def results(search_query, num_results=5):
    driver = chromedriver()
    driver.get(url)
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    assert len(search_results) >= 5, "Search results are less than 5"
    driver.close()