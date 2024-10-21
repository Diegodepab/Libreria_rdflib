# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:56:10 2024

@author: DiegoDePablo
"""

import json
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF

# Cargar los datos desde el archivo JSON
with open('family.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
familia_ns = Namespace("http://www.semanticweb.org/cbarba/FamilyOntology/")

# Crear tripletas RDF para cada miembro de la familia
for persona in data:
    persona_uri = familia_ns[persona["_id"]]

    # Añadir tripletas
    g.add((persona_uri, RDF.type, familia_ns[persona["family_id"]]))  # Tipo del sujeto (Man o Woman)

    # Relación 'hasSon'
    if "hasSon" in persona:
        son_uri = familia_ns[persona["hasSon"]]
        g.add((persona_uri, familia_ns["hasSon"], son_uri))

    # Relación 'hasDaughter'
    if "hasDaughter" in persona:
        daughter_uri = familia_ns[persona["hasDaughter"]]
        g.add((persona_uri, familia_ns["hasDaughter"], daughter_uri))

    # Relación 'hasMother'
    if "hasMother" in persona:
        mother_uri = familia_ns[persona["hasMother"]]
        g.add((persona_uri, familia_ns["hasMother"], mother_uri))

    # Relación 'hasAunt'
    if "hasAunt" in persona:
        aunt_uri = familia_ns[persona["hasAunt"]]
        g.add((persona_uri, familia_ns["hasAunt"], aunt_uri))

    # Relación 'hasBrother'
    if "hasBrother" in persona:
        brother_uri = familia_ns[persona["hasBrother"]]
        g.add((persona_uri, familia_ns["hasBrother"], brother_uri))

    # Peso (Weight)
    if "weight" in persona:
        g.add((persona_uri, familia_ns["weight"], Literal(persona["weight"])))

# Serializar el grafo a formato RDF (por ejemplo, en Turtle)
print(g.serialize(format="turtle"))

# Guardar el grafo en formato N-Triples
g.serialize(destination='triples_familia.nt', format='nt', encoding="utf-8")
