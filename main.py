import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL страницы, которую мы будем скрапить
url = "https://ww16.0123movie.net/list/movies.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Отправка HTTP-запроса к странице
response = requests.get(url, headers=headers)

# Take content
html_content = response.text

if response.status_code == 200:
    # Parsing HTML code with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    movie_cards = soup.find_all("div", class_="card h-100 border-0 shadow", limit=20)

    # List to hold movie data
    movies = []

    for card in movie_cards:
        #Name
        title_tag = card.find("h2", class_="card-title text-light fs-6 m-0")
        title = title_tag.text.strip() if title_tag else "No Name"
        #Link
        link_tag = card.find("a", class_="rounded poster")
        link = link_tag["href"] if link_tag else "No Link"

        movies.append({"Title": title, "Link": link})

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(movies)

    # Save the DataFrame to an Excel file
    df.to_excel("movies.xlsx", index=False)

else:
    print(f"Problem with access: {response.status_code}")
