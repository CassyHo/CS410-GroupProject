import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import config

# account credentials for Campuswire
username = config.username
password = config.password

# max time for element to load
response_time = 180

# CS410 Campuswire url
CS410_Channel = "https://campuswire.com/c/G4A2F7542/feed"

# Web crawler for web scraping
class WebCrawler:

    def __init__(self):
        desired_cap = {}
        # determine which operating system
        if sys.platform == "win32":
            self.browser = webdriver.Edge('Drivers/msedgedriver.exe', capabilities=desired_cap)
        elif sys.platform == "darwin":
            # Use this line if you are using Edge
            self.browser = webdriver.Edge('Drivers/msedgedriver', capabilities=desired_cap)
            
            # Use this line if you are using Chrome
            # self.browser = webdriver.Chrome()

    # set up the browser and login
    def set_up(self):
        # browser = webdriver.Edge() 
        # comment the below two lines and uncomment the above if not using Mac
        self.browser.get("https://campuswire.com/signin")
        email = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/div/div[2]/form/div/input[1]')
        pwd = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/div/div[2]/form/div/input[2]')
        login_btn = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/div/div[2]/form/button')

        # fill in the email and password and click login
        email.send_keys(username)
        pwd.send_keys(password)
        login_btn.click()

    def scrap_page(self):
        # wait for the element to load
        WebDriverWait(self.browser, response_time).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="wrapper"]/aside[2]/div[1]/div/h6')))

        # get the CS410 channel page
        self.browser.get(CS410_Channel)

        # wait for the element to load
        WebDriverWait(self.browser, response_time).until(expected_conditions.presence_of_element_located(
            (By.XPATH, '//*[@id="wrapper"]/aside[2]/div[3]/div[2]/div[4]/div[2]/div[1]/h3')))

        # open a file for writing the scraped content
        file = open("cw.txt", "w", encoding='utf-8')

        # loop through a fixed number of posts
        for i in range(0, 100):
            xpath = '//*[@id="wrapper"]/aside[2]/div[3]/div[2]/div[' + str(i + 4) + ']'
            WebDriverWait(self.browser, response_time).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
            xpath_no = xpath + '/div[2]/div[1]/span'
            xpath_title = xpath + '/div[2]/div[1]/h3'
            xpath_content = xpath + '/div[2]/div[2]'
            xpath_cater = '//*[@id="wrapper"]/div[4]/div/div/div[1]/div[2]/div[1]/span'
            xpath_likes = xpath + '/div[2]/div[3]/div[1]/span'
            # xpath_top_answer = '*[@id="wrapper"]/div[4]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div/p'
            # xpath_top_answer_likes = '//*[@id="wrapper"]/div[4]/div/div/div[2]/div[2]/div[2]/div[1]/div[3]'

            try:
                # extract info from each post
                number = self.browser.find_element(By.XPATH, xpath_no)
                title = self.browser.find_element(By.XPATH, xpath_title)
                content = self.browser.find_element(By.XPATH, xpath_content)
                title.click()
                WebDriverWait(self.browser, response_time).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_cater)))
                cater = self.browser.find_element(By.XPATH, xpath_cater)
                likes = self.browser.find_element(By.XPATH, xpath_likes)
                # top_answer = self.browser.find_element(By.XPATH, xpath_top_answer)
                # top_answer_likes = self.browser.find_element(By.XPATH, xpath_top_answer_likes)

            # continue if no such element
            except NoSuchElementException:
                continue

            # ensure the title element is scrolled into view on the browser
            self.browser.execute_script("arguments[0].scrollIntoView();", title)

            # write post information to file
            try:
                file.write(number.text[1:] + '\n' + cater.text + '\n' + title.text + '\n' + content.text + '\n'+ likes.text + '\n')

            # print the exception
            except Exception as e:
                print(e)

        # close the file
        file.close()
    
    def close(self):
        # close the browser
        self.browser.quit()


