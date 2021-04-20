# scraphones
A command-line application that find and extracts the websites’ logo image URLs and all phone numbers present on the websites.
Aplicação de linha de comando que encontra e extrai o logo, todos os números de telefones dentro dos sites dados

## indice
1. [Requisitos](#Requisitos)
2. [Pastas](#Pastas)
3. [Instalacao](#Instalação)
4. [Execução linha de comando](#Execução-linha-de-comando)
5. [Execução usando imagem docker](#Execução-usando-imagem-docker)
6. [Observações](#Observações)

### Requisitos
- [python 3](https://www.python.org/downloads/) >= 3.6
- [scrapy](https://scrapy.org/)  = 2.4
- [phonenumbers](https://pypi.org/project/phonenumbers/) = 8.12.21

### Pastas
A pasta [phonebot](https://github.com/YuriBoli/scraphones/tree/main/phonebot) contem o projeto scrapy .
##### *[Spiders](https://github.com/YuriBoli/scraphones/tree/main/phonebot/spiders)*
* [utils](https://github.com/YuriBoli/scraphones/tree/main/phonebot/spiders/utils) contém os módulos [logo_filter.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/spiders/utils/logo_filter.py), [phone_filter.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/spiders/utils/phone_filter.py) e [phone_validator.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/spiders/utils/phone_validator.py) que são utilizados no para encontrar logo, telefone e verificar os telefones válidos.
* [phonenumber.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/spiders/phonenumber.py) contém o spider que raspa os sites em busca do logo e telefone.

[items.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/items.py) contém o item modelo de saída.<br />
[middlewares.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/middlewares.py) arquivo gerado automaticamente pelo scrapy.<br />
[pipelines.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/pipelines.py) arquivo gerado automaticamente pelo scrapy.<br />
[settings.py](https://github.com/YuriBoli/scraphones/blob/main/phonebot/settings.py) contém as configurações customizadas do projeto.<br />

### Instalação
para poder [executar](#Execução-linha-de-comando) o bot, é necessário que seja instalado os requisitos(além do python), eles podem ser encontrados no arquivo [requirements.txt](https://github.com/YuriBoli/scraphones/blob/main/requirements.txt).
Para instalar todos os requisitos, execute o comando abaixo:
Linux:

`python3 -m pip install -r requirements.txt `

Windows:

`python -m pip install -r requirements.txt `

Também há a opção de ser criado uma image docker, utilizando o arquivo [dockerfile](https://github.com/YuriBoli/scraphones/blob/main/dockerfile), para criar a imagem, navegue para dentro da pasta [phonebot](https://github.com/YuriBoli/scraphones/tree/main/phonebot) e execute o comando:

`docker build -t phonebot .`

### Execução linha de comando
Para executar o bot, basta navegar até a pasta [phonebot](https://github.com/YuriBoli/scraphones/tree/main/phonebot), colar o arquivo contendo os sites, deve ser usado um arquivo contendo os sites que serão raspados, os sites devem ser separados por quebra de linha(um site por linha). Depois de adicionado o arquivo, rode o comando abaixo, onde websites.txt pode ser substituido pelo seu arquivo contendo os sites:

`cat websites.txt | scrapy crawl phonenumber`

Após a execução irão aparecer dois novos arquivos dentro da pasta [phonebot](https://github.com/YuriBoli/scraphones/tree/main/phonebot), os arquivos **phonenumbers.json** e  **log**, o arquivo **phonenumbers.json**  irá conter o output das informações coletadas nos sites, e o arquivo **log** irá conter o log da aplicação contendo as requisições  feitas e os erros recebidos e gerados.

### Execução usando imagem docker
Para executar o bot utilizando uma imagem docker você vai precisar ter contruido a [imagem](#Instalação) e vai precisar também do arquivo contendo os sites separados por quebra de linha.
Para executar o bot, contando que você tenha permissão, basta rodar o seguinte comando:

`cat websites.txt | docker run -i --name phone_container phonebot`

Após a execução, para pegar os arquivos **phonenumbers.json**  e   **log**  de dentro do container, execute os comandos:

`docker cp phone_container:/phonenumbers.json phonenumbers.json`

`docker cp phone_container:/log log`

O arquivo **phonenumbers.json**  irá conter o output das informações coletadas nos sites, e o arquivo **log** irá conter o log da aplicação contendo as requisições feitas e os erros recebidos e gerados.


### Observações
Sites que o status de resposta for 403, não irão aparecer no json, mas irão aparecer no log informando que não foi possível acessar o site devido à falta de permissões.
