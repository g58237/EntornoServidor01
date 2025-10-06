# Pasos de despliegue
## Paso 1
Se crea un repositorio local del proyecto Django con Git con el comando git init.
## Paso 2
Se usa el comando git add . para agregar los archivos y las carpetas, que contiene el proyecto Django, al repositorio, menos las carpetas vacías del proyecto, git las omitirá.
## Paso 3
Se crea un archivo .gitignore y que contenga como cadena de texto la carpeta venv para que Git lo ignore y cuando se quiera subir el proyecto a GitHub, no suba esa carpeta de dependencias y que tiene el entorno virtual para Django.
## Paso 4
se usa git status para ver las últimas modificaciones del repositorio de git.
## Paso 5
Se procede a usar git commit -m "Aquí se pone algo relacionado con los cambios realizados."
## Paso 6
Se vincula el repositorio local al repositorio de GitHub mediante el comando git remote add origin URL del repositorio de GitHub.
## Paso 7
Se usa git push -u origin master para subir el repositorio de git a GitHub.
## Paso 8
Cuando este subido el repositorio a GitHub, se procede a iniciar sesión en el servidor y cambiar el directorio de trabajo a /var/www con el comando cd, a continuación, se usa el comando git clone URL del repositorio de GitHub para descargar el repositorio del proyecto en el directorio de trabajo.
## Paso 9
Se usa el comando cd nombre del repositorio descargado y se crea un nuevo entorno virtual con el comando python3 -m venv venv, al usar un un servidor linux usamos el comando source venv/bin/activate para activar el nuevo entorno virtual.
Se usan los siguientes comandos de pip dentro del entorno virtual:
- pip install --upgrade pip
- pip install Django
Con estos comandos se actualiza pip, el gestor de dependencias de Python y se instala el framework Django dentro del entorno virtual para el proyecto.
Si se dispone de requirements.txt en la carpeta raíz del proyecto, se puede proceder a usar el comando pip install -r requirements.txt.
## Paso 10
Se edita el archivo settings.py del proyecto Django:
1. se cambia el valor True de la variable DEBUG a False.
2. Se introduce el ip del servidor, localhost y 127.0.0.1 en el array de ALLOWED_HOSTS.
3. Se crean las siguientes variables con sus respectivos valores: STATIC_URL = '/static/', STATIC_ROOT = '/var/www/proyecto/static', MEDIA_URL = '/media/', MEDIA_ROOT = '/var/www/proyecto/media'.
4. Se usa el comando Python manage.py collectstatic. Si da error con los recursos estáticos, se debe quitar o comentar la línea de la variable STATICFILES_DIRS.
## Paso 11
Se revisa que el archivo wsgi.py tenga os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings') y application = get_wsgi_application().
## Paso 12
Se crea el archivo de configuración de apache con la extensión .conf en /etc.
## Paso 13
Se habilita el archivo de configuración de apache con el comando sudo a2ensite proyecto y se recarga el proceso de apache2 con el comando sudo systemctl reload apache2.
## Paso 14
Se introduce la IP del servidor en la barra de dirección y de búsqueda de un navegador web y tendrá que ejecutarse la aplicación Django exitosamente.

# Reflexión
En el entorno local se debe realizar todas las modificaciones de una aplicación, hacer todas pruebas necesarias para que la aplicación funcione como se espera, en caso de error o fallo, se deberá arreglar si ha habido algún error o fallo durante las pruebas. Una vez que la aplicación ha pasado con éxito las pruebas, se podrá desplegar la aplicación en el entorno de producción.