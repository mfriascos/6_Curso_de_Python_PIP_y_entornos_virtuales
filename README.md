# 6_Curso_de_Python_PIP_y_entornos_virtuales

**Curso Platzi de Python con Entornos Virtuales y PIP** 

# Usando Entronos virtuales 

Los ambientes virtuales evitan que hayan choque entre móddulos al tener un ambiente compartido. 

Los pasos para crear entornos virtuales es 

Se comprueba donde está instalado Python3 y Pip3 

```sh
which Python3 pip3
```

En linux, se instala el paquete $ python3-venv

En cada proyecto se crea su propio ambiente virtual 

```sh
python3 -m venv venv
```

Para activar el ambiente 

```sh
source venv/bin/activate
```

Para salir del ambiente virtual 

```sh
deactivate
```

Para revisar la lista de dependencias se utiliza el comando 

```
pip3 freeze
```

Para instalar las versiones en especifico y colabrar en el proyecto se hace 

```
pip3 freeze > requirements.txt
```

Para instalar estos requerimientos se hace 

```
pip3 install -r requirements.txt
```

# Solicitudes HTTP con Requests

La librería request hace peticiones a otro tipo de servidores web desde python 

Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!

# Pandas 

Es una de las librerias más utilizadas y nos sirve para analizar y manipular datos de archivos duros como CSV. 

```python
import pandas as pd 
#Alternativa para project_2del curso de funciones 

df = pd.read_csv('./information_data.csv')  #Para leer el archivo csv 
df = df[df['Continent'] == 'South America'] #Filtramos los datos por south America 

countries = df['Country'].values            #Función de pandas para entregar los valores de Country
percentages= df['World Population Percentage'].values 

charts.generate_pie_chart(countries, percentages)
```

# Python para Backend: Web Server con FastAPI 

Con python se pueden crear web server con FastApi, para instalar se hace: 

```sh 
pip install fastapi
```

```sh
pip install "uvicorn[standard]"
```
Para iniciar uvicorn se escribe: 

```sh 
uvicorn main:app --reload
```

# Qué es Docker

Es una herramienta que sirve para aislar entornos, anteriormente se tenía una versión compartida de python y módulos que se podian entrelazar, luego, con los ambientes virtuales de python se lograron aislar cada dependencia y cada módulo atado a python con eso no se tiene choques entre proyectos y las dependencias y sus versiones. 

Cuanso se quiere llevar el proyecto a la nube, es necesario aislar la versión y posiblemente se pueda colapsar las versiones si no se hace el aislamiento. Esto se realiza con contenedores de docker. 

# Dockerizando Scripts de Python 

Se creará un nuevo archivo, este archivo por nombre tiene Dockerfile, luego se ejecuta 

```docker
FROM python:3.8                                                     #Aquí parte con esa versión instalada

WORKDIR /app                                                        #Creará una carpeta dentro de ese contenedor
COPY requirements.txt /app/requirements.txt                         #Una buena práctica es copiar los archivos 
                                                                    #de las dependiencias

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt   #Se ejecuta el comando para la instalación 
                                                                    #de las dependencias

COPY . /app/                                                        #Se copia todo el código  y se lo lleva hacia app

CMD bash -c "while true; do sleep 1; done"                          #Se crea un ciclo infinito para que siempre 
                                                                    #se esté ejecutando
```

Segundo, se crea un archivo llamado docker-compose.yml, el cual declara como se inicia y desde donde se inicia ese contenedor 

```yaml
services:                           #Se le pondrá un nombre al servicio 
    app-csv:                        #En este caso se llamará app-csv 
        build:
            context: .              #El contexto de ese servicio es la carpeta donde 
                                    #está localizado, para ello se escribe punto (.)
            dockerfile: Dockerfile  #Se indica el archivo dockerfile
        volumes:
            - .:/app                #Se ubica una etiqueta volumes y se indica que todos los archivos
                                    #estén enlazados con /app, se hace con el fin de realizar 
                                    #modificaciones sin que se lance nuevamente el servicio 
```

Se puede ejecutar de dos formas, instalando Docker Engine y Docker Desktop, en este caso se instalan todas las dependencias necesarias que se encuentran en la documentación de docker, se inicia el docker dektop y se espera a que este se inicie, una vez se inicia se ejecutan los comandos, en caso de que no se instale docker desktop, se instala docker engine y docker-compose, cuando se ejecuten los comandos, necesariamente se antepone el comando sudo. 

```sh
docker-compose build                #Este comando realiza la construcción del sistema, y se ejecuta cada una de 
                                    #las instrucciones del docker file 
docker-compose up -d                #Con este comando se lanza el proyecto
docker-compose ps                   #Se escribe para ver el estado de ese contenedor 
docker-compose exec app-csv bash    #Se ejecuta esa aplicación, se pone el nombre del servicio y que lo lance 
                                    #en un terminal de tipo bash 
docker-compose down                 #En caso de cometerse un error en algún archivo, es necesario digitar down
                                    #antes de lanzarlo nuevamente 
```
# Dockerizando Web Services

Se utiliza para mantener un servicio en línea 

Para realizar este tipo de dockerización se modifica el archivo DockerFile de la siguiente manera 

```docker
FROM python:3.8                                                     #Aquí parte con esa versión instalada

WORKDIR /app                                                        #Creará una carpeta dentro de ese contenedor
COPY requirements.txt /app/requirements.txt                         #Una buena práctica es copiar los archivos 
                                                                    #de las dependiencias

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt   #Se ejecuta el comando para la instalación 
                                                                    #de las dependencias

COPY . /app/                                                        #Se copia todo el código  y se lo lleva hacia app

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]         #Se lanza el servidor de uvicorn, luego se ingrese a
                                                                    #main y después a app, se ingrese al host con el puerto
                                                                    #0.0.0.0 y se conecte al puerto 80 
```

En el archivo docker-compose, se realiza 

```yaml
services:
  web-server:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
    ports:                      #Se indica que se enlace en el puerto 80 de la máquina
      - '80:80'                 #local y el del contenedor
```




