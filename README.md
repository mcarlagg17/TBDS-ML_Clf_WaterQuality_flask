# Flask Calidad del Agua

Proyecto de **Machine Learning** cuyo objetivo es implementar el mejor modelo obtenido en [repositorio Github](https://github.com/mcarlagg17/TBDS_ML_Clf_WaterQuality_flask) la creación y comparación de *modelos de clasificación* para predecir si el agua es o no es segura. Además, se implementa, el modelo de mayor *precisión*, en una aplicación flask desplegada en heroku ([repositorio flask Github](https://github.com/mcarlagg17/TBDS_ML_Clf_WaterQuality_flask))

![img](https://okdiario.com/img/2018/01/12/agua-cruda.jpg)

Para clasificar se distingue entre ***segura y no segura*** a partir de los parámetros que se muestran a continuación:  



| Variable    | description                              |
|:------------|:-----------------------------------------|
| aluminium   | dangerous if greater than 2.8            |\n
| ammonia     | dangerous if greater than 32.5           |\n
| arsenic     | dangerous if greater than 0.01           |\n
| barium      | dangerous if greater than 2              |\n
| cadmium     | dangerous if greater than 0.005          |\n
| chloramine  | dangerous if greater than 4              |\n
| chromium    | dangerous if greater than 0.1            |\n
| copper      | dangerous if greater than 1.3            |\n
| flouride    | dangerous if greater than 1.5            |\n
| bacteria    | dangerous if greater than 0              |\n
| viruses     | dangerous if greater than 0              |\n
| lead        | dangerous if greater than 0.015          |\n
| nitrates    | dangerous if greater than 10             |\n
| nitrites    | dangerous if greater than 1              |\n
| mercury     | dangerous if greater than 0.002          |\n
| perchlorate | dangerous if greater than 56             |\n
| radium      | dangerous if greater than 5              |\n
| selenium    | dangerous if greater than 0.5            |\n
| silver      | dangerous if greater than 0.1            |\n
| uranium     | dangerous if greater than 0.3            |\n
| is_safe     | class attribute {0 - not safe, 1 - safe} |

La tabla presenta el **dataset** utilizado para el estudio y creación de modelos. 

## **Estructura** del proyecto 🗿 
- ***README.md***: *archivo actual, información inicial.*
- ***proyect_resume.ipynb***: *notebook explicativo de la línea seguida en los distintos notebooks y los métodos empleados.*
- ***src***:
    - Notebooks donde se desarrolla el proyecto.
    - **data**: *lugar en el que se alamcenan los dataset, tanto modificados como original.*
    - **img**: *almacenan imagenes y figuras.*
    - **model**: 
        + *archivos pickle con los modelos entrenados*
        + model_metrics: *archivos csv con las métricas obtenidas*
    - **utils**: 
        + libreries.py: *librerias empleadas en el proyecto.*
        + utils.py: *funciones creadas para limpieza, análisis, graficar y trabajar con archivos.*
        + utilsML.py: *funciones creadas para Machine Learning.*


## Preparación 🔧

_Crear un entrono virtual y añadir las librerías mínimas para ejecutar este proyecto:_

* Creación del entorno:

```
>> conda create -n nombre_enviroment python==3.9.12

>> conda activate nombre_enviroment
```
* Instalar librerías:

Una vez creado el entorno, colocándonos en la carpeta *utils* dentro de *src* instalamos las librerías mínimas necesarias.

```
>> pip install -r requirements.txt
```

## *Consejos de uso* 🤓

*Leer el archivo <a href='proyect_resume.ipynb'>proyect_resume.ipynb</a> para tener una idea de la línea seguida y los resultados obtenidos.*

## Autora 👩🏽‍💻

* **María Carla González González** - [mcarlagg17](https://github.com/mcarlagg17)

## Tutores 👨‍🏫

* **Marco Russo** - [marcusRB](https://github.com/marcusRB) 
* **Daniel Montes** - [DanielMontes](https://linkedin.com/in/daniel-montes-serrano-a81b9447)
* **Juan Maniglia** - [JuanManiglia](https://github.com/JuanManiglia)


## Agradecimientos 🤗

> A todxs los que de una forma u otra habéis formado parte de este viaje. Deseo lo mejor para cada uno de vosotrxs. 
 
> *¡Gracias de corazón!*




---
***Proyecto final Bootcamp Data Science***

---

![img](./src/img/logo.jpg)