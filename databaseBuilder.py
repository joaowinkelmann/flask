import json
import sqlite3

with open('weather.json', encoding='utf-8-sig') as f:
    data = json.load(f)

conn = sqlite3.connect('weather.db')

# print(data)

# exemplo de registro:
    # {
    #   "temperature": "24.00",
    #   "humidity": "77.46",
    #   "dewpoint": "19.89",
    #   "pressure": "1011.72",
    #   "speed": "2.66", winkels.pythonanywhere.com. 
    #   "direction": "W",
    #   "datetime": "22-Jul-2021 13:54"
    # },

# Criando a tabela e as colunas
conn.execute('CREATE TABLE IF NOT EXISTS weather (temperature REAL, humidity REAL, dewpoint REAL, pressure REAL, speed REAL, direction TEXT, datetime TEXT)')

# Inserir os dados no banco
for item in data:
    conn.execute('INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)', (item['temperature'], item['humidity'], item['dewpoint'], item['pressure'], item['speed'], item['direction'], item['datetime']))

conn.commit()
conn.close()