#IMPORTS
import requests
import json
import csv
from datetime import datetime

#VARIABLES
tipo_envio = 'fulfillment' # Para filtrar apenas os envios FULL
categories = {}

#FUNCTIONS
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
	uri = 'https://api.mercadolibre.com/sites/{0}/search?seller_id={1}&shipping={2}&offset={3}'.format(site_id, seller_id, shipping, offset)
	response = requests.get(uri) #headers=get_auth_header())
	response.raise_for_status()
	return json.loads(response.text) #Retorna resposta JSON

def get_category(category_id):
	uri = 'https://api.mercadolibre.com/categories/{0}'.format(category_id)
	response = requests.get(uri)
	response.raise_for_status()
	return json.loads(response.text)

def get_cat_name(category_id):
    categories_name = [get_category(category_id)['name']]
    return (". ".join(categories_name))

def unique_file_name():
    time = "%d-%m-%y-%H_%M"   
    agora = datetime.today()
    return 'Output_' + agora.strftime(time) + '.csv' 

def execute():

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

   #GERA_SAIDA
    
        for item in resultados:
            try:
                with open(unique_file_name(), "a", newline='') as report:
                    wr = csv.writer(report, delimiter=';', quoting=csv.QUOTE_NONE, escapechar='')
                    wr.writerow([
                        site_id,
                        seller['id'],
                        seller['nickname'],
                        item['id'],
                        item['title'],
                        item['category_id'],
                        get_cat_name(item['category_id']),
                        item['currency_id'] + ' $' + str(item['price'])
        ])  
            except Exception as error:
                    print('Erro ao gravar no arquivo CSV - Item: ' + item['id'] + ' Erro: '  + str(error))

    print()
    print('Arquivo gerado: ' + unique_file_name())
    print()
execute()