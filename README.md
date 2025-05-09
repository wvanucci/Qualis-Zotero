# Qualis-Zotero
# Tutorial de Configuração do Código
## Antes de começar, você precisará de alguns requisitos:

Python: O código foi escrito em Python. Você precisa ter o Python instalado em sua máquina. A versão recomendada é a Python 3.x.

Pacotes Python: O código usa algumas bibliotecas externas que precisam ser instaladas. Use pip para instalar os pacotes necessários.

`pip install requests fuzzywuzzy pandas`

Conta Zotero: Certifique-se de ter uma conta no Zotero. Você pode criar uma conta em https://www.zotero.org/.

API Key Zotero: Você precisará gerar uma chave de API do Zotero, que será usada para autenticar suas requisições.

### Passo 1: Obter a API Key do Zotero

- Acesse sua conta no [Zotero](https://www.zotero.org/).

- Vá para Configurações de [API](https://www.zotero.org/settings/keys0).

- Crie uma nova chave de API.

- Copie a chave (token) de API gerada. Você usará essa chave para autenticar suas requisições para a API do Zotero.
    - OBS: Guarde o UserID da API, você pode precisar 

### Passo 2: Obter o ID do Grupo e da Coleção
- Se você estiver utilizando uma biblioteca de grupo no Zotero, precisará do ID do grupo e da chave da coleção para acessar os itens do grupo.

- ID do Grupo: Vá até a página do seu grupo no Zotero. O ID do grupo geralmente aparece na URL do grupo. Exemplo: `https://www.zotero.org/groups/GROUPID/my_group`, onde GROUPID é o ID do grupo.

- Chave da Coleção: Ao acessar a coleção, procure o ID único da coleção na URL, por exemplo: `https://www.zotero.org/groups/GROUPID/items/KEY_COLLECTION`, onde KEY_COLLECTION é a chave da coleção
    - Outra alternativa é acessar `https://api.zotero.org/users/USER_ID/groups?key=API_KEY`, onde USER_ID é o user id do API e API_KEY é a chave


### Passo 3: Configuração do Código
- Agora, vamos configurar o código com suas próprias informações.

- API Key do Zotero: No código, substitua ZOTERO_API_KEY pela sua chave de API do Zotero.

- ID do Grupo e Chave da Coleção: Substitua o ZOTERO_GROUP_ID pelo ID do seu grupo e COLLECTION_KEY pela chave da coleção que você deseja acessar.

```python
# Configurações
ZOTERO_API_KEY = 'SUA_CHAVE_DE_API_AQUI'
ZOTERO_GROUP_ID = 'ID_DO_SEU_GRUPO_AQUI'  # ID numérico do grupo
COLLECTION_KEY = 'CHAVE_DA_COLECAO_AQUI'  # Chave da coleção
```

- Arquivo CSV de Qualis: O código espera que o arquivo CSV com a lista de periódicos e suas classificações Qualis esteja disponível na máquina. Certifique-se de fornecer o caminho correto do arquivo CSV.

- O arquivo CSV deve ter o seguinte formato (sem cabeçalho):
```yaml
ISSN;NOME_DO_PERIÓDICO;ÁREA;QUALIS
2328-0662;# ISOJ JOURNAL;INTERDISCIPLINAR;C
2237-5953;(RE) PENSANDO DIREITO;DIREITO;B1
```
Atualize o caminho do arquivo no código, onde o arquivo CSV está localizado:
```python
qualis_df = pd.read_csv(r"C:\caminho\para\seu\arquivo\Qualis-2017-2020.csv", sep=';', header=None, dtype=str,
                        names=['ISSN', 'Nome', 'Área', 'Qualis']).drop_duplicates(subset='Nome', keep='first')
```

### Passo 4: Execução do Código

- Agora que você configurou tudo, execute o código para atualizar os itens da coleção com a classificação Qualis. Para fazer isso, basta rodar o script Python:
```bash
python seu_script.py
```

#####  O que o código faz?

- Carregar o arquivo CSV: O código carrega um arquivo CSV com as informações dos periódicos e suas respectivas classificações Qualis.

- Buscar itens na coleção do grupo: O código usa a API do Zotero para acessar todos os itens da coleção especificada no grupo.

- Comparar os títulos: Para cada item, o título do periódico é comparado com a lista de títulos no CSV usando uma correspondência aproximada (fuzzy matching). Se uma correspondência for encontrada, a classificação Qualis correspondente é extraída.

- Atualizar o campo extra: O código então atualiza o campo extra do item no Zotero com a classificação Qualis.

### Passo 5: Entendendo o Fluxo do Código
- Carregar CSV: O código usa a biblioteca `pandas` para carregar e processar o arquivo CSV com os dados de periódicos.

- Chamada da API do Zotero: O código faz requisições à API do Zotero para obter os itens na coleção e depois atualizá-los. Ele usa o método `requests.get` para obter os dados dos itens e o `requests.put` para atualizar o campo `extra`.

- Fuzzy Matching: A biblioteca `fuzzywuzzy` é usada para comparar os títulos dos periódicos no Zotero com os títulos do CSV e encontrar as correspondências mais próximas.

### Passo 6: Possíveis Ajustes para Personalização
- Alterar o Limite de Similaridade: O código usa o fuzzywuzzy para encontrar correspondências de títulos com uma similaridade de 80%. Se você achar que a correspondência precisa ser mais ou menos rigorosa, pode alterar esse limite no código
```python
if similaridade >= 80:
    # Considera a correspondência válida
```
- Alterar os Campos de Atualização: Se você deseja atualizar outro campo além de `extra`, altere o nome do campo no código.

- Alterar a Área ou Tipo de Qualis: O código também pode ser modificado para trabalhar com outras áreas ou categorias de Qualis, dependendo de como o arquivo CSV está estruturado.

### Considerações Finais
- Verifique o código de resposta da API: O código trata erros de resposta da API, como erros 400 ou 500, que podem ocorrer se houver problemas com a autenticação ou se o servidor estiver fora do ar. Se você quiser um tratamento mais robusto de erros, é possível adicionar mais verificações.

- Verifique os limites de requisições da API do Zotero: O Zotero pode ter limites de requisições por minuto ou por dia, então certifique-se de não fazer muitas requisições rapidamente.
