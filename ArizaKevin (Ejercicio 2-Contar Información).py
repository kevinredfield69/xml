# -*- coding: utf-8 -*-

from lxml import etree
doc = etree.parse('padron-comercial.xml')
raiz = doc.getroot()

lista_calles=[]

for calle in raiz:
    calles=calle.find("CALLE").text
    lista_calles.append(calles)

lista_comercios=[]

for calles in lista_calles:
    if calles not in lista_comercios:
        print "LA CALLE",calles,"TIENE",lista_calles.count(calles),"COMERCIOS."
        lista_comercios.append(calles)






