'''
Esercizio 1

Dato un dizionario strutturato ad albero riguardante i voti di uno studente in classe V e VI, 
RESTITUIRE un array contente la media di ogni materia

Esempio: 

medie([
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 1, 'subject' : 'italian', 'V' : 73, 'VI' : 74},
  {'id' : 1, 'subject' : 'german', 'V' : 75, 'VI' : 86}
])

ritorna 

[ (70+82)/2 , (73+74)/2, (75+86)/2 ]

ovvero

[ 76.0 , 73.5, 80.5 ]


'''

def medie(lista):
    # scrivi qui
  
  
  
# INIZIO TEST - NON TOCCARE !
import math

'''
Verifica che i numeri float in lista1 siano simili a quelli di lista2 
'''
def is_list_close(lista1, lista2):
  if len(lista1) != len(lista2):
      return False
    
  for i in range(len(lista1)):
      if not math.isclose(lista1[i], lista2[i]):
          return False
  
  return True


assert is_list_close(medie([
                            {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
                            {'id' : 1, 'subject' : 'italian', 'V' : 73, 'VI' : 74},
                            {'id' : 1, 'subject' : 'german', 'V' : 75, 'VI' : 86}
                          ]),         
                     [ 76.0 , 73.5, 80.5 ])
# FINE TEST
