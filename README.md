# Grupo-8-PDD-ISPC

Grupo 8, trabajo grupal de la catedra procesamiento de datos del ISPC.

- Gabriel Arriola - sala 1
- Ivan Didier Meier - sala 1
- Maximimliano Casello - Sala 2
- Carol Peves - sala 1
- Margarita Turrin - sala 1
- Silva Mercedes - sala 2
- Rodolfo Paz - sala 2

Este proyecto tiene como objetivo aplicar los conceptos aprendidos en Procesamiento de Datos para realizar el análisis de un conjunto de datos seleccionado. 
Las etapas del proyecto incluyen la recolección y preparación de los datos, el análisis exploratorio, el procesamiento y análisis de los datos, la visualización de resultados y la comunicación efectiva de los hallazgos.
En este proyecto, se realizó un análisis de un conjunto de datos sobre enfermedades cardíacas. El dataset utilizado se obtuvo de Kaggle y se puede encontrar en el siguiente enlace: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset.

Para llevar a cabo el análisis, se importaron las siguientes librerías: pandas, matplotlib.pyplot y seaborn. Estas herramientas proporcionaron las funcionalidades necesarias para la carga de datos, visualización y análisis.

El dataset se cargó utilizando el método read_csv de la librería pandas. Los datos se almacenaron en el DataFrame df. A continuación, se realizó una verificación de los datos cargados mediante la visualización de las primeras 10 filas con el comando df.head(10).

Posteriormente, se verificaron los tipos de datos de cada columna con el comando df.dtypes. Esto permitió conocer el tipo de dato de cada variable presente en el dataset.

Se realizó también una verificación de la presencia de datos faltantes en el dataset utilizando el comando df.isnull().sum(). Afortunadamente, no se encontraron valores faltantes en ninguna columna.

Para obtener algunas métricas básicas sobre el dataset, se utilizó el comando df.describe(). Esto proporcionó estadísticas resumidas, como el recuento, la media, la desviación estándar y los valores mínimo y máximo de cada columna.

A continuación, se realizaron análisis más específicos sobre ciertas variables del dataset.

Se examinó la distribución de la edad de los pacientes mediante un gráfico de barras utilizando la librería seaborn. El gráfico mostró que el rango etario de 50 a 60 años tenía la mayor cantidad de personas en el estudio.

Se analizó también la distribución del colesterol mediante un histograma utilizando seaborn. Se observó que había muchos registros con un valor de colesterol igual a 0. Se sugirió investigar si este valor nulo es un error en el dataset o si realmente existen pacientes con colesterol igual a 0.

Se investigó la proporción de género en el dataset mediante un gráfico de pastel utilizando matplotlib. Se encontró que el 68.3% de los pacientes eran hombres, mientras que el 31.7% eran mujeres.

Se examinó la distribución de género entre los pacientes con enfermedad cardíaca y los pacientes sin enfermedad cardíaca mediante un gráfico de barras utilizando seaborn. Se concluyó que, según el conjunto de datos analizado, había una mayor prevalencia de enfermedad cardíaca entre los hombres en comparación con las mujeres.

Se exploró la relación entre el género y el tipo de dolor de pecho mediante un gráfico de barras apiladas utilizando pandas y matplotlib. Se encontró que la mayoría de las personas no presentaban dolor en el pecho.

Finalmente, se investigó la relación entre el género y el grupo etario de los pacientes mediante un gráfico de barras utilizando pandas y matplotlib. Se observó que el grupo etario con mayor cantidad de personas en el estudio era de 53 a 64 años.

Durante el desarrollo del análisis de enfermedades cardíacas, se identificaron algunos problemas y dificultades que se presentaron, así como las soluciones correspondientes. Estos son algunos de los desafíos encontrados y cómo se abordaron:

Calidad de los datos: Uno de los desafíos comunes al trabajar con conjuntos de datos es asegurar la calidad de los datos. En este caso, se encontraron algunos registros con valores de colesterol igual a cero, lo cual es inusual y puede indicar un error en los datos o información faltante. Para abordar esto, se sugirió investigar la causa de estos valores nulos o verificar con expertos en el dominio si es posible que existan pacientes con colesterol igual a cero.

Interpretación de los resultados: Al realizar el análisis y presentar los resultados, es importante tener en cuenta las limitaciones del conjunto de datos y las conclusiones que se pueden extraer. En este caso, se realizaron observaciones y se presentaron hallazgos basados en los datos disponibles, pero se debe tener en cuenta que estos resultados se aplican específicamente a este conjunto de datos y pueden no ser generalizables a la población en general.
