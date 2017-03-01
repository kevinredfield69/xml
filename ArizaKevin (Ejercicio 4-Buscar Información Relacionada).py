# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('padron-comercial.xml')
raiz = doc.getroot()

nombre_comercio=raw_input("INTRODUCIR NOMBRE DE UN COMERCIO: ").upper()

print ""

for comercio in raiz:
    if comercio.find("NOMBRE").text == nombre_comercio:
        for calle in comercio.findall("CALLE"):
            print "EL COMERCIO",nombre_comercio,"SE ENCUENTRA EN LA CALLE",calle.text