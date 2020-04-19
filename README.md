# Teste Cognitivo.ai backend

Os arquivos do teste estão localizados no diretório `cognitivo-backend-test`. No diretório `api` se encontra o projeto de uma aplicação para servir os resultados gravados no banco de dados através de um endpoint http, feito em Flask e containerizado.

As dependências necessários estão listadas no arquivo `requirements.txt` e podem ser instaladas através do seguinte comando:

```sh
$ pip install -r requirements.txt
```

## Configuração

Para a execução do arquivo do teste, é necessário configurar algumas variáveis de ambiente. São elas:

- `TWITTER_CONSUMER_KEY` e `TWITTER_CONSUMER_SECRET`: chaves da API do Twitter.
- `DATABASE_URI`: URI para o banco de dados SQL no qual os dados serão salvos.

Para a a execução do servidor em `/api` é necessário configurar a seguinte variável de ambiente:

- `DATABASE_URI`: URI para o banco de dados SQL no qual os dados estão gravados.

## Pontos a aperfeiçoar

- Melhor tratamento de exceções no geral. Por exemplo, quando as variáveis de ambiente necessárias não estão configuradas.
- Paginação no servidor
- Montar um pipeline que pudesse ser executado automaticamente a cada semana para atualizar as métricas da AppStore: Seria coletado o CSV com as informações, carregadas e feitas as análises dos aplicativos mais avaliados e disparados jobs em uma fila para consultar a API do Twitter e atualizar o banco de dados. Por fim este pipeline poderia até mandar uma notificação por email, sms ou slack avisando ao responsável sobre o término do pipeline de coleta de dados.
