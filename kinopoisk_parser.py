import requests
from bs4 import BeautifulSoup
import json

def parse_kinopoisk_movie(movie_title):
    url = f"https://www.kinopoisk.ru/index.php?kp_query={movie_title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        movie_info = {}
        
      
        movie_info['title'] = soup.find('h1', class_='moviename-big').text.strip()
        
    
        rating = soup.find('span', class_='rating_ball')
        movie_info['rating'] = rating.text if rating else 'Рейтинг не найден'
        
      
        description = soup.find('div', class_='brand_words')
        movie_info['description'] = description.text.strip() if description else 'Описание не найдено'
        
        return movie_info
    else:
        return None

movie_title = "Интерстеллар"  
movie_data = parse_kinopoisk_movie(movie_title)

if movie_data:
    print(json.dumps(movie_data, ensure_ascii=False, indent=4))
else:
    print("Фильм не найден")
