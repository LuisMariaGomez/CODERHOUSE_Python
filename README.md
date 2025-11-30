# Proyecto Django – Gestión de Arcos

## Funcionalidades

Este proyecto es una aplicación en Django que permite gestionar una colección de arcos deportivos con autenticación de usuarios.

### Funcionalidades Principales

#### Autenticación de Usuarios
* **Registrarse**: Crear una nueva cuenta de usuario
* **Iniciar Sesión**: Acceder con credenciales de usuario
* **Cerrar Sesión**: Salir de la sesión actual

#### Gestión de Arcos
* **Crear Arcos**: Crear nuevos arcos mediante un formulario en la página
* **Listar Arcos**: Ver todos los arcos guardados en la base de datos
* **Ver Detalles**: Visualizar la información completa de un arco
* **Editar Arcos**: Modificar los datos de un arco existente
* **Eliminar Arcos**: Borrar arcos de la base de datos
* **Buscar Arcos**: Filtrar arcos por marca, modelo o tipo

#### Panel de Administración
* Acceso a `/admin/` para usuarios administrador
* Crear, editar, listar y eliminar arcos desde el panel de admin
* Gestionar usuarios desde la interfaz administrativa

### Modelo: Arco

El modelo Arco representa un arco deportivo con los siguientes campos:

* **marca** (CharField): Marca fabricante del arco
* **modelo** (CharField): Modelo específico del arco
* **potencia** (IntegerField): Potencia en libras
* **precio** (FloatField): Precio en moneda local
* **tipo** (CharField): Tipo de arco (Compuesto, Recurvo, etc.)

## Rutas Principales

| Ruta | Descripción |
|------|-------------|
| `/` | Página de inicio |
| `/crear_arco/` | Formulario para crear un nuevo arco |
| `/lista_arcos/` | Lista de todos los arcos con opciones de editar y eliminar |
| `/ver_arco/<id>/` | Ver detalles de un arco específico |
| `/editar_arco/<id>/` | Editar un arco existente |
| `/eliminar_arco/<id>/` | Eliminar un arco |
| `/admin/` | Panel de administración (requiere usuario admin) |

## Cómo Crear un Arco

### Desde la Interfaz Web (Recomendado)
1. Navega a `/crear_arco/`
2. Completa el formulario con los datos del arco:
   - Marca
   - Modelo
   - Potencia (en libras)
   - Tipo
   - Precio
3. Haz clic en "Crear Arco"

## Cómo Gestionar Arcos

### Ver Lista de Arcos
* Accede a `/lista_arcos/`
* Visualiza todos los arcos registrados
* Usa el formulario de búsqueda para filtrar por marca, modelo o tipo

### Editar un Arco
* En la lista de arcos, haz clic en "Editar"
* Modifica los datos que desees
* Haz clic en "Guardar cambios"

### Eliminar un Arco
* En la lista de arcos, haz clic en "Eliminar"
* Confirma la eliminación en la página de confirmación

## Panel de Administración

Para acceder al panel de administración:
1. Navega a `/admin/`
2. Inicia sesión con credenciales de usuario administrador
3. Desde aquí puedes:
   - Ver, crear, editar y eliminar arcos
   - Gestionar usuarios
   - Acceder a otras funciones administrativas

## Instalación y Configuración

Para ejecutar este proyecto:

```bash
# 1. Instala las dependencias
pip install -r requirements.txt

# 2. Realiza las migraciones
python manage.py migrate

# 3. Crea un usuario administrador (opcional)
python manage.py createsuperuser

# 4. Inicia el servidor de desarrollo
python manage.py runserver
```

Accede a `http://localhost:8000/` en tu navegador.

## Video de uso

```bash
https://drive.google.com/file/d/1xa_1RJr4vynmIb6GmmozBGPEBHZ9RoDB/view?usp=sharing
```