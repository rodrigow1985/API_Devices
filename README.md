#Bibliografía
1. ```https://www.digitalocean.com/community/tutorials/como-preparar-aplicaciones-de-flask-con-gunicorn-y-nginx-en-ubuntu-18-04-es```
2. ```https://www.youtube.com/watch?v=Esdj9wlBOaI&t=157s```
# Componentes del proyecto
1. Base de Datos MySql
2. PhpMyAdmin
3. Docker - docker-compose
4. Python
    1. Flask

#Tutorial
1. Instalar python
2. Instalar pip
3. Crear un entorno virtual de Python
3.1 ```sudo apt install python3-venv```
3.2 Crear entorno virtual para este proyecto
```python3 -m venv HomeServer_env```
Con esto se instalará una copia local de Python y pip en un directorio llamado ToDo_env dentro del directorio de su proyecto.
3.3 Activar entorno virtual
```source HomeServer_env/bin/activate```
4. Instalar flask
```pip install flask```
    1. Ejemplo sencillo de flask
```
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port:4000)
```

    2. Ejecutar nuestro servidor ```python3 app.py```
5. Configurar la aplicación mediante el archivo .env
6. Empezar los servicios que se utilizan en el proyecto
```
sudo docker-compose up -d
```
Los servicios son los siguientes:
- Base de Datos MySql
- PhpMyAdmin
- API
6. Generar la base de datos mediante ejecutando todas las sentencias establecidas en el archivo "database/schema.sql"
7. Para realizar las pruebas pre configuradas en el desarrollo, revisar el archivo README.md del directorio "test"
#Rutas de ejemplo
1. Swagger
```
http://host:port/version/swagger
```
2. Agregar un nuevo device [method=POST]
```
http://host:port/version/devices
```
3. Obtener todos los devices [method=GET]
```
http://host:port/version/devices
```
4. Obtener un device específico [method=GET]
```
http://host:port/version/devices/{id}
```
5. Actualizar un device específico [method=PUT]
```
http://host:port/version/devices/{id}
```
6. Borrar un device específico [method=DELETE]
```
http://host:port/version/devices/{id}
```