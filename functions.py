import pandas as pd

def read_data(url):
    # Esta función lee los csv importados
    df = pd.read_csv(url)
    return df

def clean_original_data(df):
    # Elimina el valor total de la columna sex, en el DataFrame original
    df = df[df["sex"] != "Total"]
    df["sex"].unique()
    return df

def new_df_country(df):
    #Crea un nuevo DataFrame a partir de la columna country
    country1 = {
            'id_country': ["AT", "BE", "BG", "CH", "CY", "CZ", "DE", "DK", "EE", "EL", "ES", "FI", "FR", 
               "HR", "HU", "IE", "IS", "IT", "LT", "LV","MK", "NL", "NO", "PL", "PT", "RO", "RS", "SE", "SI", "SK", "TR", "UK"],  # Valores para id_country
         }

    # Crear el DataFrame
    country = pd.DataFrame(country1)
    
    country["country_name"]= df["country"].unique()
    return country

def new_df_gender(df):
    gender1 = {'id_gender': ["F", "M"]}
    gender = pd.DataFrame(gender1)
    gender["gender"] = df["sex"].unique()
    return gender

def new_df_level(df):
    level = {'id_level': ['ESO', 'BACH-FP', 'BACH', 'FP', 'UNIVERSIDAD']}
    level_education = pd.DataFrame(level)
    level_education["valor_educacion"] = df["valor_educacion"].unique()
    return level_education

def convert_gender(gender):
    #Añade valores a la nueva columna id_gender 
    if gender == 'Females':
        return 'F'
    elif gender == 'Males':
        return 'M'
    else:
        return 'Unknown'  # En caso de que haya otros valores


def colum_id_map(df):
    #Crea una nueva columna llamada id_country
    country_map = {
    'Austria': 'AT', 'Belgium': 'BE', 'Bulgaria': 'BG', 'Switzerland': 'CH', 
    'Cyprus': 'CY', 'Czechia': 'CZ', 'Germany': 'DE', 'Denmark': 'DK', 
    'Estonia': 'EE', 'Greece': 'EL', 'Spain': 'ES', 'Finland': 'FI', 
    'France': 'FR', 'Croatia': 'HR', 'Hungary': 'HU', 'Ireland': 'IE', 
    'Iceland': 'IS', 'Italy': 'IT', 'Lithuania': 'LT', 'Latvia': 'LV', 
    'North Macedonia': 'MK', 'Netherlands': 'NL', 'Norway': 'NO', 
    'Poland': 'PL', 'Portugal': 'PT', 'Romania': 'RO', 'Serbia': 'RS', 
    'Sweden': 'SE', 'Slovenia': 'SI', 'Slovakia': 'SK', 'Türkiye': 'TR', 
    'United Kingdom': 'UK'
    }
    df['id_country'] = df['country'].map(country_map)
    return df

def rename_column_and_new_column(df):
    #Renombra la columna level_education por id_level y crea una nueva columna llamada id_datos
    df.rename(columns = {"level_education": "id_level"}, inplace = True)
    df['id_datos'] = range(1, len(df) + 1)
    return df

def new_df_datos(df):
    #Crea un nuevo DataFrame
    datos_edu = df[["id_datos", "indice_educativo", "value_unemployment", "value_education", "year", "id_country", "id_gender", "id_level"]]
    return datos_edu