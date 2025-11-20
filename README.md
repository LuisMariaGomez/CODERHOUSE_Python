# Proyecto Django – Gestión de Arcos

## Funcionalidades

Este proyecto es una pequeña aplicación en Django que permite:

* Visualizar una página de inicio

* Crear objetos Arco mediante parámetros en la URL

* Listar todos los arcos guardados en la base de datos

### Modelo: Arco

El modelo Arco representa un arco con los siguientes campos:

* marca (CharField)
* modelo (CharField)
* potencia (IntegerField)
* precio (FloatField)
* tipo (CharField)

### Crear un arco

URL con parámetros dinámicos:
/crear_arco/< marca >/< modelo >/< potencia >/< precio >/< tipo >/

Ejemplos:
```
http://localhost:8000/crear_arco/Hoyt/Helix/60/1250.50/Compuesto/

http://localhost:8000/crear_arco/Bear/Legit/70/980/Recurvo/

http://localhost:8000/crear_arco/Mathews/V3X/65/1999.99/Compuesto/

http://localhost:8000/crear_arco/PSE/Evoke/55/900/Recurvo/
```

## Listar arcos

URL: /lista_arcos/

Devuelve todos los registros de Arco.