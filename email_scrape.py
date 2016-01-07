def crawl_website():

	# spoof our browser so it looks like we're not a robot connecting to the website
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [('User-agent','Firefox')]
	browser = webdriver.Firefox()

	start_url = sys.argv[1] 
	new_url_list = []
	visited_url_list = []
	button_urls = []
	email_list = []
	new_url_list.append(start_url)

	while len(new_url_list) > 0:
		for item in new_url_list:
			browser.get(item) 
			
			emails = browser.find_elements_by_partial_link_text('@') 
			for email in emails:
				email_list.append(email.text)

			new_url_list.pop(0)
			visited_url_list.append(item)

			urls = browser.find_elements_by_tag_name('a') 
			other_urls = browser.find_elements_by_class_name('btn')
			urls = urls + other_urls
			
			for url in urls:
				link = url.get_attribute('href')
				
				#clean up the link
				if(str(link).startswith("/")): #makes incomplete links complete
					link = start_url + link
				link = str(link).split('#', 1)[0] #pulls out any anchor tags
				if(str(link).endswith('/')): #pulls out any end dashes
					link = link[:-1]	

				# adds link to the new list if appropriate
				if str(start_url) in str(link) and link not in visited_url_list and link not in new_url_list: 
					new_url_list.append(link)	

	email_list = set(email_list) #gets unique email addresses
	for unique_email in email_list:
		print unique_email

	browser.close()

if __name__ == '__main__':
	import mechanize
	import urllib2
	from selenium import webdriver
	import os
	import re
	import sys
	import pdb
	import argparse

crawl_website()






