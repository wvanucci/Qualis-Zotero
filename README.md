# qualis-zotero

Ferramenta para automatizar a verificação e classificação de artigos do Zotero com base na tabela Qualis CAPES, utilizando também a API do OpenAlex.

- instalação:  
`!pip install qualis-zotero`

## Antes de começar, existem alguns requisitos:

Python: O código foi escrito em Python. Você precisa ter o Python instalado na sua máquina. A versão recomendada é a Python 3.x.

Pacotes Python: O código usa algumas bibliotecas externas que precisam ser instaladas. Use pip para instalar os pacotes necessários.

`pip install requests fuzzywuzzy pandas rapidfuzz`

Conta Zotero: Certifique-se de ter uma conta no Zotero. Pode criar uma conta em https://www.zotero.org/.

API Key Zotero: Precisará gerar uma chave de API do Zotero, que será usada para autenticar as suas requisições.

### Passo 1: Obter a API Key do Zotero

- Acesse sua conta no [Zotero](https://www.zotero.org/).

- Vá para Configurações de [API](https://www.zotero.org/settings/keys0).

- Crie uma chave de API.

- Copie a chave (token) de API gerada. Usará essa chave para autenticar as suas requisições para a API do Zotero.
    - OBS: Guarde o UserID da API, pode precisar 

### Passo 2: Obter o ID do Grupo e da Coleção
- Se estiver a utilizar uma biblioteca de grupo no Zotero, precisará do ID do grupo e da chave da coleção para acessar os itens.

- ID do Grupo: Vá até a página do seu grupo no Zotero. O ID do grupo geralmente aparece na URL do grupo. Exemplo: `https://www.zotero.org/groups/GROUPID/my_group`, onde GROUPID é o ID do grupo.

- Chave da Coleção: Ao acessar a coleção, procure o ID único da coleção na (URL), por exemplo: `https://www.zotero.org/groups/GROUPID/nome-do-grupo/collections/KEY_COLLECTION`, onde KEY_COLLECTION é a chave da coleção. Copie e 
cole somente a URL abaixo no navegador para encontrar a KEY_COLLECTION da coleção desejada: `https://www.zotero.org/groups/GROUPID/nome-do-grupo/collections`

  - Outras informações: `https://api.zotero.org/users/USER_ID/groups?key=API_KEY`, onde USER_ID é o user ‘id’ do (API) e API_KEY é a chave

## Funcionamento

- Conecta com Zotero via API para obter artigos de uma coleção de grupo.
- Busca o ISSN via DOI ou título usando a API do OpenAlex.
- Atribui o estrato Qualis com base em base CSV fornecida:
    - Acesse o repositório [qualis-zotero](https://github.com/wvanucci/qualis-zotero) para ter acesso da base Qualis.csv do quadriênio 2017 – 2020 
- Atualiza os campos `ISSN` e `extra` nos itens Zotero.
- Usa Fuzzy Correspondência como fallback quando o ISSN não está presente na base Qualis.



Exemplo de uso
-----------------

    from qualis_zotero import processar

    config = {
        "zotero_api_key": "SUA_CHAVE_API_AQUI",
        "zotero_group_id": "SEU_ID_GRUPO",
        "collection_key": "SUA_CHAVE_COLECAO",
        "qualis_csv_path": "caminho/para/qualis.csv"
    }

    processar(**config)

Essa abordagem permite executar a análise diretamente via script, notebook ou no Google Colab.

``qualis-zotero`` irá:

- Tentar recuperar o ISSN de artigos via OpenAlex
- Verificar a classificação Qualis com base no ISSN ou nome da revista
- Atualizar automaticamente o campo *extra* do Zotero com o estrato Qualis

## Instalação local

Clone o repositório e instale localmente:

```bash
git clone https://github.com/wvanucci/qualis-zotero.git
cd qualis-zotero
pip install .


