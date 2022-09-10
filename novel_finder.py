# A simple command line python program to search for webnovels on the website https://novelfull.com
# How to use the program => Type the following in the command line: python novel_finder.py [webnovel name]
# The program will open the index page of the searched webnovel

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys

driver = webdriver.Chrome()

# Sets the name of the website to visit
site = "https://novelfull.com"

# Get name of webnovel
arg_list = []
for n in range(1, len(sys.argv)):
  arg_list.append(sys.argv[n])
novel_name = " ".join(arg_list)

# Visits the site
driver.get(site)
print("Visiting {}...".format(site))

# Enter the name of novel to search
search_element = driver.find_element(By.ID, "search-input")
search_element.clear()  # Clears the entry field
search_element.send_keys(novel_name)

# Clicks Search button
search_button = driver.find_element(By.CLASS_NAME, "glyphicon-search")
search_button.click()
print("Now searching for the webnovel: '{}'...".format(novel_name))

# Clicks Novel title
novel_title = driver.find_element(By.CLASS_NAME, "truyen-title")
novel_title.click()
print("Going to the index of the webnovel '{}'".format(novel_name))