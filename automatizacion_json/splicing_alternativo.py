# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:48:41 2024

@author: DiegoDePablo
"""
import json
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF

# Cargar los datos desde el archivo JSON
with open('splicing_Alternativo.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
splicing_ns = Namespace("http://www.semanticweb.org/cbarba/SplicingOntology/")
exon_ns = Namespace("http://www.semanticweb.org/cbarba/ExonOntology/")
protein_ns = Namespace("http://www.semanticweb.org/cbarba/ProteinOntology/")

# Crear tripletas RDF para cada evento de splicing alternativo
for event in data:
    event_uri = splicing_ns[event["_id"]]

    # Añadir tripletas
    g.add((event_uri, RDF.type, splicing_ns["SplicingAlternativo"]))  # Tipo del sujeto (Splicing alternativo)
    g.add((event_uri, splicing_ns["descripcion"], Literal(event["descripcion"])))  # Descripción

    # Añadir exones involucrados en el evento de splicing alternativo
    for exon_id in event["exones_id"]:
        exon_uri = exon_ns[exon_id]
        g.add((event_uri, splicing_ns["incluye_exon"], exon_uri))

    # Añadir proteína asociada al evento de splicing alternativo
    proteina_uri = protein_ns[event["proteina_id"]]
    g.add((event_uri, splicing_ns["asociado_a_proteina"], proteina_uri))

# Serializar el grafo a formato RDF (por ejemplo, en Turtle)
print(g.serialize(format="turtle"))

# Guardar el grafo en formato N-Triples
g.serialize(destination='triples_splicing.nt', format='nt', encoding="utf-8")