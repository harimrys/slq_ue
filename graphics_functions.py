import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_avg_education_pie_by_gender(engine):
    # Consulta SQL
    consulta = """
    SELECT g.gender AS gender, 
           ROUND(AVG(d.indice_educativo), 2) AS avg_edu  
    FROM project_ue.gender AS g 
    LEFT JOIN project_ue.datos_educativos AS d 
    ON d.id_gender = g.id_gender 
    GROUP BY g.gender 
    ORDER BY avg_edu DESC
    """
    
    # Ejecutar la consulta y obtener los datos en un DataFrame
    avg_gender_edu = pd.read_sql(consulta, con=engine)

    # Verificar el DataFrame
    print(avg_gender_edu)

    # Asignar colores según el género
    colors = ['#ff6699' if gender == 'Females' else '#6699ff' for gender in avg_gender_edu['gender']]

    # Creación del gráfico de pastel
    plt.figure(figsize = (8, 8))
    plt.pie(avg_gender_edu['avg_edu'], 
            labels = avg_gender_edu['gender'], 
            autopct = '%1.1f%%', 
            startangle = 90, 
            colors = colors, 
            wedgeprops = {'edgecolor': 'black'})

    # Añadir título
    plt.title('Promedio del Índice Educativo por Género')

    # Mostrar el gráfico
    plt.axis('equal')  # Asegurar que el gráfico sea un círculo perfecto
    plt.show()

def plot_avg_education_by_country(engine):
    # Consulta SQL
    consulta = """
    SELECT c.country_name AS country, 
           ROUND(AVG(d.indice_educativo), 2) AS avg_edu  
    FROM project_ue.country AS c 
    LEFT JOIN project_ue.datos_educativos AS d 
    ON d.id_country = c.id_country 
    GROUP BY c.country_name 
    ORDER BY avg_edu DESC
    """
    
    # Ejecutar la consulta y obtener los datos en un DataFrame
    avg_country_edu = pd.read_sql(consulta, con = engine)

    # Verificar el DataFrame
    print(avg_country_edu)

    # Creación del gráfico de barras
    plt.figure(figsize = (10, 6))
    sns.barplot(x = 'avg_edu', y = 'country', hue = 'country', data = avg_country_edu, palette = 'coolwarm', legend = False)

    # Añadir etiquetas y título
    plt.title('Promedio del Índice Educativo por País')
    plt.xlabel('Promedio del Índice Educativo')
    plt.ylabel('País')

    # Mostrar el gráfico
    plt.show()

def plot_avg_unemployment_by_gender(engine):
    # Consulta SQL
    consulta = """
    SELECT g.gender AS gender, 
           ROUND(AVG(d.value_unemployment), 2) AS avg_unem 
    FROM project_ue.gender AS g 
    LEFT JOIN project_ue.datos_educativos AS d 
    ON d.id_gender = g.id_gender 
    GROUP BY g.gender 
    ORDER BY avg_unem DESC
    """
    
    # Ejecutar la consulta
    avg_gender_unem = pd.read_sql(consulta, con = engine)

    # Verificar el DataFrame
    print(avg_gender_unem)

    # Creación del gráfico de barras
    plt.figure(figsize=(8, 5))
    sns.barplot(x = 'gender', y = 'avg_unem', hue = 'gender', data = avg_gender_unem, palette = 'magma', legend = False)

    # Añadir etiquetas y título
    plt.title('Promedio de la Tasa de Desempleo por Género')
    plt.xlabel('Género')
    plt.ylabel('Promedio de Tasa de Desempleo')

    # Mostrar el gráfico
    plt.show()


def plot_avg_unemployment_by_education_level(engine):
    # Consulta SQL
    consulta = """
    SELECT d.id_level AS level_education, 
           ROUND(AVG(d.value_unemployment), 2) AS avg_unem 
    FROM project_ue.datos_educativos AS d 
    GROUP BY d.id_level 
    ORDER BY avg_unem DESC
    """
    
    # Ejecutar la consulta y obtener los datos en un DataFrame
    avg_leveledu_unem = pd.read_sql(consulta, con=engine)

    # Verificar el DataFrame
    print(avg_leveledu_unem)

    # Creación del gráfico de barras
    plt.figure(figsize = (10, 6))
    sns.barplot(x = 'avg_unem', y = 'level_education', hue = 'level_education', data = avg_leveledu_unem, palette = 'viridis', legend = False)

    # Añadir etiquetas y título
    plt.title('Promedio de la Tasa de Desempleo por Nivel Educativo')
    plt.xlabel('Promedio de Tasa de Desempleo')
    plt.ylabel('Nivel Educativo')

    # Mostrar el gráfico
    plt.show()


def plot_avg_unemployment_and_education_by_year(engine):
    # Consulta SQL
    consulta = """
    SELECT d.year AS year, 
           ROUND(AVG(d.value_unemployment), 2) AS avg_unem, 
           ROUND(AVG(d.indice_educativo), 2) AS avg_edu 
    FROM project_ue.datos_educativos AS d 
    GROUP BY d.year 
    ORDER BY year
    """
    
    # Ejecutar la consulta y obtener los datos en un DataFrame
    avg_edu_unem = pd.read_sql(consulta, con=engine)

    # Verificar el DataFrame
    print(avg_edu_unem)

    # Creación del gráfico de líneas
    plt.figure(figsize = (12, 6))
    sns.lineplot(x = 'year', y = 'avg_unem', data = avg_edu_unem, label = 'Promedio de Tasa de Desempleo', color = 'blue', marker = 'o')
    sns.lineplot(x = 'year', y = 'avg_edu', data = avg_edu_unem, label = 'Promedio del Índice Educativo', color = 'orange', marker = 'o')

    # Añadir etiquetas y título
    plt.title('Promedio de la Tasa de Desempleo y del Índice Educativo a lo Largo de los Años')
    plt.xlabel('Año')
    plt.ylabel('Valores Promedios')
    plt.legend()

    # Mostrar el gráfico
    plt.grid(True)  # Añadir cuadrícula para mejor visualización
    plt.show()


def plot_avg_education_by_country2(engine):
    # Consulta SQL
    consulta = """
    SELECT c.country_name AS country, 
           ROUND(AVG(d.indice_educativo), 2) AS avg_edu, 
           CASE 
               WHEN AVG(d.indice_educativo) < 2 THEN 'Nivel educativo bajo' 
               WHEN AVG(d.indice_educativo) BETWEEN 2 AND 3 THEN 'Nivel educativo medio' 
               ELSE 'Nivel educativo alto' 
           END AS categoria_educativa 
    FROM project_ue.country AS c 
    LEFT JOIN project_ue.datos_educativos AS d ON d.id_country = c.id_country 
    GROUP BY c.country_name 
    ORDER BY avg_edu DESC
    """
    
    # Leer la consulta SQL en un DataFrame
    category_country = pd.read_sql(consulta, con=engine)

    # Verificar el DataFrame
    print(category_country)

    # Creación del gráfico de barras
    plt.figure(figsize = (12, 8))
    sns.barplot(x = 'avg_edu', y = 'country', hue = 'categoria_educativa', data = category_country, palette = 'pastel')

    # Añadir etiquetas y título
    plt.title('Promedio del Índice Educativo por País')
    plt.xlabel('Promedio del Índice Educativo')
    plt.ylabel('País')

    # Mostrar el gráfico
    plt.legend(title = 'Categoría Educativa')
    plt.grid(axis='x')  # Añadir cuadrícula para mejor visualización
    plt.show()























