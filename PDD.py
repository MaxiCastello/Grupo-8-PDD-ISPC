import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#Carga del Dataset;
df = pd.read_csv("./dataset/heart.csv")

# Verificación de los datos cargados
print(df.head())

# Verificación de los tipos de datos de las columnas
print(df.dtypes)

# Verificación de datos faltantes en cada columna
print(df.isnull().sum())

# METRICAS BÁSICAS
df.describe()

# DISTRIBUCIÓN DE LA EDAD:
edad_dist = (20, 5)
edad_dist, ax2 = plt.subplots(figsize=edad_dist)
ax2 = sns.countplot(x=df['age'])
plt.show()
## La edad en el dataset va de 28 a 77, siendo el grupo de 50 a 60 el rango etáreo que más cantidad de personas contiene.

# DISTRIBUCION DEL COLESTEROL: 
sns.displot(x=df['chol'], bins=30)
plt.show()
## Se ve que hay muchisimos registros con valor igual a 0 para ésta variable. Habria que analizar si hay pacientes con colesterol igual a 0, o si es un error del dataset

# CANTIDAD DE PERSONAS QUE PRESENTAN COLESTEROL 0
colesterol_0 = df[df['chol']==0]
print(" La cantidad de pacientes que presentan niveles de colesterol 0 son: ",colesterol_0.chol.count())


# PROPORCIÓN DEL GENERO
gender_counts = df['sex'].value_counts()
plt.pie(gender_counts, labels=['Hombres', 'Mujeres'], autopct='%1.1f%%')
plt.title('Proporción de género')
plt.show()
# print(gender_counts)
## De los pacientes a quienes se les realizó el estudio, el 31.7%, es decir 96 pacientes eran mujeres y el 68.3%, corrspondiente a 207 pacientes eran hombres.


# DISTRIBUCIÓN DE GÉNERO ENTRE PACIENTES CON ENFERMEDAD Y SIN ENFERMEDAD :

# Reemplazar los valores de la columna 'Sex' con etiquetas personalizadas
df['sex'] = df['sex'].replace({0: 'Mujeres', 1: 'Hombres'})

# Calcular la distribución de género para cada valor de target
gender_target_distribution = df.groupby(['sex', 'target']).size().reset_index(name='Count')

# Mapear los valores de target a las categorías "Enfermo" y "No Enfermo"
gender_target_distribution['target'] = gender_target_distribution['target'].map({0: 'Enfermo', 1: 'No Enfermo'})

# Crear el gráfico de barras para la distribución de género
plt.figure(figsize=(8, 5))
sns.barplot(x='sex', y='Count', hue='target', data=gender_target_distribution, palette='Set2')

# Agregar etiquetas a las barras
for p in plt.gca().patches:
    height = p.get_height()
    plt.gca().annotate(f"{height}", (p.get_x() + p.get_width() / 2, height),
        ha='center', va='bottom')

# Configurar título y etiquetas de ejes
plt.title('Distribución de Género según el Estado de Enfermedad')
plt.xlabel('Género')
plt.ylabel('Cantidad')

plt.show()

'''
Podemos observar que entre los pacientes con enfermedad, los hombres tienen una mayor proporción en comparación con las mujeres.
Es decir, según el conjunto de datos analizado, hay una mayor prevalencia de enfermedad cardíaca entre los hombres en comparación con las mujeres.'''