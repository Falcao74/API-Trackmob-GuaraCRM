import pandas as pd
from sqlalchemy import create_engine # type: ignore
from settings import db_server, db_name, db_user, db_password, db_port

class Load:

    '''
    | Classe responsável por carregar os registros no banco de dados MySQL.
    
    '''
    def __init__(self, normalized_data):
        # Transforma json em dataframe do pandas
        self.pd_constituents = pd.json_normalize(normalized_data.constituents, sep='_')
        self.pd_donations = pd.json_normalize(normalized_data.donations, sep='_')
        self.pd_payments = pd.json_normalize(normalized_data.payments, sep='_')
        self.pd_adresses = pd.json_normalize(normalized_data.adresses, sep='_')
        
        # usando list comprehension, evitar que qualquer coluna que tenha um nome maior do que o limite do MySQL.
        limit = 50
        self.pd_payments = self.pd_payments.loc[:, [x for x in self.pd_payments.columns if len(x) < limit]]

        # Cria conexção com o banco
        # Documentação https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls
        self._engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}?charset=utf8mb4')
        ''' 
            Importante: 1 - O pacote pymysql tem de estar instalado e importado
                        2 - Inserir no settings.py (caso seja outra)
                        3 - Esta String é para bancos MYSQL. Caso esteja utilizando outro, alterar a string de acordo.
            
            Sintaxe da engine: (mysql+pymysql://usuario:senha@ip_do_banco/nome_do_banco?charset=codificacao_do_banco)
        '''
    
    def perform(self):
        ''' Faz o insert para cada tabela'''
        self.pd_constituents.to_sql('constituents', self._engine, if_exists='append', index=False)
        self.pd_donations.to_sql('donations', self._engine, if_exists='append', index=False)
        self.pd_payments.to_sql('payments', self._engine, if_exists='append', index=False)
        self.pd_adresses.to_sql('adresses', self._engine, if_exists='append', index=False)

