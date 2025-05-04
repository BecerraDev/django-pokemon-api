# django-pokemon-api
Proyecto Django que consume la PokeAPI con CRUD, autenticación y frontend dinámico.

Este proyecto es una API simple en Django que consume datos desde una API externa de Pokémon. Está lista para usarse fácilmente mediante Docker.

Tecnologías utilizadas
- Python 3.10
- Django
- Docker
- SQLite
- API externa: [PokeAPI](https://pokeapi.co/)
- Tailwind
- Ajax + JQUERY

## Despliegue con Docker (one-click setup)

Requisitos previos: 

- Tener instalado DOCKER y DOCKER COMPOSER en sistema. 

1. Clonar este repositorio

git clone https://github.com/tu-usuario/django-pokemon-api.git
cd django-pokemon-api

2. Construye la imagen

docker build -t django-pokemon-api .

3. Corre el contenedor

docker run -p 8000:8000 django-pokemon-api

4. Abre el navegador

Esto ejecutará el servidor en http://localhost:8000.


# Credenciales:

Usuario: bbecerra
Contraseña: adminpassword

// Para cualquier cambio, ingresar /admin. en ese entorno se puede editar o registrar un nuevo usuario, se guarda en base de datos.
Para crear un super usuario, ingresar este comando:

python create_superuser.py

# Solución: 

La solución fue pensada para rendimiento y experiencia de usuario, con navegación fluida en una sola página.
No se utilizaron frameworks SPA ( VUE ) por decisión de simplicidad para esta prueba (Tuve que decidir si usar PYTHON TRADICIONAL O API REST).
Finalmente utilice Python Tradicional con uso de buenas practicas en template para reutilizar codigo. 


El sistema puede funcionar sin conexión a la API externa si ya se ha iniciado previamente localmente

# Funcionalidades principales: 

-> Filtro por tipo
-> Filtro por nombre
-> Aplicación de limitaciones sobre los datos obtenidos
-> Actualización dinamica de gráfico segun los nuevos datos. 
-> Autenticación de usuario (login/logout) usando django.contrib.auth.
-> Protección de vistas mediante LoginRequired (solo usuarios autenticados acceden a funcionalidades específicas)
-> Manejador de errores para la API externa (el sistema puede seguir funcionando offline o si la API externa no está disponible)
-> Creación de CRUD para Pokemon personalizado ( creación, lista, actualización y borrado )

# Funcionalidades no completadas: 

Por motivos de tiempo, las siguientes funcionalidades quedaron pendientes de implementación completa:

-> Registro de nuevo usuario frontend. ( Ingresar localhost:8000/admin -> usuarios -> editar, eliminar, cambiar usuario)
-> Editar Pokemon personalizado. (Codigo esta implementado pero no mostrado en frontend)
-> Relación Usuario - Pokemon personalizado en Base de Datos. (Falto tabla intermedia para conectar usuario a pokemon personalizado (Actualmente son globales)) 
-> Algunos mensajes en pantalla. (Tenía pensado en mantener el scroll en cada guardado y eliminado de pokemon personalizado)

## Estructura del desarrollo
# Dia 1. 
En este día me enfoque en conocer Python DJANGO. 
Me enfoque en crear un mapa visual de como sera el resto de día 
Se crea contenedor GIT HUB

# Dia 2. 
Utilice tutoriales para crear un AUTH USER. 
Me enfoque en dejar el login completamente funcional y validar usuarios con PYTHON DJANGO. 
También en separar carpetas en codigo reutilizable y html base usando buenas practicas. (partials, html base) 
Comentar codigo

# Día 3 
Realicé una maqueta de funciones en BACKEND. 
Conexión de API externa, listado, script de AJAX.
Creación de CRUD (creación de tabla pokemon para guardar pokemones personalizados)
Prueba en cada función

# Día 4
Me enfoque en crear elementos visuales con TAILWIND 
Adaptar datos de backend a elementos visuales
Mensajes interactivos para usuarios (MODALS, SCRIPT AJAX, PAGINA INTERACTIVA)

# Día 5
Correciones de bugs, comentar codigo faltante, revisiones de scripts
Separación de scripts en otro archivo, eliminar cosas redundantes
Buscar errores, realizar pruebas de backend

# Día 6
Seguir corrigiendo bugs, implementar mas cosas visuales y algunos errores que surgieron el día anterior con la corección 
Renderizar paginas, centrar elementos, no hardcodear codigo y que el backend se encarge de listar pokemones externos
-> Proyecto terminado. 

# Día 7
Se crea DockerFile
Se crea contenedores
Se guarda en GIT HUB 
Se realiza prueba en otro entorno
Se envia proyecto para evaluación



