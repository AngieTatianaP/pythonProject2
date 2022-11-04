# Taller Distribuidos

Este proyecto hace uso del patron Publicador/Suscriptor que maneja sensores, una base dates en Mongo.
<img src="/Users/angietatianapenapena/Downloads/patron.png"/>
****

**Base de Datos: (bdsub.py)** La base de datos es un suscriptor que esta leyendo los datos administrados por los sensores y se encarga de almacenarlos en tiempo real en una base de datos de Mongodb cargada en la nube. Este se conecta por medio de credenciales asignadas.  
**Visual: (sub.py)**  La parte visual esta encargada de leer todos los datos que se reciben de los sensores e imprimirlos por pantalla.  
**Ciudades: (cities.json)**  Archivo json que contiene todas las ciudades del mundo  
**Sensores:(sensors.py)**  Esta clase se encarga de tomar el archivo json y convertirlo en lista para asi tomar valores aleatoriamente y alimentar los senosres para tomar los datos.  
**API:**  Se hace uso de una Api que contiene la información en tiempo real de las ciudades del mundo, por lo cual cada sensor recibe la ciudad y accede al api para conocer la información y publicarla.  
**MQTT:** Se hace uso de hivemq para usar mqtt como broker para el patrón.

*****

## Instalación

Para la instalación y funcionamiento de este proyecto se debe instalar hivemq en el dispositivo y correrlo.  
Posteriormente, se inician los suscriptores y publicadores.