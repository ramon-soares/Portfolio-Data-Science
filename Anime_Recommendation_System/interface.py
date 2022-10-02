# Bibliotecas
import streamlit as st
import pandas as pd
from processing import Processing
from PIL import Image
from constants import *


class Interface:
    # Método construtor
    def __init__(self, data, titles_lower):
        self.data = data
        self.titles_lower = titles_lower

        self.initialize()

    # Página de inicialização
    def initialize(self):
        # Configurações iniciais da página
        st.set_page_config(
            page_title='Sistema de recomendação de animes por similaridade', layout='wide')
        st.title('Sistema de recomendação de animes por similaridade')

        # Opção de reset
        if 'reset' in st.session_state and st.session_state.reset:
            st.session_state['user_df'] = pd.DataFrame(
                columns=['Title', 'Score'])

        # Primeira página para executar a interface (sumirá após click no botão)
        if 'user_df' not in st.session_state:
            # Texto descrição
            description_text = st.empty()
            description_text.markdown(
                'O sistema se baseia no coeficiente de Jaccard para o cálculo de similaridade \
                que é realizado através dos gêneros de cada anime. Tal medida de proximidade \
                pode ser usada para encontrar a similaridade entre dois vetores binários \
                assimétricos ou para encontrar a similaridade entre dois conjuntos.\n\n\
                ')

            # Imagem
            img = Image.open(HOME_SCREEN_IMAGE)
            image = st.empty()
            image.image(img)

            # Botão
            start_button = st.empty()
            start_button.button('Iniciar', key='start')

            # Verificação se houve click no botão para iniciar a página de execução
            if st.session_state['start']:
                st.session_state['user_df'] = pd.DataFrame(
                    columns=['Title', 'Score'])

                description_text.empty()
                image.empty()
                start_button.empty()

                self.interface_body()
        else:
            self.interface_body()

    # Página de execução
    def interface_body(self):
        # Container para seleção dos animes pelo usuário
        with st.container():
            st.header('Selecionar títulos')
            title = st.text_input('Pesquisar:', '', key='search_title').lower()
            col0, col1 = st.columns(2)

            with col0:
                st.dataframe(
                    self.data[self.titles_lower['Titulo'].str.contains(title)], width=480)

            with col1:
                tab0, tab1 = st.tabs(['Adicionar', 'Remover'])
                with tab0:
                    st.text_input('Adicionar título por ID:',
                                  value='', key='add_title')
                    if 'id_exists' in st.session_state and not st.session_state.id_exists:
                        st.error('Índice inválido!')

                    st.number_input('Nota:', value=6.0, step=0.5, min_value=0.0, max_value=10.0,
                                    key='score')

                    st.button('Adicionar', key='add_button',
                              on_click=self.add_row_user_df)

                with tab1:
                    st.text_input('Remover título por ID:', value='',
                                  key='del_title')
                    if 'id_exists' in st.session_state and not st.session_state['id_exists']:
                        st.error('Índice inválido!')
                        st.session_state['id_exists'] = True

                    st.button('Remover', key='del_button',
                              on_click=self.del_row_user_df)

        # Container da seleção dos animes do usuário
        with st.container():
            st.header('Seleção do usuário')

            st.dataframe(st.session_state['user_df'], width=480)

            # Calcular similaridade
            st.button('Calcular similaridade', key='calculate',
                      on_click=self.calculate_similarity_run)

            # Opção de reset
            st.button('Limpar tabela', key='reset')

        # Container do resultado gerado
        with st.container():
            st.header('Resultado')
            st.number_input('Número de resultados a ser mostrado:', value=10, step=5, min_value=1, max_value=100,
                            key='number_titles')

            if 'result_df' in st.session_state:
                st.dataframe(st.session_state['result_df'].iloc[0:st.session_state['number_titles']],
                             width=480)

    # Método relacionado a ação de inserir um título após o click do botão "Adicionar"
    def add_row_user_df(self):
        try:
            id = int(st.session_state['add_title'])
            title = self.data.loc[id, 'Titulo']
            score = float(st.session_state['score'])
            st.session_state['user_df'].loc[id] = [title, score]
            st.session_state['id_exists'] = True
        except:
            st.session_state['id_exists'] = False

    # Método relacionado a ação de remover um título após o click do botão "Remover"
    def del_row_user_df(self):
        try:
            id = int(st.session_state['del_title'])
            st.session_state['user_df'].drop(id, axis=0, inplace=True)
            st.session_state['id_exists'] = True
        except:
            st.session_state['id_exists'] = False

    # Método para cálculo da similaridade utilizando a base de dados e a seleção do usuário
    @staticmethod
    def calculate_similarity_run():
        try:
            user_df = st.session_state['user_df'].reset_index(names=[
                                                              'ID Anime'])
            Processing.calculate_similarity(user_df)
            st.session_state['result_df'] = pd.read_csv(OUTPUT_CSV)
        except:
            st.session_state['result_df'] = pd.DataFrame()
