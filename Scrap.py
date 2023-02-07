from serpapi import GoogleSearch
import csv
import sqlite3
import pandas as pd
from openai import Engine
import pyttsx3 
engine = pyttsx3.init() 

# Sending api request
params = {
  "engine": "google_maps",
  "q": "pizza",
  "ll": "@40.7455096,-74.0083012,15.1z",
  "type": "search",
  "api_key": "2c8412f6dcffad48eefb445b95239a3d5aa60bbe811de7ee3eca083f4d8de283"   #api key
}

search = GoogleSearch(params)
results = search.get_dict()
local_results = results["local_results"]


# fetching data from the api
for  res in local_results:
  print(res)
  print("\n")
print(type(local_results[0]))


# converting the json data to data frame
df = pd.DataFrame(local_results) 

# convert dataframe to csv
df.to_csv('scrap.csv', index=False)

# Read the data from the csv filr
with open('scrap.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file) 

    next(csv_reader) 

    max_rating = '0'

# calculate the maximum rating from  csv file 
    for row in csv_reader: 
        rating = row[9]

        if rating > max_rating: 
            max_rating = rating

    
    csv_file.seek(0) 
    next(csv_reader)  
# print the maximum piza shops having maximum ratings
    for row in csv_reader: 
        if row[9] == max_rating: 
            print(row)
            # engine = pyttsx3.init() 
            engine.say(row[1]) 
            engine.runAndWait()

