# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:45:37 2021

@author: Admin
"""
import pytholog as pl
new_kb = pl.KnowledgeBase("Informatica")

#base di conoscenza: insieme di asserzioni
new_kb([
        "insegna(fanizzi,icon)",          #insegna(Professore,Materia)
        "insegna(costabile,ium)",
        "insegna(lops,mri)",
        "insegna(novielli,reti)",
        "insegna(di_terlizzi,discreta)",
        "insegna(centrone,discreta)",
        "insegna(abbattista,programmazione)",
        "insegna(roselli,programmazione)",
        "insegna(pirlo,aso)",
        "insegna(impedovo,aso)",
        "insegna(di_mauro,asd)",
        "insegna(pio,asd)",
        "insegna(buono,basi_di_dati)",
        "insegna(d_amato,basi_di_dati)",
        "insegna(iavernaro,calcolo)",
        "insegna(pugliese,calcolo)",
        "insegna(maggipinto,fisica)",
        "insegna(volpe,fisica)",
        
        "in(aula4,palazzo_aule)",          #in(Aula,Edificio)
        "in(aula2,palazzo_aule)",
        "in(aula_b,dib)",
        "in(aula_a,dib)",
        "in(aula_1b,dib)",
        "in(aula_1a,dib)",
        "in(lab_boole,dib)",
        "in(lab_von_neumann,dib)",
        "in(lab_turing,dib)",
        "in(lab_shannon,dib)",
        
        "corso(di_terlizzi,a1)",     #corso(Professore,Anno_corso)
        "corso(pirlo,a1)",
        "corso(abbattista,a1)",
        "corso(centrone,b1)",
        "corso(impedovo,b1)",
        "corso(roselli,b1)",
        "corso(di_mauro,a2)",
        "corso(buono,a2)",
        "corso(iavernaro,a2)",
        "corso(pio,b2)",
        "corso(d_amato,b2)",
        "corso(pugliese,b2)",
        "corso(maggipinto,a2)",
        "corso(volpe,b2)",
        "corso(novielli,a3)",
        "corso(novielli,b3)",
        "corso(costabile,a3)",
        "corso(costabile,b3)",
        "corso(lops,a3)",
        "corso(lops,b3)",
        "corso(fanizzi,a3)",
        "corso(fanizzi,b3)",
        
        "orario(di_terlizzi,h9,lunedi)",   #orario(Professore,Ora_inizio,Giorno)
        "orario(di_terlizzi,h12,martedi)",
        "orario(abbattista,h15,martedi)",
        "orario(abbattista,h9,mercoledi)",
        "orario(pirlo,h11,mercoledi)",
        "orario(pirlo,h9,giovedi)",
        "orario(di_terlizzi,h11,giovedi)",
        "orario(abbattista,h15,giovedi)",
        "orario(abbattista,h9,venerdi)",
        "orario(pirlo,h11,venerdi)",
        "orario(centrone,h9,lunedi)",
        "orario(roselli,h11,lunedi,roselli)",
        "orario(discreta,h9,martedi,centrone)",
        "orario(roselli,h11,martedi)",
        "orario(impedovo,h9,mercoledi)",
        "orario(roselli,h11,mercoledi)",
        "orario(centrone,h9,giovedi)",
        "orario(impedovo,h11,giovedi)",
        "orario(impedovo,h9,venerdi)",
        "orario(iavernaro,h9,lunedi)",
        "orario(buono,h11,lunedi)",
        "orario(di_mauro,h9,martedi)",
        "orario(buono,h11,martedi)",
        "orario(maggipinto,h9,mercoledi)",
        "orario(iavernaro,h11,mercoledi)",
        "orario(di_mauro,h9,giovedi)",
        "orario(buono,h11,giovedi)",
        "orario(di_mauro,h9,venerdi)",
        "orario(maggipinto,h10,venerdi)",
        "orario(pugliese,h9,lunedi)",
        "orario(pio,h11,lunedi)",
        "orario(volpe,h9,martedi)",
        "orario(d_amato,h11,martedi)",
        "orario(pio,h9,mercoledi)",
        "orario(pugliese,h11,mercoledi)",
        "orario(d_amato,h9,giovedi)",
        "orario(volpe,h10,giovedi)",
        "orario(pio,h9,venerdi)",
        "orario(d_amato,h10,venerdi)",
        "orario(lops,h11,lunedi)",
        "orario(fanizzi,h13,lunedi)",
        "orario(novielli,h15,lunedi)",
        "orario(lops,h9,martedi)",
        "orario(novielli,h14,mercoledi)",
        "orario(costabile,16,mercoledi)",
        "orario(fanizzi,h13,giovedi)",
        "orario(novielli,h15,giovedi)", 
        "orario(lops,h13,venerdi)", 
        "orario(costabile,16,venerdi)",
        
        #lezione(Materia,Ora_inizio,Giorno,Professore):-insegna(Professore,Materia),orario(Professore,Ora_inizio,Giorno)
        "lezione(M,H,G,P):-insegna(P,M),orario(P,H,G)",
        
        
        "classe(a1,aula4)",         #classe(Anno_corso,Aula)
        "classe(b1,aula2)",
        "classe(a2,aula_1b)",
        "classe(b2,aula_1a)",
        
        "luogo(C,X):-classe(C,A),in(A,X)"])  #luogo(Corso,Palazzo):-classe(Corso,Aula),in(Aula,Palazzo)

def ask_KB(new_kb, x): 
    results=set()
    print("Query: " + str(x))
    y=new_kb.query(pl.Expr(x))

    print("Risultati\n", y)
    # Elimina i duplicati dai risultati
    s = ""
    for e in y:
        s = str(e)
        results.add(s)
    return results

#Esempio di utilizzo:
#print(ask_KB(new_kb,"insegna(Q,discreta)") )        
