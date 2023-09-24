import pandas as pd
import requests
from bs4 import BeautifulSoup
from numpy import NaN
from constants import *


class ScrapingAnimes:
    def __init__(self):
        self.START = 0
        self.END = 4150
        self.STEP = 50

    def get_animes_id(self):
        data = pd.DataFrame(columns=['id_anime'])

        for limit in range(self.START, self.END, self.STEP):
            # Comunicação com 50 animes do ranking por vez
            url = f'https://myanimelist.net/topanime.php?type=tv&limit={limit}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # Diminuir informações da página
            content = soup.find(id='content')
            trt = content.find_all('tr', class_='ranking-list')

            # Para cada anime encontrado na página será extraído o ID
            for element in trt:
                hi = element.find('div', class_='hoverinfo')
                id_anime = hi.get('id')
                id_anime = id_anime.replace('info', '')
                data.loc[len(data)] = id_anime
            print(f'===== [{limit} - {limit + self.STEP}] -> OK =====')

        # Salvar
        data.to_csv(ID_ANIMES_CSV, index=False, sep=',')

    def get_animes_info(self):
        # Importar ids
        data = pd.read_csv(ID_ANIMES_CSV)

        # Pegar informações dos animes do myanimelist através de cada ID
        data[['title', 'genres', 'score']] = NaN
        ids = data['id_anime'].values
        for id_anime in ids:
            # Requisições
            url = f'https://myanimelist.net/anime/{id_anime}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # Diminuir informações da página
            mal = soup.find(id='myanimelist')

            # Título
            title = mal.find('h1', class_='title-name h1_bold_none')
            title = title.text

            # Score
            score = mal.find('span', itemprop='ratingValue')
            score = score.text

            # Generos/Temas
            genres = mal.find_all('span', itemprop='genre')
            genres = [genre.text for genre in genres]

            # Atribuir informações ao dataframe
            data[data['id_anime'] == id_anime] = (
                id_anime, title, ','.join(genres), score)
            print(data[data['id_anime'] == id_anime].to_string(index=False))

        # Salvar
        data.to_csv(INFO_ANIMES_CSV, index=False, sep=',')

    def database_preprocessing(self):
        # Importação
        data = pd.read_csv(INFO_ANIMES_CSV)

        # Transformar colunas dos generos e temas
        data.dropna(inplace=True)

        df = data[['id_anime', 'title', 'score']].copy()
        df.columns = ['ID Anime', 'Title', 'Score']
        df.head()

        ids = data['id_anime'].values
        for id_anime in ids:
            genres = data[data['id_anime'] ==
                          id_anime]['genres'].values[0].split(',')
            for genre in genres:
                df.loc[df['ID Anime'] == id_anime, genre] = 1.0

        # Salvar
        df.fillna(0.0, inplace=True)
        df.to_csv(DATABASE_ANIMES_CSV, index=False, sep=',')
        print('===== Processo finalizado =====')
