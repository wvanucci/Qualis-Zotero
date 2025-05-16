.. -*- coding: utf-8 -*-

Uso da Biblioteca
=================

Este tutorial mostra como obter as credenciais e configurar a biblioteca
``qualis-zotero`` para uso em seu projeto Python ou ambiente como Google Colab.

1. Obter a Zotero API Key
--------------------------

Para acessar sua biblioteca Zotero via API, você precisa de uma chave pessoal:

- Acesse: https://www.zotero.org/settings/keys
- Clique em **Create new private key**
- Dê permissão de leitura e escrita (Read/Write) para o tipo de biblioteca (pessoal ou grupo)
- Copie a chave gerada (será algo como ``abc123...``)

2. Encontrar o Zotero Group ID
------------------------------

Se você está usando um grupo do Zotero:

- Vá até: https://www.zotero.org/groups
- Clique no grupo desejado
- O número que aparece na URL (ex: ``https://www.zotero.org/groups/1234567/nomedogrupo``) é o seu ``group_id``

3. Obter a Collection Key
--------------------------

Cada coleção dentro de um grupo tem uma chave:

- No navegador, acesse a coleção dentro do grupo
- Veja o parâmetro ``collectionKey=`` na URL
- Exemplo: ``collectionKey=ABCD1234``

4. Base Qualis (CSV)
--------------------

Baixe o arquivo CSV com as informações do Qualis (ex: do Qualis Capes 2017-2020):

- Salve o arquivo localmente e anote o caminho
- Esse caminho será usado como ``qualis_csv_path``

5. Exemplo de uso
-----------------

.. code-block:: python

    from qualis_zotero import processar

    config = {
        "zotero_api_key": "SUA_CHAVE_API_AQUI",
        "zotero_group_id": "SEU_ID_GRUPO",
        "collection_key": "SUA_CHAVE_COLECAO",
        "qualis_csv_path": "caminho/para/qualis.csv"
    }

    processar(**config)

Essa abordagem permite executar a análise diretamente via scripts, notebooks ou no Google Colab.

``qualis-zotero`` irá:

- Tentar recuperar o ISSN de artigos via OpenAlex
- Verificar a classificação Qualis com base no ISSN ou nome da revista
- Atualizar automaticamente o campo *extra* do Zotero com o estrato Qualis
