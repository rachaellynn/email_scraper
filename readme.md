This is a python script that uses selenium, a headless browser, to crawl a website and scrape email
addresses off of that domain only. It does not cover subdomains or email addresses related to  external links.  

To run on your own machine, please do the following:

1. Make sure that you have Python 2.7 installed on your machine.

2. Clone this repository onto your local machine and cd into the directory.

3. Activate your virtual environment:
	$ source venn/bin/activate

4. Install the selenium and mechanize gems (if not already installed) and any other gems that your system
requires you to install when you run the script (you can check the requirements.txt file for more details). 

5. To run the script, type:
	$  python email_scrape.py http://www.example.com

	Please note that the url that you enter must be the complete url (as above)

6. The email addresses on the website should print out to the screen.


 
