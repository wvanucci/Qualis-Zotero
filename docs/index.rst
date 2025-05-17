.. -*- coding: utf-8 -*-

Bem-vindo ao qualis-zotero!
===========================

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo:

   usage

Documentação da API
===================

Este módulo oferece funções para processar artigos da biblioteca Zotero, atribuindo estratos Qualis com base em uma planilha CSV e buscando ISSNs ausentes via OpenAlex.

**Funções principais**

- `processar`_: processa os itens da coleção do Zotero e atribui estrato Qualis.
- `load_config`_: carrega o arquivo de configuração YAML.

**Zotero**

- `get_items`_: obtém os itens de uma coleção do Zotero.
- `update_item`_: atualiza o ISSN e Qualis no Zotero.

**Qualis**

- `carregar_base_qualis`_: carrega a planilha do Qualis em memória.

**OpenAlex**

- `buscar_issn`_: busca o ISSN via OpenAlex usando DOI ou título.


.. automodule:: core
   :members:
   :undoc-members:
   :show-inheritance:

Funções principais
------------------
.. _processar:

.. autofunction:: qualis_zotero.core.processar

.. _load_config:

.. autofunction:: qualis_zotero.config.load_config


Zotero
------

.. _get_items:

.. autofunction:: qualis_zotero.zotero.get_items

.. _update_item:

.. autofunction:: qualis_zotero.zotero.update_item


Qualis
------

.. _carregar_base_qualis:

.. autofunction:: qualis_zotero.qualis.carregar_base_qualis


OpenAlex
--------

.. _buscar_issn:

.. autofunction:: qualis_zotero.openalex.buscar_issn

