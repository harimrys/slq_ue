# **Project UE MySQL**

## Descripción
Este proyecto utiliza una base de datos conformada por datos extraídos de dos archivos CSV de Eurostat:

- [Young people by educational attainment level, sex and age](https://ec.europa.eu/eurostat/databrowser/view/yth_demo_040/default/bar?lang=en&category=chldyth.yth.yth_educ) 
- [Youth unemployment by sex, age and educational attainment level](https://ec.europa.eu/eurostat/databrowser/view/yth_empl_090__custom_12827409/default/bar?lang=en)

Los datos son limpiados y organizados en dataframes más pequeños para su posterior envío a MySQL Workbench. Una vez cargados los datos en MySQL, se realizan varias queries utilizando distintos métodos como `JOIN`, `GROUP BY`, `WHERE`, `ORDER BY`, `CASE`, entre otros.

Después de ejecutar las queries, los resultados son importados nuevamente a Python, donde se visualizan a través de gráficos utilizando librerías como Seaborn y Matplotlib. Además, en MySQL Workbench se ha diseñado un esquema relacional que conecta todas las tablas mediante claves primarias (primary keys) y claves foráneas (foreign keys).

En este repositorio se encuentran los siguientes archivos:
- Un notebook de Jupyter para la limpieza y creación de dataframes.
- Un archivo Python que contiene las funciones necesarias para la creación de tablas.
- Un notebook de Jupyter que importa las queries y genera los gráficos.
- Un archivo Python que contiene las funciones necesarias para ejecutar las queries y crear los gráficos.
- Un archivo SQL con las queries originales.
- Un archivo del esquema de las tablas en SQL.

## Requisitos
Para ejecutar este proyecto, necesitarás las siguientes herramientas y librerías:
- Python 3.x
- MySQL Workbench
- Pandas
- Seaborn
- Matplotlib
- MySQL Connector para Python

## Esquema de la Base de Datos
Este proyecto incluye un esquema relacional de las tablas en MySQL, conectadas mediante **primary keys** y **foreign keys**. El archivo del esquema se encuentra en el repositorio bajo el nombre `db_schema.sql`.

## Proyecto de Clase
Este es un proyecto realizado en el curso de **Ironhack**, como parte del aprendizaje sobre el uso de MySQL. 

[Enlace a la presentación](#)

## Autoras
- **Haridian Morays**
- **Cristina Ramírez**
