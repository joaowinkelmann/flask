import sqlite3

class dbController:
    def insert(temperature, humidity, dewpoint, pressure, speed, direction, datetime):
        if (temperature == None or humidity == None or dewpoint == None or pressure == None or speed == None or direction == None or datetime == None):
            return False
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO weather VALUES (?, ?, ?, ?, ?, ?, ?)', (temperature, humidity, dewpoint, pressure, speed, direction, datetime))
        conn.commit()
        conn.close()
        return True

    def get():
        conn = sqlite3.connect('weather.db')
        cursor = conn.cursor()
        cursor.execute('SELECT [temperature], [humidity], [dewpoint], [pressure], [speed], [direction], [datetime] FROM weather')
        result = cursor.fetchall()
        conn.close()
        result = [dict(zip([key[0] for key in cursor.description], row)) for row in result]
        return result