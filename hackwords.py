# -*- coding: utf_8 -*-
import pandas as pd
import sqlite3,random


mypath = "Files/"
df = pd.DataFrame()
connection = sqlite3.connect('words.db')
cursor = connection.cursor()
query="select word,frecuency,length(word) as len from hackword order by frecuency desc"
df = pd.read_sql_query(query,connection)

print(df.sort(["frecuency"],ascending=False))

for index,row in df.in