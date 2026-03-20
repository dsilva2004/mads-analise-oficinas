from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent.resolve()
README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="mads-analise-oficinas",
    version="0.1.0",
    description="Modulo para analise de dados de oficinas automoveis",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Bernardo Pereira, Diogo Silva, Gabriely Bresler",
    author_email="bernardomads@example.com",
    url="https://github.com/dsilva2004/mads-analise-oficinas",
    project_urls={
        "Source": "https://github.com/dsilva2004/mads-analise-oficinas",
        "Issues": "https://github.com/dsilva2004/mads-analise-oficinas/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "folium>=0.15.0",
        "geopandas>=0.14.0",
        "ipython>=8.0.0",
        "matplotlib>=3.7.0",
        "pandas>=2.0.0",
        "requests>=2.31.0",
        "shapely>=2.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    license="MIT",
    keywords="analytics oficinas automoveis pandas",
)