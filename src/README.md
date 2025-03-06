# Resgatando Imagens dos Municípios da Paraíba

Este projeto tem como objetivo exercitar os conhecimentos adquiridos com o GeoServer, permitindo a requisição de imagens de cidades da Paraíba com base no código do município.

## Pré-requisitos

Antes de iniciar, assegure-se de que os seguintes passos foram realizados:

1. **Criação de um Workspace no GeoServer**:

   - Crie um workspace no GeoServer com o nome desejado.

2. **Adição de um Store com o Shapefile dos Municípios da Paraíba**:

   - Baixe o arquivo shapefile dos municípios da Paraíba a partir do link abaixo:
     - [Shapefile dos Municípios da Paraíba](https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2023/UFs/PB/PB_Municipios_2023.zip)
   - No GeoServer, adicione um novo Store utilizando o shapefile baixado.

3. **Publicação de uma Camada a partir do Shapefile**:
   - Publique uma camada no GeoServer utilizando o shapefile dos municípios da Paraíba.

_Para facilitar, você pode utilizar o arquivo ZIP já preparado disponível neste repositório para criar a camada no GeoServer._

## Configuração do Ambiente

1. **Preenchimento do Arquivo `.env`**:

   - Crie um arquivo `.env` na raiz do projeto e preencha-o com as seguintes variáveis:

     ```
     WORKSPACE_NAME=<Nome do Workspace criado no GeoServer>
     LAYER_TITLE=<Título da Camada publicada>
     FORMAT=<Formato suportado pelo WMS, ex: image/png>
     BBOX=<Coordenadas mínimas e máximas para a área desejada, ex: -46.8,-23.6,-46.5,-23.4>
     CODIGO_MUNICIPIO=<Código do município que deseja resgatar, ex: 2511606>
     ```

## Execução do Projeto

1. **Instalação das Dependências**:

   - Certifique-se de que todas as dependências do projeto estão instaladas.

2. **Execução do Script**:

   - Execute o seguinte comando para gerar as imagens:

     ```
     python3 app.py
     ```

   - Este comando irá gerar duas imagens:
     - Uma imagem referente ao estado da Paraíba.
     - Uma imagem específica do município selecionado, conforme o código informado.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para melhorias ou dúvidas.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
