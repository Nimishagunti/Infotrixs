
import sqlite3

def create_favorite_cities_table():
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS favorite_cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT UNIQUE
    )''')
    connection.commit()
    connection.close()



def add_favorite_city(city):
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()
    cursor.execute("INSERT OR IGNORE INTO favorite_cities (city) VALUES (?)", (city,))
    connection.commit()
    connection.close()

def get_favorite_cities():
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()
    cursor.execute("SELECT city FROM favorite_cities")
    cities = [row[0] for row in cursor.fetchall()]
    connection.close()
    return cities

def update_favorite_city(old_city, new_city):
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE favorite_cities SET city = ? WHERE city = ?", (new_city, old_city))
    connection.commit()
    connection.close()

def delete_favorite_city(city):
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM favorite_cities WHERE city = ?", (city,))
    connection.commit()
    connection.close()









if __name__ == "__main__":
    create_favorite_cities_table()
    while True:
        choice = input("Choose operation (1:Add, 2:List, 3:Update, 4:Delete, 5:Quit): ")
        if choice == '1':
            city = input("Enter a city to add: ")
            add_favorite_city(city)
        elif choice == '2':
            cities = get_favorite_cities()
            print("Favorite cities:")
            for idx, city in enumerate(cities, 1):
                print(f"{idx}. {city}")
        elif choice == '3':
            old_city = input("Enter the city to update: ")
            new_city = input("Enter the new city name: ")
            update_favorite_city(old_city, new_city)
        elif choice == '4':
            city = input("Enter a city to delete: ")
            delete_favorite_city(city)
        elif choice == '5':
            break
