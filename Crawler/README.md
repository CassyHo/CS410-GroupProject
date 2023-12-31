# Crawler setup and usage guide
## Dependencies
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

## Configuration
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

## Run Crawler
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


## Resources
* [Flask doc](https://flask.palletsprojects.com/en/1.1.x/quickstart/)