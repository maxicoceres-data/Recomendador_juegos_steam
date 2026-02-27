# Steam Analisis

Proyecto de análisis de datos de Steam y construcción de un recomendador de juegos basado en similitud.

## Objetivo

Este repositorio busca:

- Explorar y limpiar datos de uso/juego de Steam.
- Transformar los datos para construir una matriz usuario-juego.
- Aplicar técnicas de Machine Learning (SVD + similitud del coseno).
- Generar recomendaciones de juegos similares.
- Documentar hallazgos en un reporte HTML.

## Tecnologías

- Python 3.10+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jinja2
- streamlit (incluido en dependencias)
- ipykernel (para notebooks)

## Estructura del proyecto

```text
steam_analisis/
├── data/
│   ├── raw/
│   │   ├── csv_optimo.csv
│   │   └── steam-200k.csv
│   └── processed/
├── notebooks/
│   ├── 01_eda_y_limpieza.ipynb
│   └── 02_modelo_recomendacion.ipynb
├── reports/
│   ├── reporte_steam.html
│   └── figures/
├── src/
│   ├── steam_analisis/
│   │   ├── iniciar_dataframe.py
│   │   └── reporte.py
│   ├── features/
│   ├── models/
│   └── visualization/
├── requirements.txt
├── pyproject.toml
└── fases_proyecto.md
```

## Instalación

1. Crear y activar entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

Opcional (modo editable del paquete):

```bash
pip install -e .
```

## Flujo recomendado

### 1) EDA y limpieza

Abrir y ejecutar:

- `notebooks/01_eda_y_limpieza.ipynb`

En esta fase se inspeccionan datos, distribuciones y calidad de variables.

### 2) Modelo de recomendación

Abrir y ejecutar:

- `notebooks/02_modelo_recomendacion.ipynb`

Pasos principales implementados:

- Lectura de `data/raw/csv_optimo.csv`.
- Transformación logarítmica de `value` con `np.log1p`.
- Creación de matriz pivote `game-title` x `user-id`.
- Reducción de dimensionalidad con `TruncatedSVD`.
- Cálculo de similitud con `cosine_similarity`.
- Función `recomendador(...)` para devolver juegos similares.

## Uso rápido de la función de recomendación

Dentro del notebook del modelo:

```python
recomendador(similitary_df, "12 Labours of Hercules", 7)
```

## Generación de reporte HTML

En `src/steam_analisis/reporte.py` existe la función `reporte(...)` para construir un reporte con plantillas Jinja2 y figuras.

Salida esperada en:

- `reports/reporte_steam.html`

## Módulos útiles en `src`

- `iniciar_dataframe.py`:
  - Función `informacion_df(datos)` para inspección rápida de DataFrames o archivos (`.csv`, `.xlsx`, `.xls`, `.sql`).
- `reporte.py`:
  - Función `reporte(...)` para generar un HTML con gráficos e insights.

## Próximas mejoras sugeridas

- Validar entrada en `recomendador` cuando un juego no exista en el índice.
- Guardar artefactos del modelo en `models/`.
- Agregar script/CLI para ejecutar el pipeline sin notebook.
- Publicar una app con Streamlit para consultar recomendaciones.

## Licencia

MIT (según `pyproject.toml`).
