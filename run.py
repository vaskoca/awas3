from pygooglenews import GoogleNews
from flask import Flask
from flask import Flask
from flask import Response
#from flask_ngrok import run_with_ngrok #hanya digunakan ketika menggunakan google colab dan tidak untuk di deploy ke heroku
import json
import pandas as pd

gn = GoogleNews(lang='id', country='id)')
search = gn.search('banjir akibat hujan')

articles = search['entries']
for i in articles:
  print(i.title)