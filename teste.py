from qualis_zotero import processar, load_config, processar_com_config

config = {'zotero_api_key': "",
          'zotero_group_id': '',
          "collection_key" : '',
          "qualis_csv_path": r"C:\UsersQualis-2017-2020.csv" }

processar(**config)

