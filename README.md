# Browser Extension for Campuswire
## Author
Group Name: Developer Team
| Name          | Email                 |
| ------------- |:---------------------:|
| Allan(Shengqi) Huang | shengqi5@illinois.edu |
| Chu-ching Ho  | cch11@illinois.edu    |
| Danmeng Zheng | danmeng2@illinois.edu |
| Zengjie Tang  | zengjie3@illinois.edu |

## Overview
Our team has chosen theme 1: Intelligent Browsing. We have improved a browser extension for searching Campuswire posts from the project of last year’s students. The link to the fall 2022 original project is here: https://github.com/tenkinoko/CourseProject. Our browser extension allows users to search Campuswire posts based on the keyword and see the top 5 relevant posts and the number of likes of that post. Clicking on the title of the post will take the users to the corresponding page. 

The search function in Campuswire only returns posts that match the keyword. However, the results are not ranked by their relevance to the query. The project of previous students improved the retrieval results to be the most relevant posts. However, the search results also don’t have other information like several likes or the exact date of the posts, which makes it difficult for the users to judge the usability of the posts. Furthermore, the codes of extension and crawler from the previous project did not work like what they showed in the demo. So we solved the crawler and extension malfunctions and we integrated additional information related to the posts with BM25 for more relevant retrieval results. We also improved the extension visibility and showed more information related to the posts for a better user experience.

## Tutorial Presentation
Link: https://mediaspace.illinois.edu/media/t/1_aqy9j3a4
## Setup(2 parts)
**NOTE:** Please see CS410 Project Documentation.pdf for more detailed explanation
## *Part 1*. Crawler setup and usage guide
### Dependencies
Environment:
* Python 3.11.5
* flask                     2.2.2  
* selenium                  4.9.0
* numpy                     1.26.0
* nltk                      3.8.1
```python
import nltk
nltk.download()
# Download punkt, stopwords
```

### Configuration
* Fill in the campuswire username and password in config.py
```python
# enter your Campuswire login
username = "xxx"
password = "xxx"
```

* Modify driver option in line 26-33 of crawler.py file in Crawler folder. The default is Edge.
```python
# determine which operating system
if sys.platform == "win32":
    # Use this line if you are using Edge
    self.browser = webdriver.Edge('Drivers/msedgedriver.exe', capabilities=desired_cap)

    # Use this line if you are using Chrome
    # self.browser = webdriver.Chrome('Drivers/chromedriver.exe')
elif sys.platform == "darwin":
    # Use this line if you are using Edge
    self.browser = webdriver.Edge('Drivers/msedgedriver', capabilities=desired_cap)
    
    # Use this line if you are using Chrome
    # self.browser = webdriver.Chrome()
```

* (Optional) In the line 65 of crawler.py file in Crawler folder, you can also change the number of most recent posts you’d like to scrape. The default is 100.
```python
# loop through a fixed number of posts
for i in range(0, 100):
```

### Run Crawler
1. Navigate to the **Crawler** folder
2. For mac, use this command `FLASK_APP=main.py flask run` to run the application.
```console
(base) dmz@DMZs-MBP crawler % FLASK_APP=main.py flask run
```
For windows, use these two commands `$env:FLASK_APP = "main.py"` and `flask run` to run the application.
```console
$env:FLASK_APP = "main.py"
flask run
```
3. Ctrl+Click or Simply click on http://127.0.0.1:5000, a new window of browser should automatically pop up, login and start scraping pages
4. To test if the scraping and ranking is successful, enter http://127.0.0.1:5000/{keyword} in the browser. It should return top 5 most relevant posts according to rank.py.  


### Resources
* [Flask doc](https://flask.palletsprojects.com/en/1.1.x/quickstart/)

## *Part 2*. Browser extension setup and usage guide
### Prerequisite
1. Crawler and ranker have successfully run
2. To test if the scraping and ranking is successful, enter http://127.0.0.1:5000/{keyword} in the browser. It should return top 5 most relevant posts

### Install browser extension
1. In your browser, go to **Extensions** -> **Manage Extensions** 
2. Turn on **Developer mode**
3. Click on **Load Unpacked** -> Navigate to the **Extension** folder and hit **Select**
4. **CamperaExt** should appear in **All Extensions**

### Use extension
1. Click the extension **CamperaExt**
2. Type keywords you’d like to search and hit the **Search** button
3. Click on the title of the post and the browser will open a tab to take you to the post. Login may be required before you can see the post

## Implementation
The browser extension CamperaExt is an application that facilitates the retrieval of related Campuswire posts based on user search queries. It consists of two main parts:
1. Crawler
    1. Text preprocessing and ranking:
        * Programming language: Python
        * Libraries: NLTK, re, NumPy
        * Description: These modules handle the preprocessing of the Campuswire posts and then implement the ranking algorithm using BM25 and              pivoted length normalization and IDF weighting. The sigmoid-normalized likes_count for each post is also integrated using                      weighting. 
    2. Web Crawler:
        * Programming language: Python
        * Libraries: Selenium
        * Description: The module is used for scraping posts from the CS410 class channel. It logs in to the Campuswire and navigates to the                  channel and retrieves the information from a fixed number of posts, now 20. The number can be changed if the user would like to                scrape more pages. The scraped information including PostID, Category, Title, Content, and Likes is stored in cw.txt.
    3. Flask:
        * Programming language: Python
        * Framework: Flask
        * Libraries: Selenium, NumPy, Flask, Flask-CORS
        * Description: The module creates a Flask web application and initializes the web scraping before the first request. It defines an API                 endpoint for retrieving the Campuswire posts. 
2. Chrome extension:
    * Programming language: HTML, CSS, Javascript
    * Description: The extension “CamperaExt” provides a user-friendly interface to interact with the search system. Users can input a                     keyword and click the search button, then the top five related posts are retrieved and displayed with clickable links and the                  number of likes.

**NOTE:** Please see the source code for a more detailed and step-by-step documentation.
