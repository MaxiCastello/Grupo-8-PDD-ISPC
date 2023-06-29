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