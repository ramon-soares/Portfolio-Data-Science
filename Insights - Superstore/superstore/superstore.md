# Superstore Giant
___
___

### Sobre o dataset utilizado

Com demandas crescentes e competições acirradas no mercado, a Superstore Giant está buscando seu conhecimento para entender o que funciona melhor para ela. Eles gostariam de entender quais produtos, regiões, categorias e segmentos de clientes eles devem segmentar ou evitar.

Disponível em: https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download

### Sobre as colunas do dataset

    Row ID         ->  ID exclusivo para cada linha  
    Order ID       ->  ID do pedido exclusivo para cada cliente  
    Order Date     ->  Data do pedido do produto  
    Ship Date      ->  Data de envio do produto  
    Ship Mode      ->  Modo de envio especificado pelo cliente  
    Customer ID    ->  ID exclusivo para identificar cada cliente  
    Customer Name  ->  Nome do cliente  
    Segment        ->  O segmento ao qual o cliente pertence  
    Country        ->  País de residência do cliente  
    City           ->  Cidade de residência do cliente  
    State          ->  Estado de residência do cliente  
    Postal Code    ->  Código postal de cada cliente  
    Region         ->  Região onde o cliente pertence  
    Product ID     ->  ID exclusivo do produto  
    Category       ->  Categoria do produto encomendado  
    Sub-Category   ->  Subcategoria do produto encomendado  
    Product Name   ->  Nome do produto  
    Sales          ->  Vendas do produto  
    Quantity       ->  Quantidade do produto  
    Discount       ->  Desconto fornecido  
    Profit         ->  Lucro/perda incorrido  

## Bibliotecas utilizadas
___


```python
# Importações
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações
%matplotlib inline
pd.set_option('display.max_columns', None)
sns.set_theme(style='darkgrid', palette='mako', font_scale=1.1)
```

## Importação e tratamento dos dados
___

###### Importar csv e colocá-lo como DataFrame


```python
data = pd.read_csv('dataset/Sample - Superstore.csv', encoding='windows-1252')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row ID</th>
      <th>Order ID</th>
      <th>Order Date</th>
      <th>Ship Date</th>
      <th>Ship Mode</th>
      <th>Customer ID</th>
      <th>Customer Name</th>
      <th>Segment</th>
      <th>Country</th>
      <th>City</th>
      <th>State</th>
      <th>Postal Code</th>
      <th>Region</th>
      <th>Product ID</th>
      <th>Category</th>
      <th>Sub-Category</th>
      <th>Product Name</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Discount</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>CA-2016-152156</td>
      <td>11/8/2016</td>
      <td>11/11/2016</td>
      <td>Second Class</td>
      <td>CG-12520</td>
      <td>Claire Gute</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Henderson</td>
      <td>Kentucky</td>
      <td>42420</td>
      <td>South</td>
      <td>FUR-BO-10001798</td>
      <td>Furniture</td>
      <td>Bookcases</td>
      <td>Bush Somerset Collection Bookcase</td>
      <td>261.9600</td>
      <td>2</td>
      <td>0.00</td>
      <td>41.9136</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>CA-2016-152156</td>
      <td>11/8/2016</td>
      <td>11/11/2016</td>
      <td>Second Class</td>
      <td>CG-12520</td>
      <td>Claire Gute</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Henderson</td>
      <td>Kentucky</td>
      <td>42420</td>
      <td>South</td>
      <td>FUR-CH-10000454</td>
      <td>Furniture</td>
      <td>Chairs</td>
      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>
      <td>731.9400</td>
      <td>3</td>
      <td>0.00</td>
      <td>219.5820</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>CA-2016-138688</td>
      <td>6/12/2016</td>
      <td>6/16/2016</td>
      <td>Second Class</td>
      <td>DV-13045</td>
      <td>Darrin Van Huff</td>
      <td>Corporate</td>
      <td>United States</td>
      <td>Los Angeles</td>
      <td>California</td>
      <td>90036</td>
      <td>West</td>
      <td>OFF-LA-10000240</td>
      <td>Office Supplies</td>
      <td>Labels</td>
      <td>Self-Adhesive Address Labels for Typewriters b...</td>
      <td>14.6200</td>
      <td>2</td>
      <td>0.00</td>
      <td>6.8714</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>US-2015-108966</td>
      <td>10/11/2015</td>
      <td>10/18/2015</td>
      <td>Standard Class</td>
      <td>SO-20335</td>
      <td>Sean O'Donnell</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Fort Lauderdale</td>
      <td>Florida</td>
      <td>33311</td>
      <td>South</td>
      <td>FUR-TA-10000577</td>
      <td>Furniture</td>
      <td>Tables</td>
      <td>Bretford CR4500 Series Slim Rectangular Table</td>
      <td>957.5775</td>
      <td>5</td>
      <td>0.45</td>
      <td>-383.0310</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>US-2015-108966</td>
      <td>10/11/2015</td>
      <td>10/18/2015</td>
      <td>Standard Class</td>
      <td>SO-20335</td>
      <td>Sean O'Donnell</td>
      <td>Consumer</td>
      <td>United States</td>
      <td>Fort Lauderdale</td>
      <td>Florida</td>
      <td>33311</td>
      <td>South</td>
      <td>OFF-ST-10000760</td>
      <td>Office Supplies</td>
      <td>Storage</td>
      <td>Eldon Fold 'N Roll Cart System</td>
      <td>22.3680</td>
      <td>2</td>
      <td>0.20</td>
      <td>2.5164</td>
    </tr>
  </tbody>
</table>
</div>



###### Informações iniciais sobre o dataset


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 9994 entries, 0 to 9993
    Data columns (total 21 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   Row ID         9994 non-null   int64  
     1   Order ID       9994 non-null   object 
     2   Order Date     9994 non-null   object 
     3   Ship Date      9994 non-null   object 
     4   Ship Mode      9994 non-null   object 
     5   Customer ID    9994 non-null   object 
     6   Customer Name  9994 non-null   object 
     7   Segment        9994 non-null   object 
     8   Country        9994 non-null   object 
     9   City           9994 non-null   object 
     10  State          9994 non-null   object 
     11  Postal Code    9994 non-null   int64  
     12  Region         9994 non-null   object 
     13  Product ID     9994 non-null   object 
     14  Category       9994 non-null   object 
     15  Sub-Category   9994 non-null   object 
     16  Product Name   9994 non-null   object 
     17  Sales          9994 non-null   float64
     18  Quantity       9994 non-null   int64  
     19  Discount       9994 non-null   float64
     20  Profit         9994 non-null   float64
    dtypes: float64(3), int64(3), object(15)
    memory usage: 1.6+ MB
    

###### Descrições iniciais sobre o dataset


```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row ID</th>
      <th>Postal Code</th>
      <th>Sales</th>
      <th>Quantity</th>
      <th>Discount</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>9994.000000</td>
      <td>9994.000000</td>
      <td>9994.000000</td>
      <td>9994.000000</td>
      <td>9994.000000</td>
      <td>9994.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4997.500000</td>
      <td>55190.379428</td>
      <td>229.858001</td>
      <td>3.789574</td>
      <td>0.156203</td>
      <td>28.656896</td>
    </tr>
    <tr>
      <th>std</th>
      <td>2885.163629</td>
      <td>32063.693350</td>
      <td>623.245101</td>
      <td>2.225110</td>
      <td>0.206452</td>
      <td>234.260108</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1040.000000</td>
      <td>0.444000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>-6599.978000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2499.250000</td>
      <td>23223.000000</td>
      <td>17.280000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>1.728750</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4997.500000</td>
      <td>56430.500000</td>
      <td>54.490000</td>
      <td>3.000000</td>
      <td>0.200000</td>
      <td>8.666500</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7495.750000</td>
      <td>90008.000000</td>
      <td>209.940000</td>
      <td>5.000000</td>
      <td>0.200000</td>
      <td>29.364000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9994.000000</td>
      <td>99301.000000</td>
      <td>22638.480000</td>
      <td>14.000000</td>
      <td>0.800000</td>
      <td>8399.976000</td>
    </tr>
  </tbody>
</table>
</div>



###### Excluir colunas que não vão ser utilizadas


```python
data.drop(['Row ID'], axis=1, inplace=True)
```

###### Alterar nome das colunas do dataset


```python
data.columns = [x.replace(' ', '_').lower() for x in data.columns]
data.columns
```




    Index(['order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_id',
           'customer_name', 'segment', 'country', 'city', 'state', 'postal_code',
           'region', 'product_id', 'category', 'sub-category', 'product_name',
           'sales', 'quantity', 'discount', 'profit'],
          dtype='object')



###### Mudar formato das datas


```python
data['order_date'] = pd.to_datetime(data['order_date'], format='%m/%d/%Y')
data['ship_date'] = pd.to_datetime(data['ship_date'], format='%m/%d/%Y')
```

###### Verificar dados nulos


```python
data.isnull().sum()
```




    order_id         0
    order_date       0
    ship_date        0
    ship_mode        0
    customer_id      0
    customer_name    0
    segment          0
    country          0
    city             0
    state            0
    postal_code      0
    region           0
    product_id       0
    category         0
    sub-category     0
    product_name     0
    sales            0
    quantity         0
    discount         0
    profit           0
    dtype: int64



Não há dados faltantes na base de dados

## Visualização dos dados 
_________________________________________

### Informações básicas


##### Países


```python
data['country'].value_counts()
```




    United States    9994
    Name: country, dtype: int64



Todas as vendas que estão na base de dados foram feitas nos Estados Unidos, então essa coluna pode ser excluída.


```python
data.drop(['country'], axis=1, inplace=True)
```

##### Estados


```python
data['state'].unique()
```




    array(['Kentucky', 'California', 'Florida', 'North Carolina',
           'Washington', 'Texas', 'Wisconsin', 'Utah', 'Nebraska',
           'Pennsylvania', 'Illinois', 'Minnesota', 'Michigan', 'Delaware',
           'Indiana', 'New York', 'Arizona', 'Virginia', 'Tennessee',
           'Alabama', 'South Carolina', 'Oregon', 'Colorado', 'Iowa', 'Ohio',
           'Missouri', 'Oklahoma', 'New Mexico', 'Louisiana', 'Connecticut',
           'New Jersey', 'Massachusetts', 'Georgia', 'Nevada', 'Rhode Island',
           'Mississippi', 'Arkansas', 'Montana', 'New Hampshire', 'Maryland',
           'District of Columbia', 'Kansas', 'Vermont', 'Maine',
           'South Dakota', 'Idaho', 'North Dakota', 'Wyoming',
           'West Virginia'], dtype=object)



##### Cidades


```python
data['city'].unique()
```




    array(['Henderson', 'Los Angeles', 'Fort Lauderdale', 'Concord',
           'Seattle', 'Fort Worth', 'Madison', 'West Jordan', 'San Francisco',
           'Fremont', 'Philadelphia', 'Orem', 'Houston', 'Richardson',
           'Naperville', 'Melbourne', 'Eagan', 'Westland', 'Dover',
           'New Albany', 'New York City', 'Troy', 'Chicago', 'Gilbert',
           'Springfield', 'Jackson', 'Memphis', 'Decatur', 'Durham',
           'Columbia', 'Rochester', 'Minneapolis', 'Portland', 'Saint Paul',
           'Aurora', 'Charlotte', 'Orland Park', 'Urbandale', 'Columbus',
           'Bristol', 'Wilmington', 'Bloomington', 'Phoenix', 'Roseville',
           'Independence', 'Pasadena', 'Newark', 'Franklin', 'Scottsdale',
           'San Jose', 'Edmond', 'Carlsbad', 'San Antonio', 'Monroe',
           'Fairfield', 'Grand Prairie', 'Redlands', 'Hamilton', 'Westfield',
           'Akron', 'Denver', 'Dallas', 'Whittier', 'Saginaw', 'Medina',
           'Dublin', 'Detroit', 'Tampa', 'Santa Clara', 'Lakeville',
           'San Diego', 'Brentwood', 'Chapel Hill', 'Morristown',
           'Cincinnati', 'Inglewood', 'Tamarac', 'Colorado Springs',
           'Belleville', 'Taylor', 'Lakewood', 'Arlington', 'Arvada',
           'Hackensack', 'Saint Petersburg', 'Long Beach', 'Hesperia',
           'Murfreesboro', 'Layton', 'Austin', 'Lowell', 'Manchester',
           'Harlingen', 'Tucson', 'Quincy', 'Pembroke Pines', 'Des Moines',
           'Peoria', 'Las Vegas', 'Warwick', 'Miami', 'Huntington Beach',
           'Richmond', 'Louisville', 'Lawrence', 'Canton', 'New Rochelle',
           'Gastonia', 'Jacksonville', 'Auburn', 'Norman', 'Park Ridge',
           'Amarillo', 'Lindenhurst', 'Huntsville', 'Fayetteville',
           'Costa Mesa', 'Parker', 'Atlanta', 'Gladstone', 'Great Falls',
           'Lakeland', 'Montgomery', 'Mesa', 'Green Bay', 'Anaheim',
           'Marysville', 'Salem', 'Laredo', 'Grove City', 'Dearborn',
           'Warner Robins', 'Vallejo', 'Mission Viejo', 'Rochester Hills',
           'Plainfield', 'Sierra Vista', 'Vancouver', 'Cleveland', 'Tyler',
           'Burlington', 'Waynesboro', 'Chester', 'Cary', 'Palm Coast',
           'Mount Vernon', 'Hialeah', 'Oceanside', 'Evanston', 'Trenton',
           'Cottage Grove', 'Bossier City', 'Lancaster', 'Asheville',
           'Lake Elsinore', 'Omaha', 'Edmonds', 'Santa Ana', 'Milwaukee',
           'Florence', 'Lorain', 'Linden', 'Salinas', 'New Brunswick',
           'Garland', 'Norwich', 'Alexandria', 'Toledo', 'Farmington',
           'Riverside', 'Torrance', 'Round Rock', 'Boca Raton',
           'Virginia Beach', 'Murrieta', 'Olympia', 'Washington',
           'Jefferson City', 'Saint Peters', 'Rockford', 'Brownsville',
           'Yonkers', 'Oakland', 'Clinton', 'Encinitas', 'Roswell',
           'Jonesboro', 'Antioch', 'Homestead', 'La Porte', 'Lansing',
           'Cuyahoga Falls', 'Reno', 'Harrisonburg', 'Escondido', 'Royal Oak',
           'Rockville', 'Coral Springs', 'Buffalo', 'Boynton Beach',
           'Gulfport', 'Fresno', 'Greenville', 'Macon', 'Cedar Rapids',
           'Providence', 'Pueblo', 'Deltona', 'Murray', 'Middletown',
           'Freeport', 'Pico Rivera', 'Provo', 'Pleasant Grove', 'Smyrna',
           'Parma', 'Mobile', 'New Bedford', 'Irving', 'Vineland', 'Glendale',
           'Niagara Falls', 'Thomasville', 'Westminster', 'Coppell', 'Pomona',
           'North Las Vegas', 'Allentown', 'Tempe', 'Laguna Niguel',
           'Bridgeton', 'Everett', 'Watertown', 'Appleton', 'Bellevue',
           'Allen', 'El Paso', 'Grapevine', 'Carrollton', 'Kent', 'Lafayette',
           'Tigard', 'Skokie', 'Plano', 'Suffolk', 'Indianapolis', 'Bayonne',
           'Greensboro', 'Baltimore', 'Kenosha', 'Olathe', 'Tulsa', 'Redmond',
           'Raleigh', 'Muskogee', 'Meriden', 'Bowling Green', 'South Bend',
           'Spokane', 'Keller', 'Port Orange', 'Medford', 'Charlottesville',
           'Missoula', 'Apopka', 'Reading', 'Broomfield', 'Paterson',
           'Oklahoma City', 'Chesapeake', 'Lubbock', 'Johnson City',
           'San Bernardino', 'Leominster', 'Bozeman', 'Perth Amboy',
           'Ontario', 'Rancho Cucamonga', 'Moorhead', 'Mesquite', 'Stockton',
           'Ormond Beach', 'Sunnyvale', 'York', 'College Station',
           'Saint Louis', 'Manteca', 'San Angelo', 'Salt Lake City',
           'Knoxville', 'Little Rock', 'Lincoln Park', 'Marion', 'Littleton',
           'Bangor', 'Southaven', 'New Castle', 'Midland', 'Sioux Falls',
           'Fort Collins', 'Clarksville', 'Sacramento', 'Thousand Oaks',
           'Malden', 'Holyoke', 'Albuquerque', 'Sparks', 'Coachella',
           'Elmhurst', 'Passaic', 'North Charleston', 'Newport News',
           'Jamestown', 'Mishawaka', 'La Quinta', 'Tallahassee', 'Nashville',
           'Bellingham', 'Woodstock', 'Haltom City', 'Wheeling',
           'Summerville', 'Hot Springs', 'Englewood', 'Las Cruces', 'Hoover',
           'Frisco', 'Vacaville', 'Waukesha', 'Bakersfield', 'Pompano Beach',
           'Corpus Christi', 'Redondo Beach', 'Orlando', 'Orange',
           'Lake Charles', 'Highland Park', 'Hempstead', 'Noblesville',
           'Apple Valley', 'Mount Pleasant', 'Sterling Heights', 'Eau Claire',
           'Pharr', 'Billings', 'Gresham', 'Chattanooga', 'Meridian',
           'Bolingbrook', 'Maple Grove', 'Woodland', 'Missouri City',
           'Pearland', 'San Mateo', 'Grand Rapids', 'Visalia',
           'Overland Park', 'Temecula', 'Yucaipa', 'Revere', 'Conroe',
           'Tinley Park', 'Dubuque', 'Dearborn Heights', 'Santa Fe',
           'Hickory', 'Carol Stream', 'Saint Cloud', 'North Miami',
           'Plantation', 'Port Saint Lucie', 'Rock Hill', 'Odessa',
           'West Allis', 'Chula Vista', 'Manhattan', 'Altoona', 'Thornton',
           'Champaign', 'Texarkana', 'Edinburg', 'Baytown', 'Greenwood',
           'Woonsocket', 'Superior', 'Bedford', 'Covington', 'Broken Arrow',
           'Miramar', 'Hollywood', 'Deer Park', 'Wichita', 'Mcallen',
           'Iowa City', 'Boise', 'Cranston', 'Port Arthur', 'Citrus Heights',
           'The Colony', 'Daytona Beach', 'Bullhead City', 'Portage', 'Fargo',
           'Elkhart', 'San Gabriel', 'Margate', 'Sandy Springs', 'Mentor',
           'Lawton', 'Hampton', 'Rome', 'La Crosse', 'Lewiston',
           'Hattiesburg', 'Danville', 'Logan', 'Waterbury', 'Athens',
           'Avondale', 'Marietta', 'Yuma', 'Wausau', 'Pasco', 'Oak Park',
           'Pensacola', 'League City', 'Gaithersburg', 'Lehi', 'Tuscaloosa',
           'Moreno Valley', 'Georgetown', 'Loveland', 'Chandler', 'Helena',
           'Kirkwood', 'Waco', 'Frankfort', 'Bethlehem', 'Grand Island',
           'Woodbury', 'Rogers', 'Clovis', 'Jupiter', 'Santa Barbara',
           'Cedar Hill', 'Norfolk', 'Draper', 'Ann Arbor', 'La Mesa',
           'Pocatello', 'Holland', 'Milford', 'Buffalo Grove', 'Lake Forest',
           'Redding', 'Chico', 'Utica', 'Conway', 'Cheyenne', 'Owensboro',
           'Caldwell', 'Kenner', 'Nashua', 'Bartlett', 'Redwood City',
           'Lebanon', 'Santa Maria', 'Des Plaines', 'Longview',
           'Hendersonville', 'Waterloo', 'Cambridge', 'Palatine', 'Beverly',
           'Eugene', 'Oxnard', 'Renton', 'Glenview', 'Delray Beach',
           'Commerce City', 'Texas City', 'Wilson', 'Rio Rancho', 'Goldsboro',
           'Montebello', 'El Cajon', 'Beaumont', 'West Palm Beach', 'Abilene',
           'Normal', 'Saint Charles', 'Camarillo', 'Hillsboro', 'Burbank',
           'Modesto', 'Garden City', 'Atlantic City', 'Longmont', 'Davis',
           'Morgan Hill', 'Clifton', 'Sheboygan', 'East Point', 'Rapid City',
           'Andover', 'Kissimmee', 'Shelton', 'Danbury', 'Sanford',
           'San Marcos', 'Greeley', 'Mansfield', 'Elyria', 'Twin Falls',
           'Coral Gables', 'Romeoville', 'Marlborough', 'Laurel', 'Bryan',
           'Pine Bluff', 'Aberdeen', 'Hagerstown', 'East Orange',
           'Arlington Heights', 'Oswego', 'Coon Rapids', 'San Clemente',
           'San Luis Obispo', 'Springdale', 'Lodi', 'Mason'], dtype=object)



##### Quantos produtos diferentes a base de dados possui?


```python
len(data['product_id'].unique())
```




    1862



##### Quais categorias de produtos  e quantos produtos de cada uma existem na base de dados? 


```python
data['category'].value_counts()
```




    Office Supplies    6026
    Furniture          2121
    Technology         1847
    Name: category, dtype: int64



##### Quais sub-categorias de produtos e  quantos produtos de cada uma existem na base de dados? 


```python
data['sub-category'].value_counts()
```




    Binders        1523
    Paper          1370
    Furnishings     957
    Phones          889
    Storage         846
    Art             796
    Accessories     775
    Chairs          617
    Appliances      466
    Labels          364
    Tables          319
    Envelopes       254
    Bookcases       228
    Fasteners       217
    Supplies        190
    Machines        115
    Copiers          68
    Name: sub-category, dtype: int64



##### Quantidade de itens vendidos no período analisado


```python
data['quantity'].sum()
```




    37873



##### Total em vendas no período analisado


```python
data['sales'].sum()
```




    2297200.8603000003



##### Lucro total no período analisado


```python
data['profit'].sum()
```




    286397.0217



### Informações gerais

##### Lucro total em relação a cada característica


```python
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
fig.suptitle('Lucro total em relação a cada característica')

# Ship Mode
query = data.groupby('ship_mode')["profit"].sum()
sns.barplot(ax=axes[0, 0], x=query.index, y=query).set(title='Ship Mode', xlabel='')

# Segment
query = data.groupby('segment')["profit"].sum()
sns.barplot(ax=axes[0, 1], x=query.index, y=query).set(title='Segment', xlabel='')

# Region
query = data.groupby('region')["profit"].sum().sort_values(ascending=False)
sns.barplot(ax=axes[1, 0], y=query.index, x=query).set(title='Region', ylabel='')

# Category
query = data.groupby('category')["profit"].sum().sort_values(ascending=False)
sns.barplot(ax=axes[1, 1], y=query.index, x=query).set(title='Category', ylabel='')

# Quantity
query = data.groupby('quantity')["profit"].sum()
sns.barplot(ax=axes[2, 0], x=query.index, y=query, palette='crest').set(title='Quantity', xlabel='')

# Discount
query = data.groupby('discount')["profit"].sum()
sns.barplot(ax=axes[2, 1], x=query.index, y=query, palette='crest').set(title='Discount', xlabel='')

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)
```


    
![png](output_47_0.png)
    


##### Média de lucro em relação a cada característica


```python
fig, axes = plt.subplots(3, 2, figsize=(14, 18))
fig.suptitle('Média de lucro em relação a cada característica')

# Ship Mode
query = data.groupby('ship_mode')["profit"].mean()
sns.barplot(ax=axes[0, 0], x=query.index, y=query).set(title='Ship Mode', xlabel='')

# Segment
query = data.groupby('segment')["profit"].mean()
sns.barplot(ax=axes[0, 1], x=query.index, y=query).set(title='Segment', xlabel='')

# Region
query = data.groupby('region')["profit"].mean().sort_values(ascending=False)
sns.barplot(ax=axes[1, 0], y=query.index, x=query).set(title='Region', ylabel='')

# Category
query = data.groupby('category')["profit"].mean().sort_values(ascending=False)
sns.barplot(ax=axes[1, 1], y=query.index, x=query).set(title='Category', ylabel='')

# Quantity
query = data.groupby('quantity')["profit"].mean()
sns.barplot(ax=axes[2, 0], x=query.index, y=query, palette='crest').set(title='Quantity', xlabel='')

# Discount
query = data.groupby('discount')["profit"].mean()
sns.barplot(ax=axes[2, 1], x=query.index, y=query, palette='crest').set(title='Discount', xlabel='')

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=0.4)

```


    
![png](output_49_0.png)
    


###### Levando em conta uma análise mais superficial, temos que:

* Ship Mode: A média de lucro entre os modos de envio possuem leve diferença, porém em relação ao lucro total, temos que 'Standard Class' gera bem mais lucro que os outros modos de envio, enquanto 'Same Day' gera menos lucro.
* Segment: 'Home Office' gera maior lucro médio dentre os segmentos, porém possui menos lucro total em relação aos outros. Enquanto isso 'Consumer' é o segmento com menos lucro médio, porém com maior lucro total.
* Region: 'West' e 'East' são as regiões em que o lucro total e o lucro médio são melhores.
* Category: O lucro total e médio em 'Technology' é muito superior em relação às outras categorias. 'Furniture' é a que menos gera lucro em geral.
* Quantity: Em relação à quantidade, temos que compras com menos quantidades são mais comuns, então acabam gerando mais lucro total. Inverso à isso, conforme se cresce a quantidade, o lucro médio tende a aumentar.
* Discount: Compras sem desconto tendem a dar mais lucro total, devido ao fato de que não prejudica o preço do produto. Análogo a isso, compras com 0% de desconto a 10% de desconto tendem a dar mais lucro médio, pois acima disso o lucro sobre o produto vai ficando cada vez mais baixo, podendo gerar até prejuízos.


##### Top 10 cidades que geraram mais lucro


```python
# Query
query = data.groupby(['city'])['profit'].sum().sort_values(ascending=False).head(10)

# Gráfico
plt.figure(figsize=(14, 6))
plt.xticks(rotation=45)
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:xlabel='city', ylabel='profit'>




    
![png](output_52_1.png)
    


##### Top 10 cidades que deram menos lucro ou prejuízo


```python
# Query
query = data.groupby(['city'])['profit'].sum().sort_values(ascending=True).head(10)

# Gráfico
plt.figure(figsize=(14, 6))
plt.xticks(rotation=45)
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:xlabel='city', ylabel='profit'>




    
![png](output_54_1.png)
    


##### Top 10 produtos que geraram mais lucro


```python
# Query
query = data.groupby(['product_id'])['profit'].sum().sort_values(ascending=False).head(10)

# Nome do produto que gerou mais lucro
best_seller_id = query.index[0]
best_seller = data[data['product_id']==best_seller_id]['product_name'].iloc[0]

# Gráfico
plt.figure(figsize=(14, 6))
plt.xticks(rotation=45)
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:xlabel='product_id', ylabel='profit'>




    
![png](output_56_1.png)
    



```python
best_seller
```




    'Canon imageCLASS 2200 Advanced Copier'



Temos que o produto 'Canon imageCLASS 2200 Advanced Copier' é o que possui mais lucro dentre todos os produtos, com uma grande discrepância em relação aos outros produtos.

##### Top 10 produtos que geraram mais prejuízo


```python
# Query
query = data.groupby(['product_id'])['profit'].sum().sort_values(ascending=True).head(10)

# Nome do produto que gerou mais prejuízo
worst_seller_id = query.index[0]
worst_seller = data[data['product_id']==worst_seller_id]['product_name'].iloc[0]

# Gráfico
plt.figure(figsize=(14, 6))
plt.xticks(rotation=45)
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:xlabel='product_id', ylabel='profit'>




    
![png](output_60_1.png)
    



```python
worst_seller
```




    'Cubify CubeX 3D Printer Double Head Print'



Temos que o produto 'Cubify CubeX 3D Printer Double Head Print' é o que possui mais prejuízo dentre todos os produtos, com uma grande discrepância em relação aos outros produtos.

### Análise sobre o item que gerou mais lucro


```python
# Quantidade de vendas por região
query = data[['region', 'product_id', 'sales', 'profit']]
query = query[query['product_id']==best_seller_id]
query
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>region</th>
      <th>product_id</th>
      <th>sales</th>
      <th>profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2623</th>
      <td>East</td>
      <td>TEC-CO-10004722</td>
      <td>11199.968</td>
      <td>3919.9888</td>
    </tr>
    <tr>
      <th>4190</th>
      <td>East</td>
      <td>TEC-CO-10004722</td>
      <td>10499.970</td>
      <td>5039.9856</td>
    </tr>
    <tr>
      <th>6425</th>
      <td>East</td>
      <td>TEC-CO-10004722</td>
      <td>8399.976</td>
      <td>1119.9968</td>
    </tr>
    <tr>
      <th>6826</th>
      <td>Central</td>
      <td>TEC-CO-10004722</td>
      <td>17499.950</td>
      <td>8399.9760</td>
    </tr>
    <tr>
      <th>8153</th>
      <td>West</td>
      <td>TEC-CO-10004722</td>
      <td>13999.960</td>
      <td>6719.9808</td>
    </tr>
  </tbody>
</table>
</div>



Houveram cinco vendas do produto que gerou mais lucro, todas com um bom lucro, nenhuma com prejuízo. Pode-se pensar na possibilidade de criar estratégias para acarretar um aumento de sua venda.

##### Diferença de lucro por região


```python
# Query
query = data[['region', 'profit', 'product_id']]
query = query[query['product_id']==best_seller_id]
query = query.groupby(['region']).sum().reset_index()

# Gráfico
plt.figure(figsize=(14, 8))
plt.title('Lucro por região do produto ' + best_seller)
plt.pie(x=query['profit'], autopct='%1.1f%%', textprops={'color':'white', 'weight':'bold', 'size':12})
plt.legend(labels=query['region'],
          title='Região',
          title_fontsize=14,
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          prop={'size':14})
```




    <matplotlib.legend.Legend at 0x210dfbbfb20>




    
![png](output_67_1.png)
    


##### Diferença de lucro por estados


```python
# Query
query = data[['state', 'profit', 'product_id']]
query = query[query['product_id']==best_seller_id]
query = query.groupby(['state']).sum().reset_index()

# Gráfico
plt.figure(figsize=(14, 8))
plt.title('Lucro por estados do produto ' + best_seller)
plt.pie(x=query['profit'], autopct='%1.1f%%', textprops={'color':'white', 'weight':'bold', 'size':12})
plt.legend(labels=query['state'],
          title='Estado',
          title_fontsize=14,
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),
          prop={'size':14})
```




    <matplotlib.legend.Legend at 0x210dfa102e0>




    
![png](output_69_1.png)
    


### Análise sobre o item que gerou mais prejuízo


```python
# Quantidade de vendas por região
query = data[['region', 'product_id', 'sales', 'profit']]
query = query[query['product_id']==worst_seller_id]
query
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>region</th>
      <th>product_id</th>
      <th>sales</th>
      <th>profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3151</th>
      <td>East</td>
      <td>TEC-MA-10000418</td>
      <td>1799.994</td>
      <td>-2639.9912</td>
    </tr>
    <tr>
      <th>4218</th>
      <td>West</td>
      <td>TEC-MA-10000418</td>
      <td>4799.984</td>
      <td>359.9988</td>
    </tr>
    <tr>
      <th>7772</th>
      <td>East</td>
      <td>TEC-MA-10000418</td>
      <td>4499.985</td>
      <td>-6599.9780</td>
    </tr>
  </tbody>
</table>
</div>



Houveram apenas três vendas do produto com mais prejuízo. A quantidade de vendas é bastante pequena e o prejuízo é muito grande, teve-se apenas uma venda com lucro, que foi baixo, então pode-se pensar na possibilidade de remover tal produto do catálogo.

### Análise sobre a categoria 'Furniture'

##### Diferença de lucro por região


```python
# Query
query = data[data['category'] == 'Furniture']
query = query.groupby(['region'])['profit'].sum()

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Furniture' - Lucro de acordo com cada região")
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:title={'center':"'Furniture' - Lucro de acordo com cada região"}, xlabel='region', ylabel='profit'>




    
![png](output_75_1.png)
    


A região 'Central' é a única que não obteve lucro com a categoria 'Furniture', seguida pela região 'East', que obteve pouco lucro e teve alguns pontos abordados mais à frente em relação a algumas sub-categorias dentro da categoria 'Furniture' que geram prejuízo.


```python
# Query
query = data[(data['category']=='Furniture') & (data['region']=='Central')]

# Gráfico
plt.figure(figsize=(14, 8))
plt.title("'Furniture' - Lucro de cada estado da região 'Central'")
sns.scatterplot(data=query, x='sales', y='profit', hue='state', size='state', sizes=(70,70), palette='Paired')
plt.legend(title='Estado')
```




    <matplotlib.legend.Legend at 0x210dfb0e790>




    
![png](output_77_1.png)
    


No gráfico de dispersão acima, verificamos que há alguns estados da região 'Central' que majoritariamente dão prejuízo, vamos ver melhor quais são eles.


```python
# Query
query = data[(data['category']=='Furniture') & (data['region']=='Central')]
query = query.groupby(['state'])['profit'].sum().sort_values()

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Furniture' - Lucro de cada estado da região 'Central'")
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:title={'center':"'Furniture' - Lucro de cada estado da região 'Central'"}, xlabel='state', ylabel='profit'>




    
![png](output_79_1.png)
    


Temos então que os estados 'Texas' e 'Illinois', que são da região 'Central', geram muito prejuízo em relação aos produtos da categoria 'Furniture'. Esse problema em questão é grave, uma vez que todo o prejuízo da região está concentrado nesses dois estados, que somado é maior que a soma do lucro dos outros estados. Esse tamanho de prejuízo faz com que a região fique com lucro total negativo.

### Análise relacionada às sub-categorias em geral

##### Lucro por sub-categoria


```python
# Query
query = data[['sub-category', 'profit']]
query = query.groupby(['sub-category'])['profit'].sum().sort_values(ascending=False)

# Gráfico
plt.figure(figsize=(14, 6))
plt.xticks(rotation=45)
plt.title('Lucro por sub-categorias')
sns.barplot(x=query.index, y=query, palette='crest')
```




    <AxesSubplot:title={'center':'Lucro por sub-categorias'}, xlabel='sub-category', ylabel='profit'>




    
![png](output_83_1.png)
    


'Copiers', 'Phones' e 'Accessories' dão mais lucro. Além disso, percebe-se que 'Tables' gera muito prejuízo, que é seguido por 'Bookcases' e 'Supplies' que geram um prejuízo menor, e por 'Fasteners' que gera praticamente nenhum lucro.

### Analisando a sub-categoria 'Tables'

##### Verificando lucro por região


```python
# Query
query = data[data['sub-category'] == 'Tables']

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Tables' - Lucro pelo preço de venda")
sns.scatterplot(data=query, x='sales', y='profit', hue='region', size='region', sizes=(70,70), palette='Set1')
plt.legend(title='Região')
```




    <matplotlib.legend.Legend at 0x210e08c1a30>




    
![png](output_87_1.png)
    


Em geral, essa sub-categoria ou gera pouco lucro ou gera prejuízo.Além disso, percebe-se que praticamente todas as vendas para a região 'East' dão prejuízo. Vamos fazer uma comparação.


```python
# Query
query = pd.DataFrame([[query['profit'].sum(), query[query['region']!='East']['profit'].sum()]],
                          columns=['with_east', 'without_east'])

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("Prejuízo da sub-categoria 'Tables' incluindo e excluindo a região 'East'")
sns.barplot(data=query).set(ylabel='profit')
```




    [Text(0, 0.5, 'profit')]




    
![png](output_89_1.png)
    


Conseguimos ver que a sub-categoria na região 'East' realmente dá um prejuízo muito grande, então é importante evitar fazer vendas de 'Tables' nessa região ou adotar estratégias diferentes. Vale ressaltar que mesmo evitando a região citada, ao final o lucro ainda é negativo, como vemos no gráfico.


```python
# Query
query = data[(data['sub-category'] == 'Tables')]
query = query.groupby('region').sum()['profit']

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Tables' - Lucro por região")
sns.barplot(x=query.index, y=query)
```




    <AxesSubplot:title={'center':"'Tables' - Lucro por região"}, xlabel='region', ylabel='profit'>




    
![png](output_91_1.png)
    


Somente a região 'West' gera lucro com a sub-categoria 'Tables', então é um cenário que não pode ser ignorado.

### Analisando a sub-categoria 'Bookcases''

##### Verificando lucro por região


```python
# Query
query = data[data['sub-category'] == 'Bookcases']
query = query.groupby(['region']).sum()['profit']

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Bookcases' - Lucro por região")
sns.barplot(x=query.index, y=query)
```




    <AxesSubplot:title={'center':"'Bookcases' - Lucro por região"}, xlabel='region', ylabel='profit'>




    
![png](output_95_1.png)
    


Temos um cenário um pouco parecido com o da sub-categoria 'Tables', onde somente uma região gera lucro, então novamente é uma situação que não pode ser ignorada.

### Analisando a sub-categoria 'Copiers'

##### Verificando lucro por região


```python
# Query
query = data[data['sub-category'] == 'Copiers']

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Copiers' - Lucro pelo preço de venda")
sns.scatterplot(data=query, x='sales', y='profit', hue='region', size='region', sizes=(70,70), palette='Set1')
plt.legend(title='Região')
```




    <matplotlib.legend.Legend at 0x210e1f0f0a0>




    
![png](output_99_1.png)
    


##### Quantidade de vendas com prejuízos


```python
query = data[(data['sub-category'] == 'Copiers') & (data['profit'] < 0.0)]
len(query)
```




    0



'Copiers' aparentemente não é uma sub-categoria que possui algum problema, além de gerar bastante lucro, não gera prejuízos.

### Analisando a sub-categoria 'Phones'

##### Verificando lucro por região


```python
# Query
query = data[data['sub-category'] == 'Phones']

# Gráfico
plt.figure(figsize=(14, 6))
plt.title("'Phones' - Lucro pelo preço de venda")
sns.scatterplot(data=query, x='sales', y='profit', hue='region', size='region', sizes=(70,70), palette='Set1')
plt.legend(title='Região')
```




    <matplotlib.legend.Legend at 0x210e1d91610>




    
![png](output_105_1.png)
    


Através do gráfico acima, vemos que a venda de 'Phones' dá prejuízo de forma majoritária na região 'East', porém é uma região que gera bastante lucro também, então talvez seja necessário adotar medidas estratégicas diferentes nessa região, com o intuito de diminuir os prejuízos e não parar com as vendas do produto.

## Além do que foi explorado
___

Este projeto de exploração de dados e extração de insights foi feito focado principalmente nos dados sobre regiões, produtos, categorias e sub-categorias, em relação ao lucro das vendas realizadas. Há muito ainda para ser explorado, muitas informações podem ser extraídas dos dados que foram o foco do projeto e também dos dados que não tiveram tanto foco assim, como por exemplo aqueles referentes às colunas 'Ship Mode', 'Segments', 'City', entre outros.  
Além disso, pode-se utilizar fórmulas estatísticas para entender melhor o conjunto dos dados e como eles estão distribuídos, e até criar modelos de predição focados em prever o lucro/prejuízo dos produtos.


```python

```
