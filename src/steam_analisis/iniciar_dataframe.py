import pandas as pd
from pathlib import Path
from IPython.display import display


def informacion_df(datos):
    if isinstance(datos, pd.DataFrame):
        df = datos
    else:
        # Ruta del dataframe
        ruta = Path(datos)

        try:
            # validamos el prefijo del archivo para saber como leerlo.
            if ruta.suffix == ".csv":
                df = pd.read_csv(datos)
            elif ruta.suffix in [".xlsx", ".xls"]:
                df = pd.read_excel(datos)
            elif ruta.suffix == ".sql":
                df = pd.read_sql(datos)
            else:
                raise ValueError("Extensión no soportada")
        except ValueError:
            print("La extension no es válida o no esta cargada aun")
            return None

    # Mostrar por bloques
    print("▶ Head (5 filas):")
    display(df.head(5))
    
    print("▶ Tail (5 filas):")
    display(df.tail(5))

    print("\n▶ Info del DataFrame:")
    df.info()

    print("\n▶ Dimensiones (shape):")
    print(df.shape)

    print("\n▶ Columnas:")
    print(df.columns.to_list())

    print("\n▶ Descripción estadística (describe numérico):")
    display(df.describe())

    print("\n▶ Tipos de datos:")
    print(df.dtypes)

    return df
