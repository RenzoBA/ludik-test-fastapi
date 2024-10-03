# Implementación del CRUD en un Framework Desconocido

Este proyecto consiste en la implementación de un CRUD (Crear, Leer, Actualizar
y Eliminar) para un sistema de gestión de productos utilizando FastAPI, un
framework moderno y de alto rendimiento para construir APIs con Python 3.12.7 y
SQLite.

## Funcionalidades del CRUD

El CRUD implementa las siguientes funcionalidades para la gestión de productos:

- **Crear Producto:** Permite añadir un nuevo producto al sistema.
- **Leer Productos:** Permite obtener la lista de productos o un producto
  específico.
- **Actualizar Producto (PUT):** Permite actualizar la información de un
  producto existente.
- **Actualizar Producto (PATCH):** Permite modificar algunos campos de un
  producto existente.
- **Eliminar Producto:** Permite eliminar un producto del sistema.

### Campos de Producto

Cada producto tiene los siguientes campos:

- **id:** Identificador único del producto.
- **name:** Nombre del producto.
- **description:** Descripción del producto.
- **price:** Precio del producto.
- **stock_quantity:** Cantidad disponible del producto.
- **created_at:** Fecha y hora en que se creó el producto.
- **updated_at:** Fecha y hora de la última actualización del producto.

## Requisitos

- Python 3.12.7 instalado en tu máquina. Puedes descargarlo desde
  [python.org](https://www.python.org/).
- FastAPI y Uvicorn para ejecutar la aplicación.

Nota: Windows 11 como sistema operativo (SO).

## Cómo Probar el CRUD

1. **Clona o descarga el repositorio:** Clona o descarga el repositorio en tu
   máquina.

2. **Crea un entorno virtual:** Accede a la carpeta del proyeto, crea un entorno
   virtual con el comando: `python -m venv venv` y accede a él desde la terminal
   `.\venv\Scripts\activate`.

3. **Instalar dependencias:** Instala las dependencias del proyecto con el
   comando: `pip install -r requirements.txt`.

4. **Configura el archivo .env:** Copia el archivo de configuración de ejemplo y
   actualiza las variables de entorno de ser necesario: `cp .env.example .env`.
   Nota: Para este ejemplo se ha utilizado SQLite, por lo que no se requiere
   modificar el valor de `SQLALCHEMY_DATABASE_URL`.

5. **Ejecuta la aplicación:** Desde la carpeta donde se encuentran los archivos
   del proyecto ejecuta el siguiente comando: `uvicorn main:app --reload`

6. **Accede a la documentación de la API:** Una vez que el servidor esté en
   funcionamiento, puedes acceder a la documentación interactiva de la API en
   `http://127.0.0.1:8000/docs`

7. **Resultados:** El script mostrará en la terminal el número total de URLs que
   cumplen con los criterios y también listará las URLs únicas que fueron
   encontradas.

## Documentación del Proceso de Aprendizaje

Para aprender a utilizar FastAPI, utilicé los siguientes recursos:

- **Documentación Oficial de FastAPI:** [FastAPI](https://fastapi.tiangolo.com/)
- **Foros y Contenido en línea:** Stack Overflow, Medium y YouTube.

### Desafíos Enfrentados

- **Familiarización con el Framework:** Dediqué tiempo a entender la estructura
  y las funcionalidades de FastAPI, ya que era un framework desconocido para mí.
- **Manejo de Validaciones:** Implementar validaciones de entrada fue un tanto
  desafiante, pero la documentación oficial fue de gran ayuda para resolver mis
  dudas.
- **Sintaxis y Estructura del Proyecto:** Entender la sintaxis de FastAPI y
  definir la estructura óptima de un proyecto me permitió una noción más clara
  de su implementación.

## Contacto

Si tienes alguna pregunta o necesitas soporte adicional, contáctame a mi
[LinkedIn](https://www.linkedin.com/in/renzo-bocanegra-dev/)
