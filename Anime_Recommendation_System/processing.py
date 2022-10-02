import pandas as pd
from constants import *


class Processing:
    # Método de pré-processamento da base de dados para a visualização na interface
    @staticmethod
    def preprocessing_csv(dir):
        # Ler arquivo
        data = pd.read_csv(dir)

        # Índice
        data.index = data['id_anime']
        data.index.name = 'Id'

        # Selecionar colunas importantes e editar seus nomes
        data = data[['title', 'score']]
        data.columns = ['Titulo', 'Nota Geral']

        # Cópia auxiliar com os títulos padronizados em minúsculo
        data_aux = data.copy()
        data_aux['Titulo'] = data_aux['Titulo'].apply(lambda x: x.lower())

        return data, data_aux

    # Método para cálculo da similaridade utilizando a base de dados e a seleção do usuário
    @staticmethod
    def calculate_similarity(df_user):
        data = pd.read_csv(DATABASE_ANIMES_CSV)
        data['ID Anime'] = data['ID Anime'].apply(lambda x: int(x))

        # Tratamento base
        df_base = data.copy()
        df_base.index = df_base['ID Anime']
        df_base.drop(['ID Anime', 'Title', 'Score'], axis=1, inplace=True)

        # Tratamento dados do usuário
        df_user['ID Anime'] = df_user['ID Anime'].apply(lambda x: int(x))

        # Notas dadas pelo usuário
        user_score = pd.DataFrame(df_user['Score'], columns=['Score'])
        user_score.index = df_user['ID Anime'].copy()

        # Intersecção das linhas entre base e base do usuário
        df_user = df_base.loc[df_user['ID Anime']].copy()
        df_base.drop(df_user.index, axis=0, inplace=True)

        # Criação do dataframe de resultados da similaridade
        df_results = pd.DataFrame(
            columns=['Weighted Similarity'], index=df_base.index)

        # Execução do método de Jaccard
        index_base = df_base.index.tolist()
        index_user = df_user.index.tolist()
        denominator = user_score['Score'].sum()

        for ib in index_base:
            nominator = 0
            for iu in index_user:
                similarity = Processing.jaccard_binary(
                    df_user.loc[iu], df_base.loc[ib])
                nominator += similarity * float(user_score.loc[iu])
            df_results.loc[ib, 'Weighted Similarity'] = round(
                nominator/denominator, 2)

        # Resultados
        data_temp = data.copy()
        data_temp.index = data_temp['ID Anime']
        data_temp = data_temp[['Title', 'Score']]

        df_results = pd.merge(df_results, data_temp,
                              left_index=True, right_index=True)
        df_results = df_results[['Title', 'Score', 'Weighted Similarity']]
        df_results = df_results.sort_values(
            by=['Weighted Similarity', 'Score'], ascending=False)
        df_results.to_csv(OUTPUT_CSV, sep=',')

    # Método de Jaccard
    @staticmethod
    def jaccard_binary(x, y):
        m01 = 0
        m10 = 0
        m11 = 0

        for i, j in zip(x, y):
            if i == 1:
                if j == 1:
                    m11 += 1
                else:
                    m10 += 1
            elif j == 1:
                m01 += 1

        return m11 / (m01 + m10 + m11)
