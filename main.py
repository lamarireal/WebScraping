import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы, которую будем скрапить
url = "https://ww16.0123movie.net/list/movies.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3"
}

# Отправка HTTP-запроса к странице
response = requests.get(url, headers=headers)

# Получение содержимого страницы
html_content = response.text

if response.status_code == 200:
    # Парсинг HTML-кода с помощью BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    movie_cards = soup.find_all("div", class_="card h-100 border-0 shadow", limit=20)

    # Список для хранения данных о фильмах
    movies = []

    for card in movie_cards:
        # Название
        title_tag = card.find("h2", class_="card-title text-light fs-6 m-0")
        title = title_tag.text.strip() if title_tag else "No Name"
        # Ссылка
        link_tag = card.find("a", class_="rounded poster")
        link = link_tag["href"] if link_tag else "No Link"

        movies.append({"Title": title, "Link": link})

    # Создание DataFrame из списка словарей
    df = pd.DataFrame(movies)

    # Сохранение DataFrame в файл Excel
    df.to_excel("Excel/movies.xlsx", index=False)

    # Сохранение DataFrame в CSV файл
    df.to_csv("csv/movies.csv", index=False)

else:
    print(f"Проблема с доступом: {response.status_code}")
