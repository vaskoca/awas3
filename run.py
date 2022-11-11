from pygooglenews import GoogleNews
import pandas as pd

gn = GoogleNews(lang='id', country='id)')
search = gn.search('banjir akibat hujan')

for i in search['entries']:
  print(i)
