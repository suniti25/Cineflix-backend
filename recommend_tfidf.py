import pandas as pd
import numpy as np
import sqlite3 
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
connection = sqlite3.connect('movies_data.db')
#dfmovie= pd.read_csv('final_data.csv')
cur =connection.cursor()
tfv = TfidfVectorizer(min_df=3,max_features=None, strip_accents='unicode',analyzer='word',token_pattern=r'\w{1,}',ngram_range=(1,3),stop_words='english')
dfmovie = pd.read_sql_query("SELECT tags,original_title FROM movies_data", connection)
dfmovie['tags'].fillna(' ')
tfv_matrix= tfv.fit_transform(dfmovie['tags'])
# #compute sigmoid kernel
sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
indices = pd.Series(dfmovie.index, index= dfmovie['original_title']).drop_duplicates()
def give_rec(title, sig=sig):
     idx = indices[title]
     sig_scores = list(enumerate(sig[idx]))
     sig_scores = sorted(sig_scores, key= lambda x:x[1], reverse= True)
     sig_scores = sig_scores[1:11]
     print(sig_scores)
     movie_indices = [i[0] for i in sig_scores]
     return dfmovie['original_title'].iloc[movie_indices]
print(give_rec('Southpaw'))