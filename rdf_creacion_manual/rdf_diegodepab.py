# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:59:20 2024

@author: DiegoDePablo
"""

from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF
# Crear un grafo RDF
g = Graph()

# Definir un namespace para nuestros datos
familia_ns = Namespace("http://www.semanticweb.org/cbarba/family/")

# Hombres de la familia (Man(pepe))
g.add((familia_ns["Pepe"], RDF.type, familia_ns["Man"]))
g.add((familia_ns["Juan"], RDF.type, familia_ns["Man"]))
g.add((familia_ns["Luis"], RDF.type, familia_ns["Man"]))
g.add((familia_ns["Paco"], RDF.type, familia_ns["Man"]))
g.add((familia_ns["Cesar"], RDF.type, familia_ns["Man"]))
g.add((familia_ns["Jose"], RDF.type, familia_ns["Man"]))

# Mujeres de la familia (Woman(lola) )
g.add((familia_ns["Lola"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Ana"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Marta"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Eva"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Sandra"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Maria"], RDF.type, familia_ns["Woman"]))
g.add((familia_ns["Sonia"], RDF.type, familia_ns["Woman"]))


# Relaciones familiares
# hasSon(pepe, juan), hasSon(ana, paco) hasSon(marta, jose)
g.add((familia_ns["Pepe"], familia_ns["hasSon"], familia_ns["Juan"]))
g.add((familia_ns["Ana"], familia_ns["hasSon"], familia_ns["Paco"]))
g.add((familia_ns["Marta"], familia_ns["hasSon"], familia_ns["Jose"]))

# hasDaughter(pepe, ana), hasDaughter(lola, marta), hasDaughter(lola, eva), hasDaughter(marta, maria)
g.add((familia_ns["Pepe"], familia_ns["hasDaughter"], familia_ns["Ana"]))
g.add((familia_ns["Lola"], familia_ns["hasDaughter"], familia_ns["Marta"]))
g.add((familia_ns["Lola"], familia_ns["hasDaughter"], familia_ns["Eva"]))
g.add((familia_ns["Marta"], familia_ns["hasDaughter"], familia_ns["Maria"]))
g.add((familia_ns["Sandra"], familia_ns["hasDaughter"], familia_ns["Sonia"]))

# motherwithonlydaugters(sandra) 
g.add((familia_ns["Sandra"], familia_ns["motherWithOnlyDaughters"], Literal(True)))

# hasUncle(paco, luis)
g.add((familia_ns["Paco"], familia_ns["hasUncle"], familia_ns["Luis"]))

# fatherwithsons(cesar)
g.add((familia_ns["Cesar"], familia_ns["fatherWithSons"], Literal(True)))

# hasSibling(luis, ana), hasSibling(ana, juan)
g.add((familia_ns["Luis"], familia_ns["hasSibling"], familia_ns["Ana"]))
g.add((familia_ns["Ana"], familia_ns["hasSibling"], familia_ns["Juan"]))

# hasAunt(jose, eva), hasAunt(maria, eva)
g.add((familia_ns["Jose"], familia_ns["hasAunt"], familia_ns["Eva"]))
g.add((familia_ns["Maria"], familia_ns["hasAunt"], familia_ns["Eva"]))

#EXTRA DEL DOCUMENTO DEL PROFE:
g.add((familia_ns["Pepe"], familia_ns["hasWeight"],  Literal(75)))

print(g.serialize(format="turtle").encode("utf-8"))
g.serialize(destination='triples_family.nt', format='nt', encoding="utf-8")
