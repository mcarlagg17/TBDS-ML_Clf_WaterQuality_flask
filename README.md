# Flask Calidad del Agua

Implementación del mejor modelo de **Machine Learning** ([repositorio de proyecto ML](https://github.com/mcarlagg17/TBDS_ML_Clf_WaterQuality)). El objetivo es **clasificar si el agua es o no es segura**. 
Se realiza el despliegue en heroku, utilizando *flask*.

![img](https://okdiario.com/img/2018/01/12/agua-cruda.jpg)

Se distingue entre ***segura y no segura*** a partir de los parámetros que se muestran a continuación:  



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

*La tabla presenta las **variables a introducir mediante un csv** para realizar la predicción con el modelo entrenado.*

Pudiendo comprobar un dataset con u

## **Estructura** del proyecto flask 🗿 
- ***README.md***: *archivo actual, información inicial.*
- ***app_model.py***: *archivo python que contiene las acciones de la aplicación.*
- ***static***:
    - cover.css: indicaciones generales de gráficos.
- ***templates***: archivos con las distintas pantallas.
- *data/example*: *archivos csv de ejemplo.*
- *img*: *almacenan imagenes y figuras.*
- **model_selected.pkl**: modelo seleccionado.
- **scaler.pkl**: escalador entrenado.
- *requirements.txt*: archivo con los requerimientos de instalación mínima.


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

![img](./static/img/logo.jpg)