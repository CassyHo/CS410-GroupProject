import numpy as np
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
# from mysutils.text import remove_urls
from nltk.stem import SnowballStemmer
# from string import punctuation
import re
from rank import Ranker

# initialize NLTK components
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

# specify the path to the file
data_path = "cw.txt"

# Read and preprocess Campuswire posts crawled from the text file cw.txt
# Format: [PostID, Category, Title, Content, Likes]
def read_data(filepath):
    post_file = open(filepath, "r+", encoding="utf-8")
    post = post_file.readlines()
    for i in range(len(post)):
        # not working for my env, comment out for now
        # post[i] = remove_urls(post[i]).rstrip('\n') 
        post[i] = re.sub(r"http\S+", "", post[i]).rstrip('\n')
    post = np.array(post).reshape(-1, 5)
    return post


# remove non-English words and stop words
def clean_data(txt, is_stem=False):

    # replace any digit, non-alphabetic found in txt with an empty string and convert to lower case
    txt = re.sub('[0-9]', '', txt)
    txt = txt.lower()
    txt = re.sub('[^a-zA-Z]', ' ', txt)

    # tokenize words
    word_tokens = word_tokenize(txt)

    # apply stemming and remove stop words
    if is_stem:
        filtered_word = [stemmer.stem(w) for w in word_tokens if w not in stop_words]
    else:
        filtered_word = [w for w in word_tokens if w not in stop_words]
    return filtered_word


# filter the data whose category is 'General' for further categorization
def data_split(data):
    labeled = data[np.where(data != 'General')[0], :]
    unlabeled = data[np.where(data == 'General')[0], :]
    return labeled, unlabeled

