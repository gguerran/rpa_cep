import logging
import os
from fpdf import FPDF
from fpdf.fonts import FontFace
from fpdf.enums import TableCellFillMode
from dotenv import load_dotenv


class PDF(FPDF):
    """
    Classe para gerar o PDF com os endereços.
    """
    def header(self):
        self.set_font("helvetica", "B", 12)
        self.cell(80)
        self.cell(30, 10, "Endereços", align="C")
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", style="B", size=8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


def addresses_to_json():
    """
    Lê o arquivo CSV e converte os endereços em um dicionário.
    """
    load_dotenv()
    try:
        with open(os.getenv("OUTPUT_CSV_FILE"), "r") as file:
            data = file.read()
        data = data.split("\n")
        keys = data[0].split(",")
        addresses = []
        for row in data[1:]:
            address = {}
            for i, value in enumerate(row.split(",")):
                address[keys[i]] = value
            if address.get("cep"):
                addresses.append(address)
        return addresses
    except Exception as e:
        logging.error(f"Erro: não foi possível ler o arquivo CSV. {e}")


def get_addresses_pdf():
    """
    Gera o PDF com os endereços.
    """
    data = addresses_to_json()
    try:
        pdf = PDF()
        pdf.set_font("helvetica", size=12)
        pdf.add_page()

        headings_style = FontFace()

        with pdf.table(
            borders_layout="HORIZONTAL_LINES",
            cell_fill_color=(224, 235, 255),
            cell_fill_mode=TableCellFillMode.EVEN_ROWS,
            repeat_headings=False,
            width=160,
            headings_style=headings_style,
        ) as table:
            for data_row in data:
                row = table.row()
                cel1 = (
                    f"CEP: {data_row['cep']}\n"
                    if data_row.get("cep")
                    else "CEP: Não encontrado\n"
                )
                cel1 += (
                    f"Logradouro: {data_row['logradouro']}\n"
                    if data_row.get("logradouro")
                    else "Logradouro: Não encontrado\n"
                )
                cel1 += (
                    f"Complemento: {data_row['complemento']}\n"
                    if data_row.get("complemento")
                    else "Complemento: Não encontrado\n"
                )
                cel1 += (
                    f"Unidade: {data_row['unidade']}\n"
                    if data_row.get("unidade")
                    else "Unidade: Não encontrado\n"
                )
                cel1 += (
                    f"Bairro: {data_row['bairro']}\n"
                    if data_row.get("bairro")
                    else "Bairro: Não encontrado\n"
                )
                cel1 += (
                    f"Localidade: {data_row['localidade']}\n"
                    if data_row.get("localidade")
                    else "Localidade: Não encontrado\n"
                )
                cel1 += (
                    f"UF: {data_row['uf']}\n"
                    if data_row.get("uf")
                    else "UF: Não encontrado\n"
                )

                cel2 = (
                    f"Estado: {data_row['estado']}\n"
                    if data_row.get("estado")
                    else "Estado: Não encontrado\n"
                )
                cel2 += (
                    f"Região: {data_row['regiao']}\n"
                    if data_row.get("regiao")
                    else "Região: Não encontrado\n"
                )
                cel2 += (
                    f"IBGE: {data_row['ibge']}\n"
                    if data_row.get("ibge")
                    else "IBGE: Não encontrado\n"
                )
                cel2 += (
                    f"GIA: {data_row['gia']}\n"
                    if data_row.get("gia")
                    else "GIA: Não encontrado\n"
                )
                cel2 += (
                    f"DDD: {data_row['ddd']}\n"
                    if data_row.get("ddd")
                    else "DDD: Não encontrado\n"
                )
                cel2 += (
                    f"SIAFI: {data_row['siafi']}\n"
                    if data_row.get("siafi")
                    else "SIAFI: Não encontrado\n"
                )
                row.cell(cel1, align="L", v_align="T")
                row.cell(cel2, align="L", v_align="T")

        pdf.output("addresses.pdf")
    except Exception as e:
        logging.error(f"Erro: não foi possível gerar o PDF. {e}")


get_addresses_pdf()
