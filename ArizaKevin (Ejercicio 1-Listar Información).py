# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('padron-comercial.xml')
raiz = doc.getroot()

comercios=raiz.findall("Row/NOMBRE")

print "LISTA DE PADRONES COMERCIALES DEL MUNICIPIO DE ALCOBENDAS EN LA COMUNIDAD AUTÓNOMA DE MADRID."

print ""

for comercio in comercios:
    print comercio.text