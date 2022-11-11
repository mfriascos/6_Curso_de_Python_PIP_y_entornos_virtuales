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



