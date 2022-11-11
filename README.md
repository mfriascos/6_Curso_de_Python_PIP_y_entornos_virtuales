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

