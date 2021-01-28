# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:29:42 2021

@author: marta
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete.CPD import TabularCPD
from pgmpy.inference import VariableElimination

'''
 Funzione per fare inferenza sul voto in base ai dati passati in input
 sotto forma di dizionario (Feature, Valore)
'''
def gradeBayesianInference(evidences):
    grades_infer = VariableElimination(grades)
    votoOffer = grades_infer.query(variables = ['Voto'], evidence = evidences)
    return votoOffer

'''
Creazione della Rete Bayesiana
'''
grades = BayesianModel([('Tempo libero', 'Studiato molto'), 
                        ('Studiato molto', 'Voto'),
                        ('Attitudine', 'Voto'), 
                        ('Fattore Emotivo', 'Voto'),
                        ('Difficolta', 'Voto')  
                       ])

'''
Creazione delle varie tabelle di distribuzione di probabilità
'''
freetime_cpd = TabularCPD('Tempo libero', 5, [[0.07],
                                                [0.17],
                                                [0.38],
                                                [0.28],
                                                [0.1]] )

studiedHard_cpd= TabularCPD('Studiato molto', 3, [[0.95, 0.84, 0.4, 0.2, 0.1],
                                            [0.04, 0.15, 0.59, 0.79, 0.55],
                                            [0.01, 0.01, 0.01, 0.01, 0.35]],
                      evidence=['Tempo libero'], evidence_card=[5])

aptitude_cpd = TabularCPD('Attitudine', 2, [[0.6], [0.4]])

emotionalFactor_cpd = TabularCPD('Fattore Emotivo', 2, [[0.3], [0.7]])

difficulty_cpd = TabularCPD('Difficolta', 3, [[0.2], [0.5], [0.3]])

grade_cpd = TabularCPD('Voto', 3, [[0.60,0.70,0.85,0.80,0.90,0.95,0.15,0.35,0.60,0.25,0.43,0.65,0.50,0.45,0.55,0.35,0.41,0.65,0.17,0.25,0.35,0.10,0.19,0.22,0.10,0.15,0.18,0.20,0.22,0.25,0.07,0.06,0.05,0.06,0.10,0.15],
                                  [0.35,0.27,0.14,0.17,0.08,0.04,0.70,0.55,0.35,0.65,0.50,0.32,0.30,0.40,0.35,0.55,0.53,0.32,0.63,0.60,0.55,0.40,0.43,0.48,0.50,0.58,0.60,0.46,0.55,0.58,0.10,0.30,0.50,0.27,0.40,0.45],
                                  [0.05,0.03,0.01,0.03,0.02,0.01,0.15,0.10,0.05,0.10,0.07,0.03,0.20,0.15,0.10,0.10,0.06,0.03,0.20,0.15,0.10,0.50,0.38,0.30,0.40,0.27,0.22,0.34,0.23,0.17,0.83,0.64,0.45,0.67,0.50,0.40],
], evidence=['Studiato molto', 'Attitudine', 'Fattore Emotivo', 'Difficolta'], evidence_card=[3, 2, 2, 3])


grades.add_cpds(freetime_cpd, studiedHard_cpd, aptitude_cpd, emotionalFactor_cpd, difficulty_cpd, grade_cpd)

# Controlla che le probabilità siano state impostate correttamente
if not grades.check_model():
    print("Errore nella generazione della Rete Bayesiana!")
    exit
    
    
# Esempio:
#print(gradeBayesianInference({'Fattore Emotivo':0}))

    
    

