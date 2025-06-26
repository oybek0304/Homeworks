import json
import random
import requests

# ===== Task 1: JSON Parsing =====
def read_students(file_path):
    try:
        with open(file_path, 'r') as f:
            students = json.load(f)
            print("Student Details:")
            for student in students:
                print(f"Name: {student.get('name')}, Age: {student.get('age')}, Grade: {student.get('grade')}")
    except FileNotFoundError:
        print("students.json file not found.")


# ===== Task 2: Weather API =====
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print("Temperature:", data['main']['temp'], "°C")
        print("Humidity:", data['main']['humidity'], "%")
        print("Condition:", data['weather'][0]['description'])
    else:
        print("Failed to get weather data. Status code:", response.status_code)


# ===== Task 3: JSON Modification =====
def load_books(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except:
        return []

def save_books(file_path, books):
    with open(file_path, 'w') as f:
        json.dump(books, f, indent=4)

def add_book(file_path, book):
    books = load_books(file_path)
    books.append(book)
    save_books(file_path, books)
    print("Book added.")

def update_book(file_path, title, updated_info):
    books = load_books(file_path)
    for book in books:
        if book['title'].lower() == title.lower():
            book.update(updated_info)
            save_books(file_path, books)
            print("Book updated.")
            return
    print("Book not found.")

def delete_book(file_path, title):
    books = load_books(file_path)
    new_books = [book for book in books if book['title'].lower() != title.lower()]
    if len(new_books) != len(books):
        save_books(file_path, new_books)
        print("Book deleted.")
    else:
        print("Book not found.")


# ===== Task 4: Movie Recommendation System =====
def recommend_movie_by_genre(genre, api_key):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'Search' in data:
            movie = random.choice(data['Search'])
            print("Recommended Movie:")
            print("Title:", movie['Title'])
            print("Year:", movie['Year'])
        else:
            print("No movies found in that genre.")
    else:
        print("Failed to fetch movies.")

# ====== Example Usage (uncomment to run) ======
# read_students("students.json")
# get_weather("Tashkent", "your_openweather_api_key")
# add_book("books.json", {"title": "New Book", "author": "John", "year": 2023})
# update_book("books.json", "New Book", {"year": 2024})
# delete_book("books.json", "New Book")
# recommend_movie_by_genre("action", "your_omdb_api_key")
