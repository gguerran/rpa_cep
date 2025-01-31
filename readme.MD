# RPA CEP

Script de busca de endereços pelo CEP, enviando email e gerando PDF.

## Configurar e Executar

1. Clone do  repositório.
2. Vá para a pasta do projeto
3. Crie um virtualenv com Python 3
4. Ative o virtualenv.
5. Crie o arquivo `.env` baseado no `example.env`
6. Instale as dependências.
7. Execute a aplicação

```console
git clone https://github.com/gguerran/rpa_cep.git
cd rpa_cep
python3. -m venv venv
source venv/bin/activate
cp example.env .env
pip install -r requirements.txt
python main.py
```


**Bibliotecas Utilizadas**
----
Para este projeto foram utilizadas as bibliotecas `built-in` do python:
 - [`csv`](https://docs.python.org/3/library/csv.html) Usada para gerar e salvar o CSV com os dados buscados da API;
 -  [`logging`](https://docs.python.org/3/library/logging.html): Usada para gerar logs de erros e informações de debug importantes;
 - [`os`](https://docs.python.org/3/library/os.html): Usada para buscar os dados de variáveis de ambiente definidas no .env;
 - [`smtplib`](https://docs.python.org/3/library/smtplib.html): Usada para o envio dos emails.

Bibliotecas de terceiros:
  - [`fpdf2`](https://py-pdf.github.io/fpdf2/index.html): Usada para gerar o PDF com os dados de endereço;
  - [`pandas`](https://pandas.pydata.org/docs/): Usada para ler o CSV enviado e extrair os dados dos ceps;
   - [`python-dotenv`](https://saurabh-kumar.com/python-dotenv/): Usada para carregar os dados do .env em caso de problemas de compatibilidade;
   - [`requests`](https://requests.readthedocs.io/en/latest/): Usada para enviar requisições ao servidor de endereços.
