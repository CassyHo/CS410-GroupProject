## Dependencies
My environment:
* Python 3.11.5
* flask                     2.2.2  
* selenium                  4.9.0
* numpy                     1.26.0
* nltk                      3.8.1

## Prerequisite
```python
import nltk
nltk.download()
```
Download punkt, stopwords

## Configuration
* Fill the account info in crawler.py
* Set environment variable in terminal `$env:FLASK_APP = "main.py"`

## Run
1. In the dictionary of **Crawler**, using `flask run` to run this application.
2. Click on http://127.0.0.1:5000, the browser is supposed to start and automatically sign in, transfer to CS410 channel, browse post and save to cw.txt file.
3. Enter http://127.0.0.1:5000/{keyword} in the browser, return all keyword-related posts according to rank.py.  


## Resources
* [Flask doc](https://flask.palletsprojects.com/en/1.1.x/quickstart/)


