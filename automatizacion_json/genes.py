# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:26:19 2024

@author: DiegoDePablo
"""

import json
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF

# Cargar los datos desde el archivo JSON
with open('genes.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
gene_ns = Namespace("http://www.semanticweb.org/cbarba/GeneOntology/")

# Crear tripletas RDF para cada gen
for gene in data:
    gene_uri = gene_ns[gene["_id"]]

    # Añadir tripletas
    g.add((gene_uri, RDF.type, gene_ns["Gene"]))  # Tipo del sujeto (Gen)
    g.add((gene_uri, gene_ns["nombre"], Literal(gene["nombre"])))  # Nombre del gen
    g.add((gene_uri, gene_ns["descripcion"], Literal(gene["descripcion"])))  # Descripción

    # Añadir tripletas para la ubicación
    g.add((gene_uri, gene_ns["cromosoma"], Literal(gene["ubicacion"]["cromosoma"])))
    g.add((gene_uri, gene_ns["ubicacion_inicio"], Literal(gene["ubicacion"]["inicio"])))
    g.add((gene_uri, gene_ns["ubicacion_fin"], Literal(gene["ubicacion"]["fin"])))

    # Añadir tripletas para el contenido de nucleótidos
    g.add((gene_uri, gene_ns["AT_contenido"], Literal(gene["contenido_nucleotidos"]["AT"])))
    g.add((gene_uri, gene_ns["GC_contenido"], Literal(gene["contenido_nucleotidos"]["GC"])))

    # Añadir la función
    g.add((gene_uri, gene_ns["funcion"], Literal(gene["funcion"])))

    # Añadir el organismo
    g.add((gene_uri, gene_ns["organismo"], Literal(gene["organismo"])))

    # Añadir otros atributos (dominio y enfermedades asociadas)
    g.add((gene_uri, gene_ns["dominio"], Literal(gene["otros_atributos"]["dominio"])))
    
    # Añadir enfermedades asociadas como una lista
    for enfermedad in gene["otros_atributos"]["enfermedades_asociadas"]:
        g.add((gene_uri, gene_ns["enfermedad_asociada"], Literal(enfermedad)))


print(g.serialize(format="n3").encode("utf-8"))

# Guardar el grafo en formato N-Triples
g.serialize(destination='triples_genes.nt', format='nt', encoding="utf-8")
