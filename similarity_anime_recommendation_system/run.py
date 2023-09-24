# Bibliotecas
import pandas as pd
from processing import Processing
from interface import Interface
from constants import *

# Pré-processamento da base
data, data_aux = Processing.preprocessing_csv(INFO_ANIMES_CSV)
dash = Interface(data, data_aux)
