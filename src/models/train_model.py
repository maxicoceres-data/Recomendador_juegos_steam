import pandas as pd 
import numpy as np 
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD


from pathlib import Path


#Creo ruta del csv optimo
data_folder = Path("../data/raw/")
data_processed_folder = Path("../data/processed/")
datos = data_folder / "csv_optimo.csv"

#vatriable para leer el csv 
df_optimo = pd.read_csv(datos)

#hago el log de los valores para optimizrlos
df_optimo["value_log"]=np.log1p(df_optimo['value'])

#pongo en minusculas los nombres de los titulos para que la busqueda sea mejor
df_optimo["game-title"] = df_optimo["game-title"].str.lower()

#creo el pivot y relleno los nan con 0
df_pivot = pd.pivot_table(df_optimo,index="game-title", columns="user-id", values="value_log")
df_pivot = df_pivot.fillna(0)


#hago el trucated para que el aprendizaje sea mas optimo con 75 componentes.
svd = TruncatedSVD(n_components=75, random_state=42)
matriz_comprimida = svd.fit_transform(df_pivot)

#hacemos la matrix y el dataframe de similitud
similarity_matrix=cosine_similarity(matriz_comprimida)
similitary_df = pd.DataFrame(similarity_matrix, index=df_pivot.index, columns=df_pivot.index)


#creo la serializacion de los datos.
with open(data_processed_folder / "similitary.pkl","wb") as archivo:
    pickle.dump(similitary_df, archivo)

