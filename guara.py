from sqlalchemy import create_engine # type: ignore
import pymysql # type: ignore
import json
import requests

class GuaraCRM:
    '''
    | Classe responsável por fazer a interface com o GuaraCRM e retornar os registros.
    
    '''
    def __init__(self, token):
        self._endpoint = "https://guaracrm.com.br/api/v1/constituents"
        self._headers = {'Content-Type': 'application/json'}
        self._page = 1
        self._result_per_page = 600 # Quantidade de registros por página
        self._token = token
        self._total_pages = 0
        self._chunk = 20 # Quantidade de páginas a serem visitadas antes de salvar no banco

    
    @property
    def url(self):
        ''' Monta endpoint com os parametros para fazer a requisição na API '''
        return f'{self._endpoint}?access_token={self._token}&per_page={self._result_per_page}&page={self._page}'

    
    def has_next_page(self):
        ''' Verifica se possui próxima pagina para ser visitada'''
        return False if self._page is None else True

    
    def hit(self):
        ''' Faz requisição para APi e retorna o conjunto de doadores'''
        response = requests.get(self.url, headers=self._headers)
        json = response.json()
        self._page = json['metadata']['pagination']['next_page']  ##Seta qual a próxima pagina
        self._total_pages = json['metadata']['pagination']['total_pages'] #Seta o total de páginas (apenas para demonstração)
        return json['constituents']

    
    def perform(self, chunk_size):
        ''' Executa requisição para todas as paginas da API.'''
        i = 0
        data = []
        while (self.has_next_page() and i < chunk_size):
            print(f'Pagina {self._page} de {self._total_pages} - '
                  f'{self.percentagem(self._page, self._total_pages):.2f} % do processo')
            data += self.hit()
            i += 1
        return data

    def percentagem(self, divisor, dividendo):
        try:
            _divisor = float(divisor)
            _dividendo = float(dividendo)
            result = 100 * _divisor / _dividendo
            return result if isinstance(result, float) else 0.00
        except ZeroDivisionError:
            return 0.00

