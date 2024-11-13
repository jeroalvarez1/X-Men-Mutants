# Ejercicio X-Men-Mutants

Esta es una API construida con **FastAPI**, utilizando **PostgreSQL** como base de datos y **SQLAlchemy** como ORM. La API se ejecuta con **Docker** y ofrece soporte para versiones **v2** y **v3**. Incluye pruebas unitarias para garantizar el funcionamiento correcto de la API. La API está desplegada en un servidor web.
El ejercicio consiste en dessarrollar una API que permita guardar, detectar, y dar estadisticas de personas mutantes en base a su ADN.

## Características

- **FastAPI** para una API rápida y eficiente.
- **PostgreSQL** como base de datos.
- **SQLAlchemy** como ORM para la gestión de la base de datos.
- **Docker** para facilitar la ejecución del entorno de desarrollo.
- **Tests unitarios** para verificar la funcionalidad.
- Soporte para múltiples versiones de la API: **v2** y **v3**.
- Desplegada en un servidor web para acceso público.

## Instalación y Ejecución con Docker

### Requisitos Previos

- Tener **Docker** y **Docker Compose** instalados en tu máquina.

### Pasos para ejecutar el proyecto localmente

1. **Clonar el repositorio**:

    ```bash
    git clone https://github.com/jeroalvarez1/X-Men-Mutants.git
    cd X-Men-Mutants
    ```

2. **Construir y ejecutar el contenedor de Docker**:

    En el directorio raíz del repositorio, ejecuta:

    ```bash
    docker-compose up --build -d
    ```

3. **Acceder a la aplicación**:

    La API estará disponible localmente en [http://localhost:8000](http://localhost:8000).

## Despliegue en Servidor Web

La API está desplegada en un servidor web accesible públicamente.

- **URL Base**: `http://45.236.130.118:8000/`
- **Versión 2**: `http://45.236.130.118:8000/v2`
- **Versión 3**: `http://45.236.130.118:8000/v3`

### Endpoints Disponibles

###### Nota: para cambiar de versión en el despliegue local, debe modificar en el archivo .env la variable API_VERSION a la verision deseada, v2 o v3. Ej: API_VERSION=v3. Por default en servidor se enceuntra en v3.

#### V2

##### 1. **Verificar si el ADN es de un mutante**

- **Método**: `POST`
- **URL**: `/v2/human/mutant/`
- **Body**:

    ```json
    {
        "dna": [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
    }
    ```
- **Descripción**: Verifica si el ADN es de mutante retornando 403 o 200.

#### V3

##### 1. **Verificar si el ADN es de un mutante**

- **Método**: `POST`
- **URL**: `/v3/human/mutant/`
- **Body**:

    ```json
    {
        "dna": [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG"
        ]
    }
    ```
- **Descripción**: Verifica si el ADN es de mutante retornando 403 o 200 y lo almacena en la base de datos.

##### 2. **Estadísticas de mutantes**

- **Método**: `GET`
- **URL**: `/v3/human/stats/`
- **Descripción**: Obtiene las estadísticas de mutantes y humanos almacenados en la base de datos.