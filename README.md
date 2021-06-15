# meli-swat
Ejercicio 1 - Scripting

# Challenge Técnico - SWAT

## Demanda
Como parte de nossas tarefas de análise, temos a necessidade de consultar e modificar informações massivamente. Para agilizar o processo de consulta foi construído um script que realiza a seguinte tarefa:
Recorrer a todos os itens publicados pelos seguintes users:
* site_id, seller_id (Dados de _input_)
* MLA,326659539
* MLB,244066576

**Considerações:**
1. Utilizar o seguinte filtro para obter somente os que cumpram a condição "Envío" = "Full"
2. Gerar archivo de Loque que contenha os seguintes dados de cada item por user/site

**Estrutura do relatório:**

**site_id**, **seller_id**, **nickname**, **id del ítem**, **title del item**, **category_id** (_donde está
publicado_), **name de la categoría** (_no el id_), currency_symbol+ **price**


**Exemplo:**

_MLA, 99999, SampleNickname, MLA999999, "Sample title", MLA11111, "Herramientas", $99
MLB, 22222, SampleNickn2, MLB22221, "Sample title 2", MLB2222, "Herramientas", R$33_


## Solução

Foi criado um _Python script_ que recebe um arquivo `data_input.txt` de input com os dadso de site_id e seller_id. A execução do script gera um arquivo no formato CSV, seguindo os seguintes parâmetros de nomenclatura `Output_DD-MM-AA-HH_mm.csv`.

(**Exemplificando:** Output_14-06-21-20_18.csv)


## Prerequisitos

1. Contar con Python 3.9.5 o superior. Link de descarga: [Python](https://www.python.org/downloads/)

2. Configurar el archivo brindado 'properties.ini'. Dentro de la sección [SETUP] se debe ingresar las claves para los atributos de 'client_id' y 'client_secret'.
