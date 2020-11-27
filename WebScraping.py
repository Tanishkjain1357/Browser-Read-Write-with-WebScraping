# By Tanishk Jain and Ameya Jain

from selenium import webdriver
import time
import numpy
import pandas as pd

# fields = ['HELLO']
# file = pd.read_csv(r'C:\Users\Tanishk\Desktop\WebWork\edgedriver_win64\AllValues1.csv',delimiter=',',skipinitialspace=True, usecols=fields)
# file = pd.Series(file['HELLO'])
# # data = file.toArray()
# print(file[129])
# for x in file:
# 	print(x)

print("Hello world")
browser = webdriver.Edge("./msedgedriver.exe")
browser.get("https://webwork.math.umass.edu/webwork2/F20_STAT_515_3")
browser.find_element_by_id("uname").send_keys("username")
browser.find_element_by_id("pswd").send_keys("password")
browser.find_element_by_id("none").click()

browser.find_element_by_link_text("Review").click()
elem = browser.find_element_by_link_text("Problem 10").click()



for value in range(0, 4):
	ans1 = browser.find_elements_by_id("AnSwEr0001")
	ans1[value].click()
	for vals in range(0, 4):
		ans2 = browser.find_elements_by_id("AnSwEr0002")
		print(ans1[value].get_attribute("value"), ans2[vals].get_attribute("value"))
		ans2[vals].click()
		browser.find_element_by_id("submitAnswers_id").click()
		time.sleep(2)
		# text = "At least one of the answers above is NOT correct."
		# if(text not in browser.page_source):
		# 	print("TRUEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
		# 	break



######################################################################################################################################################
# for i in range(131, 170):
# for i in numpy.arange(0, 1.00, .01):
# 	browser.find_element_by_id("AnSwEr0001").clear()
# 	res = i
# 	browser.find_element_by_id("AnSwEr0001").send_keys(str(res))
# 	browser.find_element_by_id("submitAnswers_id").click()
# 	elem = browser.find_element_by_link_text("incorrect").text
# 	if(elem != "incorrect"):
# 		break
	# break

# <span class="ResultsWithError ResultsWithErrorInResultsTable">incorrect</span>

######################################################################################################################################################