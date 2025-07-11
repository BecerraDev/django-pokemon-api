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

# INSTALACIÓN (one-click setup)

**Requisitos previos:**

- Tener instalado DOCKER DESKTOP y DOCKER COMPOSER en sistema.
- Asegurarse de que Docker Desktop esté abierto y en ejecución antes de iniciar el proyecto.

**Pasos para clonar y levantar el proyecto:**

1. Clonar este repositorio desde la terminal ( CMD ): 

   ``` git clone https://github.com/BecerraDev/django-pokemon-api ```

2. Acceder al directorio del proyecto:
   
   ``` cd django-pokemon-api ```

3. Construye y levanta los contenedores con Docker Compose:

   ``` docker-compose up --build ```

4. Abre tú navegador y accede a:

   ``` [http://localhost:8000](http://localhost:8000) ```


# Credenciales:

- Usuario: bbecerra
- Contraseña: becerra123

Nota: El filtrado y la búsqueda de datos desde la PokéAPI pueden tardar algunos segundos, ya que dependen de la velocidad de respuesta del servicio externo. / Algunas imágenes de Pokémon pueden no cargarse correctamente debido a posibles problemas temporales en la API (Sucede en la tarde o noche) Los datos obtenidos siguen siendo correctos.

# Guia de uso:

Al acceder al servidor en localhost:8000, se redirige automáticamente a la página de inicio (Home). En esta página, se presenta un modal solicitando al usuario iniciar sesión. El modal puede cerrarse en cualquier momento, permitiendo al usuario continuar navegando con normalidad. Sin embargo, solo los usuarios autenticados tienen acceso a las funcionalidades relacionadas con la base de datos. Las vistas protegidas, como la de /pokemon, requieren autenticación.

*Una vez que el usuario ingresa sus credenciales correctamente y accede a la opción "Pokemon" en el Navbar, el sistema despliega una landing page que incluye filtros y una opción de búsqueda de Pokémon conectada a la Poke API.*

La búsqueda y los filtros cuentan con validaciones. Si el usuario realiza una búsqueda por nombre y luego selecciona otro filtro, la búsqueda se reinicia automáticamente para evitar errores. Durante la búsqueda, los selectores de filtro se bloquean y se muestra un ícono de carga para indicar que el sistema está procesando la solicitud.

*El usuario puede seleccionar una carta de Pokémon para ver más detalles sobre el mismo. Los datos obtenidos de la Poke API se visualizan en un gráfico, el cual se actualiza dinámicamente con la nueva información.*

Más abajo, se ofrece la opción de agregar un Pokémon personalizado. Para que el Pokémon tenga una imagen asociada, el usuario debe proporcionar una URL válida que comience con http y termine en .png. Posteriormente, el sistema lista todos los Pokémon personalizados agregados.

**Para crear un superusuario, ejecuta el siguiente comando en la terminal:**

python create_superuser.py Nota: Asegúrate de tener Python correctamente instalado en tu entorno de desarrollo.

**Para gestionar los usuarios, accede a la interfaz de administración de Django en la siguiente URL:**

localhost:8000/admin

# Solución: 

La solución fue diseñada con un enfoque en el rendimiento y la experiencia del usuario, priorizando una navegación fluida dentro de una sola página.
Se optó por no utilizar frameworks SPA como Vue.js, en favor de mantener la simplicidad de la implementación para esta prueba técnica.
Tras evaluar entre el uso de Python tradicional o una API REST, se eligió utilizar Django con renderizado del lado del servidor. Además, se aplicaron buenas prácticas mediante el uso de templates reutilizables, lo que permite mantener el código limpio, organizado y fácil de mantener.

El sistema puede funcionar sin conexión a la API externa si ya se ha iniciado previamente localmente

## Funcionalidades principales

- **Filtro por tipo**
- **Filtro por nombre**
- **Aplicación de limitaciones sobre los datos obtenidos**
- **Actualización dinámica de gráfico según los nuevos datos**
- **Autenticación de usuario** (login/logout) usando `django.contrib.auth`
- **Protección de vistas** mediante `LoginRequired` (solo usuarios autenticados acceden a funcionalidades específicas)
- **Manejador de errores para la API externa** (el sistema puede seguir funcionando offline o si la API externa no está disponible)
- **CRUD para Pokémon personalizado** (creación, listado, actualización y eliminación)
- **Docker**
- **Endpoints de CRUD para Pokémon personalizado** (revisar `urls.py`)

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

# El procesamiento de los datos obtenidos desde la POKE API se realiza en dos etapas:

En el backend (Django): los datos son filtrados y transformados para entregar al frontend solo la información relevante. Esto incluye la creación de estructuras específicas (como arrays con los datos procesados).

En el frontend: se llevan a cabo cálculos adicionales, ordenamientos y visualizaciones (por ejemplo, conteos por tipo de Pokémon, estadísticas promedio, etc.). Esto me permitió aprovechar herramientas de visualización como gráficos o tablas interactivas usando JavaScript. Esta separación busca mantener el backend liviano, actuando como proveedor de datos procesados, y delegar la parte visual y de análisis dinámico al navegador del usuario.

## Estructura del desarrollo
# Día 1

Investigación sobre Python Django.

Creación de un mapa visual para planificar el desarrollo del proyecto.

Creación de repositorio en GitHub.

# Día 2

Implementación de Auth User con Django.

Desarrollo del login funcional y validación de usuarios.

Organización del código en carpetas reutilizables y creación de HTML base usando buenas prácticas (partials, base HTML).

Comentarios en el código.

# Día 3

Desarrollo de maqueta de funciones en backend.

Conexión con API externa, listado y creación de script AJAX.

Creación del CRUD para gestionar Pokémon personalizados (tabla en base de datos).

Pruebas para cada función implementada.

# Día 4

Desarrollo de elementos visuales con Tailwind CSS.

Adaptación de los datos del backend a los elementos visuales.

Implementación de mensajes interactivos para usuarios (modals, script AJAX, página interactiva).

# Día 5

Corrección de bugs.

Comentarios en el código faltante.

Revisión de scripts y eliminación de código redundante.

Realización de pruebas en backend.

# Día 6

Continuación de corrección de bugs.

Implementación de más elementos visuales.

Corrección de errores surgidos el día anterior.

Renderización de páginas, alineación de elementos y evitar hardcoding en el código, asegurando que el backend maneje el listado de Pokémon externos.

# Día 7

Creación de Dockerfile.

Creación de contenedores y despliegue.

Subida del proyecto a GitHub.

Pruebas del proyecto en otro entorno.

Envío del proyecto para evaluación.





