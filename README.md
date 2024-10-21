# RDF Family Project

Este repositorio contiene un conjunto de scripts que utilizan la librería **RDFLib** en Python para convertir datos estructurados en formato JSON a tripletas RDF. El proyecto se centra en la representación de datos de familias, genes, proteínas y eventos de splicing alternativo, usando ontologías semánticas para modelar relaciones y atributos.

## Tabla de Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Librería Usada](#librería-usada)
- [Estructura de Archivos](#estructura-de-archivos)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Contribuciones](#contribuciones)

## Descripción del Proyecto

El objetivo principal de este proyecto es demostrar cómo estructurar y serializar datos en tripletas RDF utilizando la librería **RDFLib** de Python. Los datos originales se encuentran en formato JSON, y abarcan distintos dominios:

- Información sobre miembros de una familia.
- Datos sobre genes y proteínas.
- Eventos de splicing alternativo.

Cada script genera tripletas RDF, las serializa en formatos como **Turtle** o **N-Triples**, y almacena la información en archivos RDF que pueden ser utilizados en análisis semánticos y aplicaciones web.

## Librería Usada

### RDFLib
[RDFLib](https://rdflib.readthedocs.io/en/stable/) es una librería para trabajar con **RDF** (Resource Description Framework) en Python. RDF es una tecnología clave para representar información sobre recursos en la web, usada en el contexto de la web semántica. Con RDFLib, puedes:

- Crear y manipular gráficos RDF.
- Añadir tripletas RDF a un grafo.
- Serializar y exportar gráficos RDF en diversos formatos, como Turtle y N-Triples.

### Utilidad de RDFLib
**RDFLib** facilita la conversión de datos estructurados (en este caso, JSON) en gráficos RDF, lo cual permite:

- Representar relaciones semánticas complejas entre entidades (por ejemplo, relaciones familiares o interacciones entre proteínas).
- Hacer consultas y análisis sobre estos datos utilizando SPARQL.
- Integrar estos gráficos en aplicaciones que trabajen con ontologías, como bases de datos RDF o herramientas de web semántica.

## Estructura de Archivos

### Carpeta `familia_json`:
- `familia.json`: Datos de una familia en formato JSON.
#### Resultado:
- `triples_familia.nt`: Archivo N-Triples generado con las tripletas RDF de la familia.

### Carpeta `automatizacion_json`:
- `genes.json`: Información sobre genes.
- `exones.json`: Información sobre exones de genes.
- `proteinas.json`: Datos sobre proteínas y sus funciones.
- `splicing_Alternativo.json`: Eventos de splicing alternativo y los exones y proteínas asociadas.

#### Resultados:
- `triples_exon.nt`: Archivo N-Triples generado con los exones.
- `triples_protein.nt`: Archivo N-Triples generado con las proteínas.
- `triples_splicing.nt`: Archivo N-Triples generado con los eventos de splicing alternativo.

### Scripts de conversión:
- `family_to_rdf.py`: Script que convierte los datos de `familia.json` en tripletas RDF.
- `genes_to_rdf.py`: Script que convierte datos de genes en tripletas RDF.
- `proteins_to_rdf.py`: Script que convierte los datos de `proteinas.json` en tripletas RDF.
- `splicing_to_rdf.py`: Script que convierte los eventos de splicing alternativo en tripletas RDF.


## Requisitos

- Python 3.x
- Librería `rdflib` (pip install rdflib)

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tuusuario/rdf-family-project.git
   ```

## Contribuciones

¡Las contribuciones son bienvenidas! todo archivo que ayude a crear ejercicios relacionados a ontologías con el uso de python serán bienvenidos :), siéntete libre de hacer un fork del repositorio y crear un pull request con tus cambios.
