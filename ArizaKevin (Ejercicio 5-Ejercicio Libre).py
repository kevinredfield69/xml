# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('padron-comercial.xml')
raiz = doc.getroot()

calle=raw_input("INTRODUCIR NOMBRE DE UNA CALLE: ").upper()
tipo_actividad=raw_input("INTRODUCIR NOMBRE DE UN TIPO DE ACTIVIDAD: ").upper()

print ""

print "LISTA DE COMERCIOS QUE SE ENCUENTRAN EN LA CALLE",calle,"Y REALIZAN EL TIPO DE ACTIVIDAD",tipo_actividad

print ""

for lugar in raiz:
    if lugar.find("CALLE").text == calle:
        if lugar.find("TIPO_ACT").text == tipo_actividad:
            for comercio in lugar.findall("NOMBRE"):
                print comercio.text

