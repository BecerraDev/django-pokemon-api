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

docker-compose up --build

3. Abre el navegador

Ejecutar proyecto localmente en http://localhost:8000.


# Credenciales:

Usuario: bbecerra
Contraseña: becerra123

// Para crear un super usuario, ingresar este comando:

python create_superuser.py

// Revisar usuarios, ingresar este comando. ( es necesario estar logeado )

localhost:8000/admin

# Solución: 

La solución fue diseñada con un enfoque en el rendimiento y la experiencia del usuario, priorizando una navegación fluida dentro de una sola página.
Se optó por no utilizar frameworks SPA como Vue.js, en favor de mantener la simplicidad de la implementación para esta prueba técnica.
Tras evaluar entre el uso de Python tradicional o una API REST, se eligió utilizar Django con renderizado del lado del servidor. Además, se aplicaron buenas prácticas mediante el uso de templates reutilizables, lo que permite mantener el código limpio, organizado y fácil de mantener.

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
-> Docker
-> Endpoints de CRUD POKEMON PERSONALIZADO (revisar urls.py)

## Funcionalidades pendientes

Por motivos de tiempo, las siguientes funcionalidades quedaron sin implementación completa:

- **Registro de nuevo usuario desde el frontend**  
  Actualmente, los usuarios deben crearse desde el panel de administración (`localhost:8000/admin`) o ejecutando el script `python create_superuser.py`.
- **Edición de Pokémon personalizado**  
  El código backend está implementado, pero no está conectado al frontend.
- **Relación Usuario ↔ Pokémon personalizado**  
  Falta una tabla intermedia que asocie cada Pokémon personalizado con su usuario. Actualmente, todos los Pokémon personalizados son globales.
- **Mejoras en la experiencia de usuario (UX)**  
  Algunos mensajes en pantalla están pendientes, así como mantener la posición del scroll después de guardar o eliminar un Pokémon.

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



