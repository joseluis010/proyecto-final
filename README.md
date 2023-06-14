# Proyecto-final

link a la lista de reproducción del video:

https://www.youtube.com/playlist?list=PLUyQwHt6WAJ6fL8XImmLa6zRtYticfzuj


## BathRooms
Este proyecto es una aplicación web para buscar y agregar información sobre baños públicos en diferentes ciudades. Permite a los usuarios encontrar baños cercanos y agregar nuevos baños a la base de datos.

## Características
º Búsqueda de baños: Los usuarios pueden buscar baños públicos en una ciudad específica. La búsqueda se realiza por país y ciudad, y muestra los resultados de la dirección de los baños encontrados en la ciudad seleccionada.

º Registrar usuarios al sistema.

º Login en el programa para poder ingresar mas baños públicos para poder ser utilizados.

º Agregar información: Los usuarios pueden agregar nuevos baños públicos a la base de datos. Deben proporcionar información como país, ciudad y dirección del baño.

º Validación de datos: El sistema valida los datos ingresados por los usuarios para garantizar la integridad de la información. Se verifican campos obligatorios y se realizan comprobaciones adicionales para asegurarse de que los datos sean válidos y consistentes.

º Mensajes de retroalimentación: Se utilizan mensajes de retroalimentación para informar a los usuarios sobre el resultado de sus acciones. Los mensajes pueden ser de éxito, error o información, y se muestran en la interfaz de usuario para proporcionar una mejor experiencia de uso.









2- hay que instalar el modulo: pip install folium para poder importar el mapa



## Paso a Paso

- Al clonar en git primero debemos ejecutar estos 3 comandos :

º python manage.py makemigrations

º python manage.py migrate

º python manage.py runserver

- En settings  agregar esto  


 ºSTATIC_URL = "static/"

 ºSTATICFILES_DIRS = [BASE_DIR / "static"]

- Hay que instalar el modulo: pip install folium para poder importar el mapa

- Creo una aplicación llamada HOME en la carpeta "aplicacion"

º La agrego en config/settings.py en INSTALLED_APPS = [ ... "home", ]

º En config/urls.py dejo estos valores:

from django.contrib import admin from django.urls import path , include

urlpatterns = [ path('admin/', admin.site.urls), path('', include(("home.urls", "home"))), ]

- En aplicaciones/home/ creamos urls.py y agregamos estos valores
from django.urls import path

from . import views

urlpatterns = [ path('', views.index, name='index'), ] PARA INGRESAR AL INDEX O PANTALLA PRINCIPAL.

- En aplicaciones/home/models.py creamos 4 clases: PAIS, CIUDAD, CALLE donde CIUDAD depende de PAIS y CALLE de ambas 2 y la clase USUARIOS.

En aplicaciones/home/forms.py creamos 4 clases para crear formularios:  
- AgregarInformacionForm donde agregamos: pais, ciudad y calle

- BuscarForm donde buscamos las calles indicando los campos pais y ciudad:

º si la calle no existe la crea y devuelve un mensaje de que fue creado y refresca la pagina º si la calle ya existe nos devuelve un mensaje de que la calle ya existe y no refresca la pagina, nos permite ver si el error fue de tipeo.

- CustomUserCreationForm para crear usuarios, nos pide un nombre de usuario, email, password y confirmación de password.

- CustomAuthenticationForm para loguearse a la aplicación donde corrobora nombre de usuario y password.

En aplicaciones/home/views.py tenemos 6 funciones:

- Una para mostrar el index, 
- About La explicacion acerca de nosotros, 
- Otras 2 para agregar informacion sobre los baños y para buscar calles que tengan baños:

º nos pide agregar el país y la ciudad, si hay calles creadas nos muestra todas. º si no hay calles creadas nos devuelve un mensaje de que no se encontraron calles 
- 2 últimas para registrarse y loguearse

En aplicaciones/home/admin.py
creo los campos en admin: Pais, Ciudad y Calle en el superusercreate pusimos: admin y pass: 1234

Tengo 9 templates:

 º  base.html 

 º  index.html 

 º about.html 

 º navbar.html

 º footer.html

 º register.html

 º login.html 

 º agregar_informacion.html 

 º buscar.html


 ## Cosas a mejorar
- Me hubiera gustado mejorar la plantilla de Bootstrap, pero no comprendí bien esa área, cuando intentaba hacer cambios me daba error mi programa, por eso es que no lo continué.

- La parte de formularios me costó bastante entender, tanto el código que hay que agregar en el html como en el controlador, por eso no avancé a desarrollar LAS VISTAS BASADAS EN CLASES. Hubo mucho de copia y pego y aún intentando buscar la info, no he logrado entenderlo.

- Me costó entender como usar estilos en un archivo .py y .html, algunos pude usar pero buscando info en otras fuentes.

- Aprender a manipular el mapa del menú BUSQUEDA, para que muestre la ubicación de las calles.