#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#IMPORTS
import requests
import json
import csv
from datetime import datetime, timedelta
from multiprocessing import Pool

#VARIABLES
tipo_envio = 'fulfillment' # Para filtrar apenas os envios do tipo FULL
categories = {}
currencies = {}


#FUNCTIONS
##Busca de Itens considerando o offset
def get_search_start(site_id, seller_id, shipping):
	
	offset  = 0
	results = []

	search_result = get_search_offset(site_id, seller_id, shipping, offset)
	results.extend(search_result['results'])  #soma os resultados da paginação
	offset = offset + search_result['paging']['limit'] #Limite de itens retornados por consulta = 50 
	
	while search_result['paging']['total'] > offset: # Repete a consulta enquanto o offset não for maior que a quantidade de itens.
		
		search_result = get_search_offset(site_id, seller_id, shipping, offset)
		results.extend(search_result['results']) #Soma os resultados de todas as consultas
		offset = offset + search_result['paging']['limit']

	return {'seller':search_result['seller'], 'results':results} #Retorna Seller e resultados

def get_search_offset(site_id, seller_id, shipping, offset):
	url = 'https://api.mercadolibre.com/sites/{0}/search?seller_id={1}&shipping={2}&offset={3}'.format(site_id, seller_id, shipping, offset)
	response = requests.get(url)
	response.raise_for_status()
	return json.loads(response.text) #Retorna resposta JSON

##Define nome de arquivo único (por minuto)
def unique_file_name():
    time = "%d-%m-%y-%H_%M"   
    agora = datetime.today()
    return 'Output_' + agora.strftime(time) + '.csv' 

##Get Category name utilizando multiprocessamento
def get_category(category_id):
	url = 'https://api.mercadolibre.com/categories/{0}'.format(category_id)
	response = requests.get(url)
	response.raise_for_status()
	return json.loads(response.text)

def get_cat_name(category_id):
    return categories[category_id]

##Funcao map utilizada para filtrar lista de categorias e simbolo monetário
def multi_map(results, key, value):
	map = {} 
	for result in results:
		map[result[key]] = result[value]
	return map
  
def get_cat_results(category_ids):
	category_ids = [category_id for category_id in category_ids if category_id not in categories.keys()]
	pool = Pool(10)
	return multi_map(pool.map(get_category, category_ids), 'id', 'name') 

def get_curr_symbol(currency_id):
	return currencies[currency_id]

def get_currencies():
	url = 'https://api.mercadolibre.com/currencies'
	response = requests.get(url)
	response.raise_for_status()
	return multi_map(json.loads(response.text), 'id', 'symbol')


##Main - Função Principal
def run():
    #TXT INPUT
    input = csv.reader(open('data_input.txt'), delimiter=',') 

    #MANIPULA DADOS DE ENTRADA
    for [site_in, seller_in] in input:
        site_id         = site_in
        seller_id 		= seller_in
        search_result	= get_search_start(site_id, seller_id, tipo_envio)
        seller			= search_result['seller']
        resultados		= search_result['results']
        print('Consultando Site_ID: ' + site_id + ' e Seller_ID: ' + seller_id)

        global currencies
        global categories
        currencies = get_currencies()

        category_ids = [item["category_id"] for item in resultados]
        categories.update(get_cat_results(list(dict.fromkeys(category_ids)))) #atualiza a lista de categorias
   
   #GERA OUPUT CSV
        
        for item in resultados:
            try:
                with open(unique_file_name(), "a", newline='') as report:
                    wr = csv.writer(report, delimiter=',', quoting=csv.QUOTE_MINIMAL, escapechar='')
                    wr.writerow([
                        site_id,
                        seller['id'],
                        seller['nickname'],
                        item['id'],
                        item['title'],
                        item['category_id'],
                        get_cat_name(item['category_id']),
                        get_curr_symbol(item['currency_id']) + str(item['price'])
        ])  
            except Exception as error:
                    print('Erro ao gravar no arquivo CSV - Item: ' + item['id'] + ' Erro: '  + str(error))

    print()
    print('Arquivo gerado: ' + unique_file_name())
    print()

if __name__ == '__main__':
    try:
        run()
    except Exception as general_error: 
        print('Erro: ' +str(general_error))
