
def recomendador(sim_df,juego, n=6):
    
    #convierto los juegos en minusculas
    juego = juego.lower()
    
    indice_juego = sim_df.index.get_loc(juego)
    
    juegos_recomendados = sim_df.iloc[indice_juego].sort_values(ascending=False)
    
    top5_juegos_recomendados = juegos_recomendados[1:n+1]
    
    top5_juegos_recomendados.index.to_list()
    
    return top5_juegos_recomendados