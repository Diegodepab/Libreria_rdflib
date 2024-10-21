# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:44:24 2024

@author: DiegoDePablo
"""

import json
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF

# Cargar los datos desde el archivo JSON
with open('proteinas.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
protein_ns = Namespace("http://www.semanticweb.org/cbarba/ProteinOntology/")

# Crear tripletas RDF para cada proteína
for protein in data:
    protein_uri = protein_ns[protein["_id"]]

    # Añadir tripletas
    g.add((protein_uri, RDF.type, protein_ns["Protein"]))  # Tipo del sujeto (Proteína)
    if "nombre" in protein:
        g.add((protein_uri, protein_ns["nombre"], Literal(protein["nombre"])))  # Nombre de la proteína
    g.add((protein_uri, protein_ns["descripcion"], Literal(protein["descripcion"])))  # Descripción
    g.add((protein_uri, protein_ns["funcion"], Literal(protein["funcion"])))  # Función
    g.add((protein_uri, protein_ns["estructura"], Literal(protein["estructura"])))  # Estructura
    g.add((protein_uri, protein_ns["localizacion_celular"], Literal(protein["localizacion_celular"])))  # Localización celular

    # Añadir interacciones con otras proteínas
    if "interaccion" in protein:
        for interaccion in protein["interacciones"]:
            g.add((protein_uri, protein_ns["interactua_con"], protein_ns[interaccion]))
    

# Serializar el grafo a formato RDF (por ejemplo, en Turtle)
print(g.serialize(format="n3").encode("utf-8"))

# Guardar el grafo en formato N-Triples
g.serialize(destination='triples_protein.nt', format='nt', encoding="utf-8")