# Challenge Técnico - SWAT

## meli-swat-challenge
Exercício 1 - Scripting

# Escopo

## Problema
Partindo de uma demanda de tarefas de análise, temos a necessidade de consultar e modificar informações de forma massiva. Para agilizar o processo de consulta foi construído um script que realiza a seguinte tarefa:
Recorrer a todos os itens publicados pelos seguintes users:
* `site_id`, `seller_id` (Dados de _input_)
* MLA,326659539
* MLB,244066576

**Considerações:**
1. Utilizar o seguinte filtro para obter somente os que cumpram a condição "Envío" = "Full"
2. Gerar archivo de Loque que contenha os seguintes dados de cada item por user/site

**Estrutura do relatório:**

**site_id**, **seller_id**, **nickname**, **id del ítem**, **title del item**, **category_id** (_donde está
publicado_), **name de la categoría** (_no el id_), currency_symbol+ **price**


**Exemplo:**

_MLA,326659539,FERRETERIA JASPER,MLA752196932,Jaula Trampa Rata Ratón Laucha 30x13x13cm Jasper Caballito,MLA417939,Trampas para Ratas,$960_

## Solução

Através de um _Python script_, que recebe um arquivo `data_input.txt` de entrada de dados de `site_id` e `seller_id`, como saída recebemos um arquivo de LOG no formato CSV, seguindo os seguintes parâmetros de nomenclatura `Output_DD-MM-AA-HH_mm.csv`.

(**Exemplificando:** Output_15-06-21-16_23.csv)

## Pré-requisitos
1. Contar con `Python 3.8.5` o superior.
2. É necessário configurar um arquivo seguro `credencias.cfg`. Temos uma sessão [credencias] onde é necessária uma chave de acesso `appid` e `secret`. Esse ID e Secret é adquirido em https://developers.mercadolivre.com.br.
### Observações
Durante os processos de criação do script foi detectado que as APIs extraídas da documentação não necessitaríam autenticação, para fins de testes foram criados dois scripts `script_challenge_swat_master.py`(com autenticação) e `script_challenge_swat_noauth.py`(sem autenticação). 
Por boas práticas adotaremos o script com autenticação.

