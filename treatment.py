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


with open('m_treatment.txt') as f:
	URL_LIST = f.readlines()
	print URL_LIST

def get_random_entry(array):
	index = random.randrange(1,len(array)-1)
	return array[index]

def get_login_credentials(gender):
    '''returns (username, password)'''
    if (gender=='male'): #male
      return get_random_entry(MALE_CREDENTIALS)
    else: # female 
      return get_random_entry(FEMALE_CREDENTIALS)


# def get_site_file():
#    return get_random_entry(URL_LIST)
    

def find_gender(f_gender):
	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", False)
	profile.set_preference("browser.cache.memory.enable", False)
	profile.set_preference("browser.cache.offline.enable", False)
	profile.set_preference("network.http.use-cache", False) 
	#### can also set proxy, it's a good alternative to not be blocked
	browser =webdriver.Firefox(profile)
	
	[user_email, user_password] = get_login_credentials(f_gender)
	browser.get('http://gmail.com')

	emailElem = browser.find_element_by_id('identifierId')
	emailElem.send_keys(user_email)
	nextButton = browser.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]")
	nextButton.click()

	time.sleep(10)

	passwordElem = browser.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/span[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

	passwordElem.send_keys(user_password)

	signinButton = browser.find_element_by_css_selector('#passwordNext')
	signinButton.click()

	time.sleep(10)
	#########################################################################################################################################################################
	############# 	TREATMENT ##################
	#visit all websites
	# URL_LIST =["https://realpython.com/modern-web-automation-with-python-and-selenium/", "https://www.youtube.com/watch?v=XqvCNYEqy34"]

	# treatment used to define nature of the user
	for url in URL_LIST:
		print(url)
		browser.get(url)
	# ##########################################################################################################################################################################
	# ################# make searches in a location############################

	SEARCH_LIST=["starbucks","Taj Mahal", ""] 


	for term in SEARCH_LIST:
		browser.get('https://www.google.com/')
		time.sleep(10)

		search_box=browser.find_element_by_css_selector('div.a4bIc > input.gLFyf.gsfi:nth-child(3)')
		search_box.send_keys(term)
		# time.sleep(10)
		search_box.send_keys(Keys.ENTER)
		time.sleep(20)

		pyautogui.hotkey('ctrl', 's')
		time.sleep(5)
		pyautogui.typewrite("term")
		pyautogui.hotkey('enter')
		time.sleep(10)
		browser.delete_all_cookies()
		time.sleep(60)

find_gender('male')
