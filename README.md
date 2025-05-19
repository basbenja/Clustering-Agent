# **Agente Autónomo de Clusterización**

## **Prerrequisitos para poder ejecutar el proyecto**
#### **1. Crear un entorno virtual de Python 3.12.7**
Para crear un entorno virtual, existen diferentes herramientas. La que yo utilizo se llama
`pyenv`, que permite manejar distintas versiones de Python. En el [repositorio de GitHub
de `pyenv`](https://github.com/pyenv/pyenv) se encuentran las instrucciones para
instalarla.

Una vez instalado `pyenv`, seguir los siguientes pasos:
```bash
pyenv install 3.12.7                      # instala la versión 3.12.7 de Python
pyenv virtualenv 3.12.7 clusering-agent   # crea un entorno llamado "clusering-agent" con Python 3.12.7
pyenv activate clusering-agent            # activa el entorno recién creado
```

#### **2. Instalar dependencias**
Una vez activado el entorno virtual, instalar las dependencias del proyecto, listadas
en el archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

NOTA: `requirements.txt` contiene las dependencias necesarias para poder correr
las dos carpetas del proyecto.