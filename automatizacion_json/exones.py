import json
from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF

# Cargar los datos desde el archivo JSON
with open('exones.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
exon_ns = Namespace("http://www.semanticweb.org/cbarba/SplicingOntology/")

# Crear tripletas RDF para cada exón
for exon in data:
    exon_uri = exon_ns[exon["_id"]]
    gen_uri = exon_ns[exon["gen_id"]]

    # Añadir tripletas
    g.add((exon_uri, RDF.type, exon_ns["Exon"]))  # Tipo del sujeto (Exón)
    g.add((exon_uri, exon_ns["gen"], gen_uri))  # Gen asociado
    g.add((exon_uri, exon_ns["ubicacion_inicio"], Literal(exon["inicio"])))  # Inicio
    g.add((exon_uri, exon_ns["ubicacion_fin"], Literal(exon["fin"])))  # Fin
    g.add((exon_uri, exon_ns["descripcion"], Literal(exon["descripcion"])))  # Descripción
    g.add((exon_uri, exon_ns["secuencia"], Literal(exon["contenido_nucleotidos"])))  # Contenido nucleotidos

# Serializar el grafo a formato RDF (por ejemplo, en Turtle)
print(g.serialize(format="n3").encode("utf-8"))
g.serialize(destination='triples_exon.nt', format='nt', encoding="utf-8")


#g.serialize(destination='turtle.ttl', format='turtle', encoding="utf-8")


