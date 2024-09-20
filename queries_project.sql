USE project_ue;

-- Calcular la media del índice educativo por género uniendo las tablas gender y datos_educativos

SELECT g.gender AS gender, ROUND(AVG(d.indice_educativo), 2) AS avg_edu 
FROM project_ue.gender AS g
LEFT JOIN project_ue.datos_educativos AS d
ON  d.id_gender = g.id_gender
GROUP BY g.gender
ORDER BY avg_edu DESC;

-- Calcular la media del índice educativo por país uniendo las tablas country y datos_educativos

SELECT c.country_name AS country, ROUND(AVG(d.indice_educativo), 2) AS avg_edu 
FROM project_ue.country AS c
LEFT JOIN project_ue.datos_educativos AS d
ON  d.id_country = c.id_country
GROUP BY c.country_name
ORDER BY avg_edu DESC;



-- Calcular la media de la tasa de desempleo por género uniendo las tablas gender y datos_educativos

SELECT g.gender AS gender, ROUND(AVG(d.value_unemployment), 2) AS avg_unem
FROM project_ue.gender AS g
LEFT JOIN project_ue.datos_educativos AS d
ON  d.id_gender = g.id_gender
GROUP BY g.gender
ORDER BY avg_unem DESC;


-- Calcular la media de la tasa de desempleo por nivel de educación uniendo las tablas level_education y datos_educativos

SELECT d.id_level AS level_education, ROUND(AVG(d.value_unemployment), 2) AS avg_unem
FROM project_ue.datos_educativos AS d
GROUP BY d.id_level
ORDER BY avg_unem DESC;

-- Calcular el promedio del índice educativo y la tasa de desempleo por año
SELECT d.year AS year, ROUND(AVG(d.value_unemployment), 2) AS avg_unem, ROUND(AVG(d.indice_educativo), 2) AS avg_edu
FROM project_ue.datos_educativos AS d
GROUP BY d.year
ORDER BY avg_unem DESC;

-- Calcular la desviación del índice educativo

SELECT ROUND(STDDEV_POP(d.indice_educativo), 2) AS desviacion_tipica
FROM project_ue.datos_educativos AS d;

-- Sacar el país con el máximo índice educativo y el que tenga el mínimo
-- País con el valor mínimo del indice_educativo
SELECT 
    c.country_name AS country, 
    MIN(d.indice_educativo) AS minimum
FROM 
    project_ue.country AS c
LEFT JOIN 
    project_ue.datos_educativos AS d
ON  
    d.id_country = c.id_country
WHERE 
    d.indice_educativo = (SELECT MIN(d2.indice_educativo) 
                          FROM project_ue.datos_educativos AS d2)
GROUP BY 
    c.country_name;

-- País con el valor máximo del indice_educativo
SELECT 
    c.country_name AS country, 
    MAX(d.indice_educativo) AS maximum
FROM 
    project_ue.country AS c
LEFT JOIN 
    project_ue.datos_educativos AS d
ON  
    d.id_country = c.id_country
WHERE 
    d.indice_educativo = (SELECT MAX(d2.indice_educativo) 
                          FROM project_ue.datos_educativos AS d2)
GROUP BY 
    c.country_name;
    

-- Clasificar los países por su nivel educativo 

SELECT c.country_name AS country, 
	ROUND(AVG(d.indice_educativo), 2) AS avg_edu, 
	CASE 
        WHEN AVG(d.indice_educativo) < 2 THEN 'Nivel educativo bajo'
        WHEN AVG(d.indice_educativo) BETWEEN 2 AND 3 THEN 'Nivel educativo medio'
        ELSE 'Nivel educativo alto'
    END AS categoria_educativa
FROM project_ue.country AS c
LEFT JOIN project_ue.datos_educativos AS d
ON  d.id_country = c.id_country
GROUP BY c.country_name
ORDER BY avg_edu DESC;