from jinja2 import Template
import os

def reporte(nombre_archivo,titulo,carpeta_fotos,lista_fotos,destino_reporte, insights):
    template = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{reporte_titulo}}</title>
    <style>
        :root {
            --steam-dark: #171a21;
            --steam-blue: #1b2838;
            --steam-light-blue: #66c0f4;
            --text-color: #c7d5e0;
            --card-bg: #2a475e;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--steam-dark);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }

        header {
            text-align: center;
            padding-bottom: 40px;
            border-bottom: 2px solid var(--card-bg);
            margin-bottom: 40px;
        }

        h1 {
            color: white;
            font-size: 2.5rem;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .galeria {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .item-foto {
            background-color: var(--steam-blue);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
            border: 1px solid rgba(102, 192, 244, 0.1);
            width:100%;
        }

        .item-foto:hover {
            transform: translateY(-5px);
            border-color: var(--steam-light-blue);
        }

        .item-foto img {
            width: 100%;
            height: auto;
            display: block;
            border-bottom: 4px solid var(--card-bg);
        }

        .item-foto h2 {
            padding: 15px;
            margin: 0;
            font-weight: bold;
            text-align: center;
            background: var(--card-bg);
            color: white;
            font-size: 1.5rem;
            text-transform:uppercase;
        }
        
        .insight-box{
            padding:2em;
            text-align:center;
            background:var(--card-bg);
            color:white;
            font-size:1.1rem;
        }

        /* Pie de página o Info adicional */
        .footer-note {
            text-align: center;
            margin-top: 50px;
            font-size: 0.8rem;
            color: #566471;
        }
    </style>
</head>
<body>
    <header>
        <h1>Reporte Juegos de Steam</h1>
    </header>
    <div class="galeria">
        {% for foto in fotos %}
    <div class="item-foto">
        <h2 class="titulo-grafico">{{foto | replace("_"," ") | replace(".png"," ") | title}}</h2>
        <img src="{{ruta}}/{{foto}}" alt="Imagen {{loop.index}}"   />
        
        <div class="insight-box">
                    <strong>Análisis:</strong> 
                    {# Usamos .get para que si no existe el nombre exacto, no falle #}
                    {{ insights.get(foto, "No se encontró un análisis para este gráfico.") }}
                </div>
        
    </div>
        {%endfor%}
    </div>   
</body>
</html>
    """
    
    plantilla = Template(template)
    
    contenido_html = plantilla.render(
        reporte_titulo = titulo,
        ruta = carpeta_fotos,
        fotos = lista_fotos,
        destino_reporte = destino_reporte,
        insights = insights
         
    )
    
    carpeta_destino = destino_reporte 
    
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
        
    ruta_completa = os.path.join(carpeta_destino,nombre_archivo)
    
    
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write(contenido_html)
        
    print(f"Archivo {nombre_archivo}, fue creado con exito.")