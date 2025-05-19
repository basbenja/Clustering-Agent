# **Agente Autónomo de Clusterización**
Esta carpeta contiene dos archivos:
* `eda.ipynb`: notebook de análisis exploratorio de datos.
* `clustering_agent.py`: script que contiene la implementación del agente autónomo de
  clusterización.

## **Cómo correrlo**
Primero, ver los prerrequisitos enunciados en el archivo `../README.md`. Luego,
habiendo instalado las dependencias y estando en el entorno virtual, correr el
siguiente comando en la terminal:
```bash
python clustering_agent.py
```

Esto generará un nuevo archivo `iris_data_challenge_with_clusters.csv` en esta carpeta,
que contiene la base de datos con las transformaciones hechas y una nueva columna llamada
`cluster` que indica a qué cluster pertenece cada fila.

## **Análisis exploratorio**
La base de datos tiene 150 filas y 4 columnas, todas de tipo `float64`, que fueron
renombradas para una manipulación más fácil:
* `sepal length (cm)` → `sepal_length`
* `sepal width (cm)` → `sepal_width`
* `petal length (cm)`→ `petal_length`
* `petal width (cm)` → `petal_width`

Todas las columnas tienen datos faltantes:
* `sepal_length`: 11 (%7.33)
* `sepal_width`: 14 (%9.33)
* `petal_length`: 17 (%11.33)
* `petal_width`: 17 (%11.33)

La única columna que tiene valor atípicos es `sepal_width`, que solamente tiene 1.

Hay una fila repetida, que decidimos eliminarla.

Hay algunas altas correlaciones entre las variables:
* `petal_length` y `sepal_length`: 0.88
* `petal_length` y `petal_width`: 0.97

Haciendo gráficos de dispersión, se puede observar que ambas relaciones son
aproximadamente lineales.

Viendo los gráficos de densidad de las diferentes variables, se
puede observar que:
* `sepal_length` tiene una distribución levemente sesgada a la izquierda, pero en general
  simétrica alrededor de aproximadamente 5.8.
* `sepal_width` tiene una distribución simétrica centrada aproximadamente en 3.
* `petal_length` tiene una distribución bimodal con los picos en aproximadamente 1 y 5.3.
* `petal_width` tiene una distribución bimodal con los picos en aproximadamente 0.2 y 1.8.

## **Decisiones de implementación**
### **Manipulación de valores nulos**
Si elimináramos todas las filas con datos faltantes, se eliminarían 51 filas, lo cual
representa aproximadamente el 30% de la base de datos, que es bastante.

No hay correlaciones de nulidad importates, lo cual indica que los datos faltantes son aleatorios.

Hay 6 filas con 2 o más valores nulos, que representa el %4.027 de los datos. Como no es
un porcentaje alto, y además no hay correlaciones de nulidad importantes, se decidió
eliminar esas filas.

Hasta ahora, hay 143 filas y sabemos que todas las que tienen valores nulos,
tienen exactamente 1.

Como `sepal_width` tiene una distribución simétrica, reemplacé los valores
nulos por la media de la columna.

Para el resto de las columnas, y aprovechando que el dataset no es muy grande,
decidí utilizar `KNNImputer` para imputar los valores nulos. Sin embargo,
`KNNImputer` require que los datos estén en la misma escala, por lo que primero
hacemos esto.

### **Escalado de los datos**
Usamos `StandardScaler` para escalar los datos, que hace que todas las columnas
tengan una distribución normal estándar (media 0 y varianza 1).

### **Clusterización**
Como algoritmo de clusterización, utilicé `KMeans`.

#### **Determinación de la cantidad de clusters**
Para determinar la cantidad de clusters, utilizamos el método del codo, que consiste en
graficar la varianza total intra-cluster (en inglés within-cluster sum of squares, WCSS)
en función de la cantidad de clusters.

## **Supuestos asumidos**
Ninguno.