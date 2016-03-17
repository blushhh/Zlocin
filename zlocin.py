# -*- coding: utf-8 -*-

dnk = open("dnk.txt").read()

#Žiga
ziga_spol = "TGCAGGAACTTC"
ziga_rasa = "AAAACCTCA"
ziga_barva_las = "TTAGCTATCGC"
ziga_barva_oci = "AAGTAGTGAC"
ziga_oblika_obraza = "ACCACAA"

#Matej
matej_spol = "TGCAGGAACTTC"
matej_rasa = "AAAACCTCA"
matej_barva_las = "CCAGCAATCGC"
matej_barva_oci = "TTGTGGTGGC"
matej_oblika_obraza = "AGGCCTCA"

#Miha
miha_spol = "TGCAGGAACTTC"
miha_rasa = "AAAACCTCA"
miha_barva_las = "GCCAGTGCCG"
miha_barva_oci = "GGGAGGTGGC"
miha_oblika_obraza = "GCCACGG"

match = "1 match found: "

if (dnk.find(ziga_spol)>0) and (dnk.find(ziga_rasa)>0) and (dnk.find(ziga_barva_las)>0) and (dnk.find(ziga_barva_oci)>0) and (dnk.find(ziga_oblika_obraza)>0):
    print match + "Sladoled je pojedel Žiga."

if (dnk.find(matej_spol)>0) and (dnk.find(matej_rasa)>0) and (dnk.find(matej_barva_las)>0) and (dnk.find(matej_barva_oci)>0) and (dnk.find(matej_oblika_obraza)>0):
    print match + "Sladoled je pojedel Matej."

if (dnk.find(miha_spol)>0) and (dnk.find(miha_rasa)>0) and (dnk.find(miha_barva_las)>0) and (dnk.find(miha_barva_oci)>0) and (dnk.find(miha_oblika_obraza)>0):
    print match + "Sladoled je pojedel Miha."



