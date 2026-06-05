import sqlite3
import pandas as pd

df = pd.read_csv('written_sessions.csv')
conn = sqlite3.connect('database.db')
df.to_sql('playtime_data', conn, if_exists='replace', index=False)
result = pd.read_sql('', conn)
conn.close()
