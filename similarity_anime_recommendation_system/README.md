# Introdução

O sistema se baseia no coeficiente de Jaccard para o cálculo de similaridade que é realizado através dos gêneros de cada anime. Tal medida de proximidade pode ser usada para encontrar a similaridade entre dois vetores binários assimétricos ou para encontrar a similaridade entre dois conjuntos.

Neste sistema, para chegar à conclusão de quais animes irão ser recomendados para o usuário, primeiro é utilizado o coeficiente de Jaccard entre cada título da base de dados e cada título escolhido pelo usuário. Então para cada título da base, é feito o cálculo de similaridade com cada anime que o usuário especificou, seguido do cálculo de uma média ponderada que considera como pesos as notas dadas pelo usuário para cada anime. O resultado é a similaridade em que um anime da base possui com TODA a base passada pelo usuário, ou seja, uma relação de 1 para todos.

O cálculo é feito para cada anime da base de dados e o resultado é mostrado inicialmente de maneira com que os títulos mais similares apareçam primeiro, e a quantidade a ser mostrada pode ser editada pelo usuário, sendo possível visualizar mais ou menos títulos de acordo com sua necessidade.

# Como a similaridade é calculada?

O sistema em questão utiliza os gêneros de cada anime como critério para o cálculo de similaridade. São usados vetores binários para o cálculo. Cada vetor representa todos os gêneros existentes (de acordo com a base de dados usada, que possui como fonte o site https://myanimelist.net). Todos os vetores possuem o mesmo tamanho e se comportam da seguinte forma: se os gêneros disponíveis são aventura, comédia e romance, para representar um título que possui somente os gêneros aventura e romance, o vetor seria (1, 0, 1); já para um título que é somente de comédia, o vetor seria (0, 1, 0), ou seja, se o título possui um determinado gênero, ele possui valor 1 no vetor, caso contrário possui o valor 0.

O cálculo é realizado da seguinte forma, considerando um objeto _i_ e um objeto _j_:

    a = o número de atributos que são iguais a 1 para ambos os objetos; 
    b = o número de atributos que são iguais a 0 para o objeto i, mas iguais a 1 para o objeto j;
    c = o número de atributos que são iguais a 1 para o objeto i, mas iguais a 0 para o objeto j.

Então, a similaridade de Jaccard para esses atributos é calculada pela seguinte equação:

$$J(i, j) = \frac{a}{a + b + c}$$

Dessa forma, considerando os vetores:

    V1 = (0, 1, 0, 0, 0, 1, 0, 0, 1)
    V2 = (0, 0, 1, 0, 0, 0, 0, 0, 1)

A similaridade é calculada da seguinte forma:

$$J(V1, V2) = \frac{a}{a + b + c} = \frac{1}{1 + 1 + 2} = 0.25$$

Desse modo, considerando um objeto _x_ da base de dados, três objetos _a_, _b_ e _c_ e as notas _n1_, _n2_ e _n3_ (relacionados aos objetos _a_, _b_ e _c_ respectivamente) dos títulos passados pelo usuário, o cálculo final da similaridade entre o objeto _x_ e base do usuário (_y_), utilizando a média ponderada, dá-se por:

$$ Sim(x, y) = \frac{J(x, a) * n1 + J(x, b) * n2 + J(x, c) * n3}{n1 + n2 + n3} $$

# Base de dados

A base de dados foi construída a partir de um _web scraping_ do site https://myanimelist.net. Uma nova base de dados pode ser construída através do arquivo **get_animes_data.py**, que consiste em um script Python com uma classe que possui os métodos necessários para o _web scraping_.

Primeiramente é necessário pegar os _ids_ dos títulos, e a melhor forma que foi considerada para fazer isto é através da página de _Top Anime_, em que os títulos estão ordenados através da nota geral, onde são disponibilizados 50 títulos por página. O método para a _request_ dos _ids_ é o **get_animes_id**.

Após isso, é possível entrar na página específica de cada título pelo _id_ e salvar vários dados interessantes. No caso desse sistema, as informações mais relevantes foram os gêneros de cada anime (utilizados para o cálculo de similaridade) e a nota geral de cada um (apenas para uma visualização do usuário e uma ordenação no resultado final). O método para a _request_ das informações individuais é **get_animes_info**.

Por fim, é necessário que haja um pré-processamento para transformar os gêneros em vetores binários, e isto é feito através do método **database_preprocessing**, que considera o valor 1 para o gênero existente determinado anime e 0 para o gênero ausente naquele anime.

Após esses processos, a base de dados está pronta para que sejam realizados os cálculos de similaridade.

# Instalação de bibliotecas e uso do sistema

Todas as bibliotecas que são necessárias para a utilização do sistema estão no arquivo **requirements.txt**, e a instalação delas pode ser feita através do terminal com o seguinte comando:

    pip install -r requirements.txt

Após a instalação das bibliotecas, o script pode ser executado com o seguinte comando no terminal a partir do diretório que se encontra o arquivo **run.py**:

    streamlit run run.py

Uma janela web abrirá e o usuário poderá fazer o uso do sistema.