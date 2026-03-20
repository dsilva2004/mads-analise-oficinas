# Mads Analise Oficinas

Biblioteca Python para gestao e analise de dados de oficinas automoveis.

O modulo trabalha em memoria e disponibiliza funcoes para:
- registo e listagem de utilizadores, oficinas, categorias e compras;
- analise estatistica de compras e faturacao;
- visualizacao em mapa;
- exportacao para JSON e CSV.

## Instalacao

### A partir do PyPI

```bash
pip install mads-analise-oficinas
```

## Importacao

```python
from MadsAnaliseOficinas import *
```

Tambem podes importar funcoes especificas:

```python
from MadsAnaliseOficinas import addUser, addCatOficina, addOficina, registarCompra
```

## Estrutura de dados (em memoria)

O modulo mantem quatro estruturas globais:
- utilizadores (dict)
- categoriasOficinas (list)
- oficinas (dict)
- compras (dict)

Isto significa que os dados existem apenas durante a execucao do programa. Para persistir informacao, usa as funcoes de exportacao.

## Fluxo recomendado

1. Registar categorias de oficina com addCatOficina.
2. Registar oficinas com addOficina.
3. Registar utilizadores com addUser.
4. Registar compras com registarCompra.
5. Consultar listagens, estatisticas, mapa e exportacao.

## API Principal

### Registos

#### addUser(nome, nif, dataNascimento, genero)
Regista um utilizador.

Parametros:
- nome: texto (apenas letras e espacos)
- nif: texto numerico com 9 digitos
- dataNascimento: formato YYYY-MM-DD
- genero: M, F ou Outro

Saida:
- imprime erros de validacao, ou mensagem de sucesso

#### addCatOficina(categoria, cor)
Regista uma categoria de oficina com uma cor para uso no mapa.

Parametros:
- categoria: texto com pelo menos 3 caracteres
- cor: uma das cores permitidas pelo Folium (ex.: blue, red, green)

Saida:
- imprime erros de validacao, ou mensagem de sucesso

#### addOficina(nif, nome, categoria, latitude, longitude, morada, cidade, codigoPostal, horario)
Regista uma oficina.

Validacoes relevantes:
- nif unico com 9 digitos
- categoria tem de existir em categoriasOficinas
- latitude entre -90 e 90
- longitude entre -180 e 180
- codigoPostal no formato XXXX-XXX

#### registarCompra(nifUtilizador, nifOficina, valor, descricao, dataCompra, catCompra)
Regista uma compra associada a utilizador e oficina.

Parametros-chave:
- dataCompra: YYYY-MM-DD
- catCompra: P (Produto) ou S (Servico)

Regras:
- valor maior que 0
- NIFs devem existir
- evita compras duplicadas com os mesmos dados principais

### Listagens

As funcoes de listagem apresentam tabelas com pandas e IPython.display:
- listarCategorias()
- listarOficinas(nif=None, nome=None, categoria=None, cidade=None)
- listarUtilizador(nif=None, nome=None, genero=None)
- listarCompras(idCompra=None, nifUtilizador=None, nifOficina=None, categoria=None, valorMin=None, valorMax=None, dataInicio=None, dataFim=None)

### Mapa

#### mapa()
Gera visualizacao de oficinas no mapa com Folium.

Comportamento:
- monta pontos com base nas oficinas registadas;
- usa categoria/cor definida em categoriasOficinas;
- guarda ficheiro mapa.html;
- apresenta o mapa no ambiente interativo.

### Estatisticas

- verTotalOficinas(): total de oficinas registadas
- verTotalUtilizadores(): total de utilizadores registados
- consultarVolumeFaturação(nif=None): volume de faturacao total ou por oficina
- consultarMaisAdquirido(top=5): top de descricoes mais adquiridas
- listasVolumeVendas(top=10): ranking de oficinas por volume de vendas
- visualizarEvolucaoDespesas(nifUtilizador=None): grafico temporal das despesas

### Exportacao

- exportarParaJSON(): exporta os dados para dados_exportados.json
- exportarParaCSV(): exporta para
	- utilizadores.csv
	- oficinas.csv
	- compras.csv
	- categoriasOficinas.csv

## Exemplo completo

```python
from MadsAnaliseOficinas import *

addCatOficina("Mecanica", "blue")
addCatOficina("Pintura", "red")

addOficina(
		nif="501234567",
		nome="Oficina Centro",
		categoria="Mecanica",
		latitude=41.235,
		longitude=-8.620,
		morada="Rua Central 100",
		cidade="Maia",
		codigoPostal="4470-123",
		horario="09:00-18:00",
)

addUser("Maria Silva", "123456789", "1990-01-15", "F")

registarCompra(
		nifUtilizador="123456789",
		nifOficina="501234567",
		valor=79.90,
		descricao="Mudanca de oleo",
		dataCompra="2026-03-01",
		catCompra="S",
)

listarCompras()
consultarVolumeFaturação()
exportarParaCSV()
```

## Publicacao no PyPI

```bash
python -m build
python -m twine check dist/*
python -m twine upload dist/*
```

