import streamlit as st 
import pickle
from pathlib import Path
from src.models.recomendador import recomendador


BASE_DIR = Path.cwd()

data_processed_similitary = BASE_DIR / "data" / "processed" / "similitary.pkl"

@st.cache_data
def cargar_datos():
    if not data_processed_similitary.exists():
        st.error(f"No se encontró el archivo en: {data_processed_similitary}")
        st.stop()

    with open(data_processed_similitary, "rb") as f:
        matriz = pickle.load(f)

    return matriz



sim_df = cargar_datos()


st.title("Recomendador de juegos en Steam")

opciones = sim_df.index.to_list()

seleccion = st.selectbox("Seleccione un juego:", opciones, index=None,placeholder="--- Escribe para buscar un juego ---",label_visibility="hidden")
    
boton_recomendar = st.button("¡Recomendar Juegos!")


if boton_recomendar and seleccion:
    st.subheader(f"Si te gusta {seleccion} te recomendamos: ")
        
    lista_recomendados = recomendador(sim_df,seleccion)

    columnas = st.columns(2, gap="medium")
    for i, (juego,score) in enumerate(lista_recomendados.items()):
        with columnas[i % 2]:
            with st.container(border=True):
                st.markdown(f"### 🎮 {juego}")
                st.caption(f"Similitud: {score:.3f}")