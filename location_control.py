import time, re                                                     # time.sleep, re.split
import sys                                                          # some prints
from selenium import webdriver                                      # for running the driver on websites
from datetime import datetime                                       # for tagging log with datetime
from selenium.webdriver.common.keys import Keys                     # to press keys on a webpage
from selenium.webdriver.support import expected_conditions as EC                   # to press keys on a webpage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
# import org.openqa.selenium.support.ui.WebDriverWait;
# import org.openqa.selenium.support.ui.ExpectedConditions;
import pyautogui
import random


# get login ids
def clean(s):
    toks = s.strip().split(' ')
    return toks

with open('FEMALE.txt') as f:
    FEMALE_CREDENTIALS = map(clean, f.readlines())
    # print FEMALE_CREDENTIALS

with open('MALE.txt') as f:
    MALE_CREDENTIALS = map(clean, f.readlines())


# with open('yoga.txt') as f:
# 	URL_LIST = f.readlines()
# 	print URL_LIST

def get_random_entry(array):
	index = random.randrange(1,len(array)-1)
	return array[index]

def get_login_credentials(gender):
    '''returns (username, password)'''
    if (gender=='male'): #male
      return get_random_entry(MALE_CREDENTIALS)
    else: # female 
      return get_random_entry(FEMALE_CREDENTIALS)

def find_gender(f_gender):
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False) 
	#### can also set proxy, it's a good alternative to not be blocked
	browser =webdriver.Firefox(profile)
	
	

	SEARCH_LIST=["monthly news highlights", "arvind kejriwal","raj thackery","b.s. yeddyurappa", "kashmiri pandits","kaveri river dispute","narendra modi","Chandrayan","Starbucks","schools near me", "gyms","jewellery","apartments","beyonce","best universities for social sciences", "data science jobs","gadgets","wework"]
	

	for term in SEARCH_LIST:
		browser.get('https://www.brightlocal.com/local-search-results-checker/')
		print('opened the link')
		print('entering serch term...............')
		s_box=browser.find_element_by_css_selector("#search-term")
		s_box.send_keys(term)
		print(term)
		print('entered search term')
		print('entering location.................')
		s_city=browser.find_element_by_css_selector('#search-location') ######################################################
		s_city.send_keys("Delhi")
		print('entered location')


		print('working on country................')

		country_box=browser.find_element_by_css_selector('#search-country')
		select = Select(country_box)
		print('waiting for dropdown')
		time.sleep(5)
		select.select_by_value('IN')
		#country_India=browser.find_element_by_xpath('/html[1]/body[1]/div[2]/section[1]/section[1]/article[1]/section[1]/div[1]/form[1]/div[3]/div[1]/select[1]/option[85]')
		time.sleep(5)
		button_green=browser.find_element_by_xpath('/html[1]/body[1]/div[2]/section[1]/section[1]/article[1]/section[1]/div[1]/form[1]/div[6]/div[1]/button[1]')
		button_green.click()
		time.sleep(20)

		print('getting first window handle')
		window_before=browser.window_handles[0]
		print(window_before)


		page_one=browser.find_element_by_css_selector('div.carousel-cell.is-selected:nth-child(1) > a:nth-child(1)')
		page_one.click()
		time.sleep(20)

		window_after=browser.window_handles[1]
		browser.switch_to_window(window_after)
		print(window_after)
		time.sleep(20)
		pyautogui.hotkey('ctrl', 's')
		time.sleep(10)
		pyautogui.typewrite(term+"_Delhi")
		pyautogui.hotkey('enter')
		time.sleep(50)
		print("............................................................................................................")
	browser.quit()



find_gender('female')
