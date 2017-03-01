# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('padron-comercial.xml')
raiz = doc.getroot()

actividad=raw_input("ESCRIBIR TIPO DE ACTIVIDAD: ").upper()

print ""

print "LISTA DE COMERCIOS QUE REALIZAN EL TIPO DE ACTIVIDAD",actividad,"EN EL MUNICIPIO DE ALCOBENDAS."

print ""

for comercio in raiz:
    if comercio.find("TIPO_ACT").text == actividad:
        for comercios in comercio.findall("NOMBRE"):
            print comercios.text