import csv
import logging
import os
import pandas as pd
import requests
from dotenv import load_dotenv


def get_addresses():
    """
    Busca os endereços dos CEPs listados no arquivo CSV
    """
    load_dotenv()
    base_url = os.getenv("BASE_CEP_URL")
    data = pd.read_csv("ceps_lista_30.csv")
    data.columns = ["CEP"]
    ceps = data["CEP"].tolist()
    keys = [
        "logradouro",
        "complemento",
        "unidade",
        "bairro",
        "localidade",
        "uf",
        "estado",
        "regiao",
        "ibge",
        "gia",
        "ddd",
        "siafi",
    ]

    addresses = []
    for cep in ceps:
        url = base_url.format(cep=cep)
        data = requests.get(url).json()
        if "erro" in data:
            """
            Se o CEP não for encontrado, o campo "erro" é retornado.
            O CEP não encontrado é ignorado e o programa continua a busca.
            """
            logging.error(f"CEP {cep} não encontrado")
        else:
            addresses.append(data)
    return addresses


def ceps_to_addresses():
    """
    Converte os CEPs do arquivo CSV em endereços e salva em um arquivo CSV.
    """
    addresses = get_addresses()
    try:
        with open(os.getenv("OUTPUT_CSV_FILE"), "w", newline="") as file:

            writer = csv.DictWriter(file, fieldnames=addresses[0].keys())
            writer.writeheader()
            for address in addresses:
                if address:
                    writer.writerow(address)
    except Exception as e:
        logging.error(f"Erro: {e}")
