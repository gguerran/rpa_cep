import logging
import os
from dotenv import load_dotenv
from smtplib import SMTP, SMTPException


def send_mail(receivers: list | tuple, subject: str, message: str) -> None:
    """
    :param receivers: Lista de endereços de email
    :param subject: Assunto do email
    :param message: Mensagem do email
    :return: None

    Envia um email com os endereços em anexo.
    """

    load_dotenv()
    sender = os.getenv("EMAIL_SENDER")
    host = os.getenv("EMAIL_HOST")
    port = os.getenv("EMAIL_PORT")
    username = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")

    try:
        server = SMTP(host=host, port=port)
        server.ehlo()
        server.starttls()
        msg = "\r\n".join(
            [
                "From: {}".format(sender),
                "To: {}".format(receivers),
                "Subject: {}".format(subject),
                "",
                message,
            ]
        ).encode("utf-8")

        server.login(user=username, password=password)
        server.sendmail(sender, receivers, msg)
        server.close()
        logging.debug("Email enviado com sucesso")
    except SMTPException:
        logging.error("Erro: não foi possível enviar o email")
    except Exception as e:
        logging.error(f"Erro: {e}")
