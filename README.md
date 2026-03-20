# Mads Analise Oficinas

Pacote Python para analise de dados relacionados com oficinas automoveis.

## Instalacao

```bash
pip install mads-analise-oficinas
```

## Uso rapido

```python
from MadsAnaliseOficinas import addUser, addCatOficina

addUser("Maria", "123456789", "1990-01-15", "F")
addCatOficina("Pintura", "blue")
```

## Desenvolvimento local

```bash
python -m pip install --upgrade build twine
python -m build
python -m twine check dist/*
```

## Publicacao no PyPI

```bash
python -m twine upload dist/*
```

