import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

#Carga del Dataset;
df = pd.read_csv("./dataset/heart.csv")
df.head()

# METRICAS BÁSICAS
df.describe()

# DISTRIBUCIÓN DE LA EDAD:
edad_dist = (20, 5)
edad_dist, ax2 = plt.subplots(figsize=edad_dist)
ax2 = sns.countplot(x=df['Age'])
plt.show()
## La edad en el dataset va de 28 a 77, siendo el grupo de 50 a 60 el rango etáreo que más cantidad de personas contiene.

# DISTRIBUCION DEL COLESTEROL: 
sns.displot(x=df['Cholesterol'], bins=30)
sns.show()
## Se ve que hay muchisimos registros con valor igual a 0 para ésta variable. Habria que analizar si hay pacientes con colesterol igual a 0, o si es un error del dataset

# CANTIDAD DE PERSONAS QUE PRESENTAN COLESTEROL 0
colesterol_0 = df[df['Cholesterol']==0]
print(" La cantidad de pacientes que presentan niveles de colesterol 0 son: ",colesterol_0.Cholesterol.count())
