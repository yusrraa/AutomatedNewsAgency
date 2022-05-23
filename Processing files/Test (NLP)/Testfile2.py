import pymysql
import numpy as np
import pandas as pd
import re
from bs4 import BeautifulSoup
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from tensorflow.python.keras.layers import Input, LSTM, Embedding, Dense, Concatenate, TimeDistributed, Bidirectional
from tensorflow.python.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping
import warnings

connection = pymysql.connect(host="localhost", user="root", passwd="newsagn", database="newsagn")
cursor = connection.cursor()
cursor.execute("select * from unprocesssed_scrape_data;")
scrapped_data = cursor.fetchall()
connection.close()
print(scrapped_data)