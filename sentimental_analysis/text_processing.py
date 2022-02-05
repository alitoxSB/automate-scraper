from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np

def reader():
  df = pd.read_csv('data.csv')
  tweet_array = [df.tweet]
  """Read tweets and save in the txt file"""
  a_file = open("sentimental_analysis/tweets.txt", "w")

  for row in tweet_array:
    np.savetxt(a_file, row, fmt='%s')
  a_file.close()

def analysis():
  """Start the sentimental analysis of scrape tweets"""
  reader()
  analyzer = SentimentIntensityAnalyzer()
  pos_count = 0
  pos_correct = 0
  with open("sentimental_analysis/tweets.txt","r") as f:
    for line in f.read().split('\n'):
      vs = analyzer.polarity_scores(line)
      if vs['compound'] > 0:
        pos_correct += 1
        pos_count +=1

  neg_count = 0
  neg_correct = 0

  with open("sentimental_analysis/tweets.txt","r") as f:
    for line in f.read().split('\n'):
      vs = analyzer.polarity_scores(line)
      if vs['compound'] <= 0:
        neg_correct += 1
      neg_count +=1

  print("Precisión Positiva = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
  print("Precisión Negativa = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

def start_system():
  """Start system with sentimental analysis"""
  analysis()