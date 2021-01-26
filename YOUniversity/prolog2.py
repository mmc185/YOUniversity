# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:45:37 2021

@author: Admin
"""

import pytholog as pl
new_kb = pl.KnowledgeBase("Informatica")

#base di conoscenza:insieme di asserzioni
new_kb(["insegna(P,M):-lezione(M,H,G,P)",  #P=professore M=materia  H=ora inizio  G=giorno della settimana
        "in(aula4,palazzo_aule)",
        "in(aula2,palazzo_aule)",
        "in(aula_b,dib)",
        "in(aula_a,dib)",
        "in(aula_1b,dib)",
        "in(aula_1a,dib)",
        "in(lab_boole,dib)",
        "in(lab_von_neumann,dib)",
        "in(lab_turing,dib)",
        "in(lab_shannon,dib)",
        "corso(di_terlizzi,a)",
        "corso(pirlo,a)",
        "corso(abbattista,a)",
        "corso(centrone,b)",
        "corso(impedovo,b)",
        "corso(roselli,b)",
        "corso(di_mauro,a)",
        "corso(buono,a)",
        "corso(iavernaro,a)",
        "corso(pio,b)",
        "corso(d_amato,b)",
        "corso(pugliese,b)",
        "corso(maggipinto,a)",
        "corso(volpe,b)",
        "corso(novielli,a)",
        "corso(novielli,b)",
        "corso(costabile,a)",
        "corso(costabile,b)",
        "corso(lops,a)",
        "corso(lops,b)",
        "corso(fanizzi,a)",
        "corso(fanizzi,b)",
        "lezione(discreta,9,lunedi,di_terlizzi)",
        "lezione(discreta,12,martedi,di_terlizzi)",
        "lezione(programmazione,15,martedi,abbattista)",
        "lezione(programmazione,9,mercoledi,abbattista)",
        "lezione(aso,11,mercoledi,pirlo)",
        "lezione(aso,9,giovedi,pirlo)",
        "lezione(discreta,11,giovedi,di_terlizzi)",
        "lezione(programmazione,15,giovedi,abbattista)",
        "lezione(programmazione,9,venerdi,abbattista)",
        "lezione(aso,11,venerdi,pirlo)",
        "lezione(discreta,9,lunedi,centrone)",
        "lezione(programmazione,11,lunedi,roselli)",
        "lezione(discreta,9,martedi,centrone)",
        "lezione(programmazione,11,martedi,roselli)",
        "lezione(aso,9,mercoledi,impedovo)",
        "lezione(programmazione,11,mercoledi,roselli)",
        "lezione(discreta,9,giovedi,centrone)",
        "lezione(aso,11,giovedi,impedovo)",
        "lezione(aso,9,venerdi,impedovo)",
        "lezione(calcolo,9,lunedi,iavernaro)",
        "lezione(basi_di_dati,11,lunedi,buono)",
        "lezione(asd,9,martedi,di_mauro)",
        "lezione(basi_di_dati,11,martedi,buono)",
        "lezione(fisica,9,mercoledi,maggipinto)",
        "lezione(calcolo,11,mercoledi,iavernaro)",
        "lezione(asd,9,giovedi,di_mauro)",
        "lezione(basi_di_dati,11,giovedi,buono)",
        "lezione(asd,9,venerdi,di_mauro)",
        "lezione(fisica,10,venerdi,maggipinto)",
        "lezione(calcolo,9,lunedi,pugliese)",
        "lezione(asd,11,lunedi,pio)",
        "lezione(fisica,9,martedi,volpe)",
        "lezione(basi_di_dati,11,martedi,d_amato)",
        "lezione(asd,9,mercoledi,pio)",
        "lezione(calcolo,11,mercoledi,pugliese)",
        "lezione(basi_di_dati,9,giovedi,d_amato)",
        "lezione(fisica,10,giovedi,volpe)",
        "lezione(asd,9,venerdi,pio)",
        "lezione(basi_di_dati,10,venerdi,d_amato)",
        "lezione(mri,11,lunedi,lops)",
        "lezione(icon,13,lunedi,fanizzi)",
        "lezione(reti,15,lunedi,novielli)",
        "lezione(mri,9,martedi,lops)",
        "lezione(reti,14,mercoledi,novielli)",
        "lezione(ium,16,mercoledi,costabile)",
        "lezione(icon,13,giovedi,fanizzi)",
        "lezione(reti,15,giovedi,novielli)", 
        "lezione(mri,13,venerdi,lops)", 
        "lezione(ium,16,venerdi,costabile)",
        "classe(a,aula4)",
        "classe(b,aula2)",
        "classe(a,aula_1b)",
        "classe(b,aula_1a)",
        "luogo(C,X):-classe(C,A),in(A,X)"])  #C=corso X=palazzo A=aula

query="yes"
while(query=="yes"):
    x=input("Inserisci la query oppure inserisci exit per uscire:")
    if(x!="exit"):
        y=new_kb.query(pl.Expr(x))
        print(y)
        z=input("vuoi fare un'altra query?(yes/no)")
        if(z=="no"):
            query="no"
    else:
        break
            
        
