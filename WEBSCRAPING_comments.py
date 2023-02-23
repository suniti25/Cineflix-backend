#!/usr/bin/env python
# coding: utf-8

# In[1]:


#scraping user reviews from imdb based on movie_id for sentiment analysis


# In[2]:


import requests
from bs4 import BeautifulSoup
from random import randint
import pandas as pd


# In[3]:


# url = 'https://www.imdb.com/title/tt0369610/reviews?ref_=tt_urv'
# response = requests.get(url)
# page = BeautifulSoup(response.content)
# reviews = page.findAll('div', attrs={'class':'text show-more__control'})
# clean_review=[]
# for review in reviews:
#     comment = review.get_text()
#     clean_review.append(comment)
# clean_review
print('hi')

# In[4]:


movies = pd.read_csv('clean.csv')


# In[12]:

import time
movies['imdb_id']= movies['imdb_id'].dropna()
movies_id = movies['imdb_id'].tolist()
#print(movies_id)

str = 'https://www.imdb.com/title/{}/reviews?ref_=tt_urv'
data = []
#counter =0
for movie in movies_id[2000:5000]:
    random_int = randint(1,5)
    print(movie)
    review_data={}
    # if counter == 500:
    #     time.sleep(random_int)
    #     print('hi')
    #     counter = 0
    url = str.format(movie)
    response = requests.get(url)
    page = BeautifulSoup(response.content,features="html.parser")
    reviews = page.findAll('div', attrs={'class':'text show-more__control'})
    clean_review=[]
    for review in reviews[:2]:
        comment = review.get_text()
        clean_review.append(comment)
    review_data['reviews'] = clean_review
    review_data['imdb_id'] = movie
    data.append(review_data)
    #counter += 1
data[15]
user_review_1000plus = pd.DataFrame(data)


user_review_1000plus.to_csv('2000-5000review.csv')


















# %%
