# coding: utf8
import datetime
import pandas as pd
import requests

from guara import GuaraCRM
from normalize import Normalize
from load import Load
from settings import user_token

def main():
    token = user_token # vindo do settings.py
    guara = GuaraCRM(token)
    inicio = datetime.datetime.now()

    while guara.has_next_page():
        dados_puro = guara.perform(chunk_size = guara._chunk)
        dados_normalizados = Normalize(dados_puro)
        Load(dados_normalizados).perform()
        print(f'..: Lote concluído :..\nInício: {inicio.hour} horas e {inicio.minute} minutos')

    final = datetime.datetime.now()

    print(
        f'Processo finalizado com sucesso!'
        f'\n Início em {inicio.hour} : {inicio.minute}: {inicio.second} - Término em '
        f'{final.hour}: {final.minute}: {final.second}\n'
        f'Processo completo no tempo de {final - inicio}'
    )
if __name__ == "__main__":
    main()

