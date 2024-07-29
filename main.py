import requests
from bs4 import BeautifulSoup

# URL страницы, которую мы будем скрапить
url = "https://youtube.com"

# Отправка HTTP-запроса к странице
response = requests.get(url)

# Получение контента страницы
html_content = response.text

# Парсинг HTML-кода с помощью BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Извлечение заголовка страницы
title = soup.title.string

# Извлечение описания страницы из мета-тега
description_tag = soup.find("meta", attrs={"name": "description"})
description = description_tag["content"] if description_tag else "Описание не найдено"

# Вывод результатов
print(f"Заголовок: {title}")
print(f"Описание: {description}")