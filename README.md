# meli-swat
Ejercicio 1 - Scripting

# Challenge Técnico - SWAT

## Demanda
Como parte de nossas tarefas de análise, temos a necessidade de consultar e modificar informações massivamente. Para agilizar o processo de consulta foi construído um script que realiza a seguinte tarefa:
Recorrer a todos os itens publicados pelos seguintes users:
* site_id, seller_id
* MLA,326659539
* MLB,244066576

Considerações:
1. Utilizar el siguiente filtro para obtener solamente los que cumplan esta condición "Envío" = "Full"
2. Generar archivo de LOG que contengan los siguientes datos de cada ítem por cada
user/site:
site_id, seller_id, nickname, id del ítem, title del item, category_id (* donde está
publicado *), name de la categoría (* no el id *), currency_symbol + price
EJEMPLO
MLA, 99999, SampleNickname, MLA999999, "Sample title", MLA11111, "Herramientas", $99
MLB, 22222, SampleNickn2, MLB22221, "Sample title 2", MLB2222, "Herramientas", R$33


## Solución

Se creó un script Python el cual recibe un archivo input en formato CSV para listar los site_id y seller_id requeridos. El script genera un archivo con la siguiente nomenclatura "log DD MM AAAA - HH MM.csv"(Ejemplo 31 05 2021 - 05 30.csv). 
Para mas información, el script genera (o actualiza si ya existe) el archivo "ExecutionLog.txt" en el cual se muestra la secuencia de ejecución del script desde que es iniciado hasta su finalización, indicando fecha y hora de cada registro y errores si ocurrieran dentro de la ejecución.

## Prerequisitos

1. Contar con Python 3.9.5 o superior. Link de descarga: [Python](https://www.python.org/downloads/)

2. Configurar el archivo brindado 'properties.ini'. Dentro de la sección [SETUP] se debe ingresar las claves para los atributos de 'client_id' y 'client_secret'.

## Instalación

Dentro de la consola escribir el siguiente comando:

```bash
git clone https://github.com/Gaston87/ml-challenge.git
cd ml-challenge
pip install -r requisitos.txt
```

## Comandos Script

Help:
```bash
py script.py -h
```

Ejecución:
```bash
py script.py -i input.csv
```
