import logging
import os
from dotenv import load_dotenv
from send_mail import send_mail
from get_addresses import ceps_to_addresses
from pdf_generator import get_addresses_pdf, addresses_to_json


# Template de mensagem do email
MESSAGE_TEMPLATE = """
Prezado(a),

Seguem os dados de endereço do CEP {cep}:
Logradouro: {logradouro}
Complemento: {complemento}
Unidade: {unidade}
Bairro: {bairro}
Localidade: {localidade}
UF: {uf}
Estado: {estado}
Região: {regiao}
IBGE: {ibge}
GIA: {gia}
DDD: {ddd}
SIAFI: {siafi}

Atenciosamente,
Sua equipe
"""


def main():
    load_dotenv()
    try:
        """
        Executa o script principal.
        """
        ceps_to_addresses()
        addresses = addresses_to_json()
        for address in addresses:
            """
            Envia um email para cada endereço encontrado.
            """
            message = MESSAGE_TEMPLATE.format(**address)
            send_mail(
                receivers=os.getenv("EMAIL_RECEIVERS").split(","),
                subject=f"Endereço do CEP {address['cep']}",
                message=message,
            )
        get_addresses_pdf()
    except Exception as e:
        logging.error(f"Erro na execução do script: {e}")


if __name__ == "__main__":
    main()
