# web-crawling-and-scraping

# Introdução

Este repositório contém um projeto de web scraping desenvolvido utilizando o framework Scrapy para extrair todas as notícias dos sites de nóticias "Folha" e "Globo" que contenham o termo "Segurança da Informação". Em seguida, os dados são armazenados em um arquivo JSON e carregados em uma tabela do BigQuery usando um notebook Colab.

# Objetivo

O objetivo deste projeto é automatizar a coleta de notícias relevantes sobre "Segurança da Informação" do site "Folha", armazená-las em um formato estruturado (JSON) e, em seguida, carregá-las em uma tabela do BigQuery para análise posterior.

# Funcionalidades

O projeto possui as seguintes funcionalidades:

Web Scraping com Scrapy: Utiliza o framework Scrapy para extrair as notícias da página da "Folha" que contenham o termo "Segurança da Informação".

Armazenamento em JSON: Os dados coletados são estruturados em formato JSON e armazenados em um arquivo.

Carregamento para o BigQuery: Os dados são carregados em uma tabela específica do BigQuery para facilitar a análise e o compartilhamento dos resultados.

Notebook Colab: O projeto inclui um notebook Jupyter hospedado no Google Colab, que executa o carregamento dos dados no BigQuery e também pode ser usado para análise exploratória dos dados.

# Pré-requisitos

Antes de executar o projeto, é necessário ter os seguintes pré-requisitos configurados:

Ter o Python instalado na versão 2.9 ou superior.
Ter o Scrapy instalado na versão 3.10.9 ou superior.
Ter uma conta no Google Cloud Platform (GCP) e configurar o acesso ao BigQuery.

Esperamos que este projeto seja útil e facilite a coleta e análise de notícias. 
# :) 
