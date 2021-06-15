# Challenge Técnico - SWAT

## meli-swat-challenge
Exercício 1 - Scripting

# Escopo do Teste

## Problema
Partindo de uma demanda de tarefas de análise, temos a necessidade de consultar e modificar informações de forma massiva. Para agilizar o processo de consulta foi construído um script que realiza a seguinte tarefa:

Recorrer a todos os itens publicados pelos seguintes users:
* `site_id`, `seller_id` (Dados de _input_)
* MLA,326659539
* MLB,244066576

**Considerações:**
1. Utilizar o seguinte filtro para obter somente os que cumpram a condição "Envío" = "Full"
2. Gerar um arquivo LOG que contenha os seguintes dados de cada item por user/site

**Estrutura do relatório:**

**site_id**, **seller_id**, **nickname**, **id del ítem**, **title del item**, **category_id** (_donde está
publicado_), **name de la categoría** (_no el id_), currency_symbol+ **price**


**Exemplo:**

_MLA,326659539,FERRETERIA JASPER,MLA752196932,Jaula Trampa Rata Ratón Laucha 30x13x13cm Jasper Caballito,MLA417939,Trampas para Ratas,$960_

## Solução

Através de um _Python script_, que recebe um arquivo `data_input.txt` de entrada de dados fornecidos (`site_id`,`seller_id`), na saída temos como resultante um arquivo de LOG no formato CSV, com o seguinte parâmetro de nomenclatura `Output_DD-MM-AA-HH_mm.csv`.

(**Exemplificando:** Output_15-06-21-16_23.csv)

## Pré-requisitos
1. Utilizar `Python 3.8.5` ou superior.
2. Os arquivos `data_input.txt`, `credencias.cfg` e `script.py` precisar estar no mesmo diretório.
3. É necessário configurar um arquivo seguro `credencias.cfg`. 
  
    3.1. Na sessão [credencias] é necessária uma chave de acesso `appid` e `secret`. Esse ID e Secret pode ser adquirido em https://developers.mercadolivre.com.br.
 

### Considerações
Seguindo as documentações sugeridas pelo exercício proposto:
1. https://developers.mercadolivre.com.br/pt_br/itens-e-buscas
2. https://developers.mercadolivre.com.br/pt_br/categorias-e-atributos-veiculos
3. https://developers.mercadolivre.com.br/pt_br/localizacao-e-moedas


Durante os processos de criação e teste do script foi detectado que as APIs extraídas das documentações acima não necessitam autenticação para acesso, porém para fins de boas práticas foram criados dois scripts separados, onde o com autenticação é o principal.

1. Principal: `script_challenge_swat_master.py`(com autenticação)
2. Teste: `script_challenge_swat_noauth.py`(sem autenticação). 
