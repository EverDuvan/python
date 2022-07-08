import os
from dotenv import load_dotenv
load_dotenv()

# como importar datos de un diccionario de diccionanrios en un archivo .env
# (data1 =primer ejemplo, data_2 = segundo ejemplo, data_3 = tercer ejemplo)

a = eval(os.getenv("basesdedatos"))
credentials=a['data_2']
print (credentials['DB_USER'], credentials['DB_PASS'], credentials['DB_IP'], credentials['DB_PORT'], credentials['DB_NAME'])


